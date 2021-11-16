import json
import logging
import os
import random

try:
    from kafka import KafkaProducer
    from kafka.errors import NoBrokersAvailable, KafkaConnectionError, KafkaError
    from redis import Redis
except ImportError as ime:
    logging.warning(f"Required modules are not available: {ime.name}")
    raise

__version__ = "0.1.1"


class ConfigurationError(Exception):
    """
    Error for missing configuration
    """

    def __init__(self, var, message="Configuration Not available!"):
        self.var = var
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.var} -> {self.message}'


class Configurations:
    @property
    def kafka_host(self):
        var_name = "KAFKA_HOST"
        if os.environ.get(var_name):
            return os.environ.get(var_name)
        raise ConfigurationError(var_name)

    @property
    def kafka_port(self):
        var_name = "KAFKA_PORT"
        if os.environ.get(var_name):
            return os.environ.get(var_name)
        raise ConfigurationError(var_name)

    @property
    def kafka_topic(self):
        var_name = "KAFKA_TOPIC"
        if os.environ.get(var_name):
            return os.environ.get(var_name)
        raise ConfigurationError(var_name)

    @property
    def redis_host(self):
        var_name = "REDIS_HOST"
        if os.environ.get(var_name):
            return os.environ.get(var_name)
        raise ConfigurationError(var_name)

    @property
    def redis_port(self):
        var_name = "REDIS_PORT"
        if os.environ.get(var_name):
            return os.environ.get(var_name)
        raise ConfigurationError(var_name)

    @property
    def redis_db(self):
        var_name = "REDIS_PARTITION_DB"
        if os.environ.get(var_name):
            return os.environ.get(var_name)
        raise ConfigurationError(var_name)

    @property
    def enable_sites_partition(self):
        var_name = "ENABLE_SITES_PARTITION"
        if os.environ.get(var_name):
            return os.environ.get(var_name)
        raise ConfigurationError(var_name)

    @property
    def split_key(self):
        var_name = "SPLIT_KEY"
        if os.environ.get(var_name):
            return os.environ.get(var_name)
        raise ConfigurationError(var_name)

    @property
    def round_robin_enable(self):
        var_name = "ROUND_ROBIN_ENABLE"
        if os.environ.get(var_name):
            return os.environ.get(var_name)
        raise ConfigurationError(var_name)


class KafkaPublisher:
    def __init__(self, **config):
        try:
            default_config = Configurations()
            self.is_connected = False
            self.producer = None
            self.partition_db = Redis(
                host=config.get("redis_host", default_config.redis_host),
                port=config.get("redis_port", default_config.redis_port),
                db=config.get("redis_db", default_config.redis_db),
                decode_responses=True,
            )
            self.host = config.get("kafka_host", default_config.kafka_host)
            self.port = config.get("kafka_port", default_config.kafka_port)
            self.output_topic = config.get("kafka_topic", default_config.kafka_topic)

            self.kafka_broker = [f"{self.host}:{str(self.port)}"]

            self.previous_partition_count = "partition_count"
            self.round_robin_counter_key = "counter"
            if config.get("auto_connect", True):
                self._connect_producer()

            logging.debug(
                f"KAFKA DETAILS: {self.kafka_broker[0]} -> {self.output_topic}"
            )

            self.partition_id_list = []
            self.split_key_partition_mapper = {}
            self._fetch_partition_list()

            self.enable_sites_partition = config.get("enable_sites_partition", default_config.enable_sites_partition)
            self.split_key = config.get("split_key", default_config.split_key)
            self.round_robin_enable = config.get("round_robin_enable", default_config.round_robin_enable)
            self.count = 0
        except Exception as e:
            logging.exception(e)
            raise

    @property
    def __version__(self):
        return __version__

    def _connect_producer(self):
        try:
            logging.info(f"connecting to KAFKA: {self.kafka_broker[0]}")
            self.producer = KafkaProducer(
                bootstrap_servers=self.kafka_broker,
                value_serializer=lambda v: v.encode("utf-8"),
                api_version=(0, 10, 1),
            )
            self.is_connected = True
            logging.info(f"connected to KAFKA: {self.kafka_broker[0]}")
        except Exception as e:
            logging.exception(f"Unable to connect to KAFKA : {e}")
            self.is_connected = False
            raise

    def _fetch_partition_list(self):
        try:
            self.partition_id_list = list(
                self.producer.partitions_for(self.output_topic)
            )
            previous_count = self.partition_db.get(self.previous_partition_count)
            if previous_count and int(len(self.partition_id_list)) != int(
                    previous_count
            ):
                self.partition_db.flushdb()
            self.partition_db.set(
                self.previous_partition_count, len(self.partition_id_list)
            )
        except Exception as e:
            logging.exception(f"error while fetching partition list: {e}")
            raise

    def _flush_kafka_queue(self):
        try:
            self.producer.flush()
        except Exception as e:
            logging.error(f"error while flush kafka queue: {e}")
            raise

    def _flush_partition(self):
        try:
            self._fetch_partition_list()
            self.split_key_partition_mapper = {}
        except Exception as e:
            logging.error(f"error while flushing partition list : {e}")
            raise

    def _get_update_random_partition_id(self, split_key):
        try:
            if self.round_robin_enable:
                round_robin_counter = self.partition_db.get(
                    self.round_robin_counter_key
                )
                round_robin_counter = (
                    0 if round_robin_counter is None else round_robin_counter
                )
                random_partition_id = self.partition_id_list[
                    int(int(round_robin_counter) % len(self.partition_id_list))
                ]
                self.partition_db.set(
                    self.round_robin_counter_key, int(round_robin_counter) + 1
                )
            else:
                random_partition_id = self.partition_id_list[
                    int(random.randint(0, len(self.partition_id_list) - 1))
                ]

            self.partition_db.set(split_key, random_partition_id)  # update redis
            self.split_key_partition_mapper.update(
                {split_key: random_partition_id}
            )  # update mapper in memory
            return random_partition_id
        except Exception as e:
            logging.error(f"error while getting random partition id: {e}")
            raise

    def _publish_message(self, message: dict, random_partition_id: int = 0):
        resp = False
        logging.debug(f"data to be sent: {message}")
        try:
            if random_partition_id is None:
                random_partition_id = 0
            logging.debug(f"sending data to kafka")
            kafka_response = self.producer.send(
                self.output_topic,
                json.dumps(message),
                partition=int(random_partition_id),
            )
            resp = True
            logging.debug(f"sent data to kafka")
        except (
                NoBrokersAvailable,
                KafkaConnectionError,
                KafkaError,
        ) as connection_error:
            logging.error(f"Error in connecting to KAFKA : {connection_error}")
            kafka_response = connection_error
        except Exception as unrecognized_partition:
            logging.error(f"Assuming unknown partition error: {unrecognized_partition}")
            self._flush_partition()
            split_key = message.get(self.split_key)
            random_partition_id = self._get_update_random_partition_id(split_key)
            message["partition"] = str(random_partition_id)
            try:
                kafka_response = self.producer.send(
                    self.output_topic,
                    json.dumps(message),
                    partition=random_partition_id,
                )
                self.producer.flush()
                resp = True
                logging.debug("Message Published to KAFKA after re-fetching partition")
            except Exception as es:
                logging.error(f"Unable to publish message to KAFKA : {es}")
                kafka_response = "Not Published"
        return resp, kafka_response

    def publish(self, message: dict):
        self.perform_task(message=message)

    def perform_task(self, message: dict):
        if not self.is_connected:
            self._connect_producer()
        logging.debug("performing tasks before sending data to kafka")
        msg_id = message.get("msg_id")
        split_key = message.get(self.split_key)
        try:
            if not message.get("data") and len(message["data"]) <= 0:
                logging.warning(
                    f"No tags found in the data payload, Skipping KAFKA publish"
                )
                return
            if not self.enable_sites_partition and split_key is None:
                message["partition"] = ""
                _resp, _resp_text = self._publish_message(message=message)
            if split_key is None:
                random_partition_id = 0
            elif (
                    split_key in self.split_key_partition_mapper
            ):  # check if split key exists in mapping
                random_partition_id = self.split_key_partition_mapper.get(split_key)
            else:
                random_partition_id = self.partition_db.get(
                    split_key
                )  # get partition from redis
                self.split_key_partition_mapper.update({split_key: random_partition_id})
            if (
                    random_partition_id is None
                    or int(random_partition_id) not in self.partition_id_list
            ):  # confirm if partition in partition list
                random_partition_id = self._get_update_random_partition_id(split_key)

            message["partition"] = str(random_partition_id)
            _resp, _resp_text = self._publish_message(
                message=message, random_partition_id=int(random_partition_id)
            )

            logging.info(
                f"MSG_id: {msg_id}  SPLIT_KEY: {split_key} "
                f"PARTITION: {random_partition_id} KAFKA Response: {_resp} : {_resp_text}"
            )

            self.count += 1
            if self.count == 1000:
                self.count = 0
                self._flush_kafka_queue()

        except Exception as es:
            logging.error(
                f"error while parsing message before publishing to KAFKA : {es}"
            )
            raise
