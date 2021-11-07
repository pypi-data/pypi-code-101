import time

from confluent_kafka.admin import AdminClient,ConfigResource,KafkaException
import confluent_kafka
import concurrent.futures


from cube_async_w_kafka.Networkplane.Exceptions import ConnectionError, InterfaceRegistrationFailed, InterfaceAttachFailed, NetworkPlaneFailure, UpdateFailed, UpdateRejected
import logging
from multiprocessing import Process, Event, Queue, Manager

from cube_async_w_kafka.Networkplane.Task import Task

class Network_Plane():
    """
    The main class to manage and live update kafka producers:
    - Regular: with/without data loss & duplication in case of failure.
    - Idempotent: no dataloss no duplication.
    - Transactional.

    Workflow:

            0 - The Network plane should start before starting the interfaces
            1 - It discovers the accessible topic (discover_topic method)
            2 - An interface should register to check if it's topic is known and accessible prior to get a NetPort
            3 - The interface sends records through the NetPort
    """

    def __init__(self,network_plane_spec, to_be_connected_interfaces_spec):

        self._network_plane_spec = network_plane_spec
        self._address = self._network_plane_spec["address"]

        #list of interfaces based on their address with their status: registered, attached ...
        self._interfaces_status = {}
        for interface_spec in to_be_connected_interfaces_spec:
            per_interface_status=Manager().dict()
            per_interface_status["interface_spec"]=interface_spec
            per_interface_status["registered"]=False
            per_interface_status["attached"]=False
            self._interfaces_status[interface_spec["address"]]=per_interface_status

        #gives indication: True/False if the network plane is running or stopped
        self._run_status = Event()
        self._run_status.clear()

        #gives indication: True/False if the network plane is sending data and operational
        self._send_status = Event()
        self._send_status.clear()

        #task handler
        self._task = Task()


        #topics seen by the network plane when connected to kafka broker
        self._accessible_topics = Manager().list()

        #topics that interfaces are working on
        self._active_topics=[]

        #the current producer config dict
        self._producer_config={}

        #stats
        self._latest_stats={}

        #Network plane status
        self.__status=Manager().dict()

        self._P_Live_Sync = None


    def isRunning(self):
        return self._run_status.is_set()

    def isConnected(self,connection_timeout=10):
        try:

            if connection_timeout > 0:

                admin_client = AdminClient(self._producer_config)
                topics=admin_client.list_topics(timeout=connection_timeout).topics
                logging.getLogger(self._address).critical("CHECK Connection: CONNECTION SUCCESS to kafka cluster " + str(self._producer_config['bootstrap.servers']))

                #considered as return True
                return topics

            else:

                logging.getLogger(self._address).error("CHECK Connection: TIMEOUT must be > 0")
                return False

        except Exception as e:

            logging.getLogger(self._address).critical("CHECK Connection: CONNECTION FAILED (timeout="+str(connection_timeout)+") to kafka cluster "+str(self._producer_config['bootstrap.servers'])+", details:"+str(e))
            return False


    def get_Status(self, connection_timeout=10):

        self.__status.clear()

        if connection_timeout > 0:

            self.__status["UP"] = self._run_status.is_set()
            self.__status["SEND"] = self._send_status.is_set()
            self.__status["RUNNING_UPDATE"] = self._task.to_do()
            self.__status["INT"] = self._interfaces_status
            self.__status["ACTIVE_TOPICS"] = self._active_topics
            self.__status["METRICS"]=self.metrics()



            #Check active topics
            discovered_topics=self.isConnected(connection_timeout)

            if discovered_topics:

                self.__status["CONNECTED"] = True
                self.__status["DISCOVERED_TOPICS"] = discovered_topics

                all_topics_still_active=True
                topic_name=""
                for topic in self._active_topics:

                    if not topic["name"] in discovered_topics.keys():
                        all_topics_still_active=False
                        topic_name=topic
                        break

                if all_topics_still_active:
                    logging.getLogger(self._address).info("Check TOPICS Operations - Topics SUCCESS - "+str(self._active_topics))
                    self.__status["ACTIVE_TOPICS_OPS"]=True
                else:
                    logging.getLogger(self._address).critical("Check TOPIC Operations - Topics FAILURE - "+str(topic_name)+" does not exist in the broker or not accessible")
                    self.__status["ACTIVE_TOPICS_OPS"] = False

            else:

                self.__status["CONNECTED"]=False
                self.__status["DISCOVERED_TOPICS"] = False
                self.__status["ACTIVE_TOPICS_OPS"]=False

        else:

            logging.getLogger(self._address).error("timeout must be > 0")

        return self.__status


    def update_producer(self, new_network_plane_spec,update_instructions, connection_timeout=10):
        """
        Live update of the producer config without traffic interruption.
        Only applicable when kafka cluster is reachable, it is not applicable when connection is lost (due to data in the producer instance that we cannot flush in this case).

        :param new_network_plane_spec:
        :param update_instructions:
        :return:
        :raises: UpdateFailed, UpdateRejected
        """


        if self.isConnected(connection_timeout) and self._run_status.is_set() :

            logging.getLogger(self._address).info("updating the network plane")


            if self._task.set("UPDATE_PRODUCER",update_instructions):

                self._network_plane_spec=new_network_plane_spec
                self._producer_config=self.get_producer_config(new_network_plane_spec)

            else:

                raise UpdateFailed("Update failed: task failed to execute")
        else:
            raise UpdateFailed("Update failed: network plane is not started or kafka cluster is unreachable")


    def discover_topics(self, connection_timeout=10):
        """
        Find the list of topic accessible by the network plane
        :param connection_timeout:
        :return:
        """

        try:

            admin_client = AdminClient(self._producer_config)
            topics_dict = admin_client.list_topics(timeout=connection_timeout).topics

            for topic, topicMetadata in topics_dict.items():

                if topic[:2] != '__':
                    self._accessible_topics.append(topic)


        except KafkaException as e:
            logging.getLogger(self._address).critical("kafka cluster unreachable:" +str(self._producer_config['bootstrap.servers']+", connection timed out: "+str(e)))
            raise ConnectionError("kafka cluster unreachable")


    def describe_topic(self, topic, connection_timeout=10):
        """
        Find the description of a specified topic
        :param topic:
        :param connection_timeout:
        :return:
        """

        if not topic in map(lambda x:x["name"],self._active_topics):

            working_topic={"name":topic}

            try:

                admin_client = AdminClient(self._producer_config)
                topic_dict = admin_client.list_topics(topic=topic,timeout=connection_timeout).topics
                topicMetadata=topic_dict[topic]

                topic_configResource = admin_client.describe_configs([ConfigResource(confluent_kafka.admin.RESOURCE_TOPIC, topic)])

                for j in concurrent.futures.as_completed(iter(topic_configResource.values())):
                    config_response = j.result(timeout=connection_timeout)

            except KafkaException as e:

                logging.getLogger(self._address).critical("kafka cluster unreachable:" + str(
                    self._producer_config['bootstrap.servers'] + ", connection timed out: " + str(e)))
                raise ConnectionError("kafka cluster unreachable")



            # data retention in hours
            working_topic["retention_hours"] = int(config_response['retention.ms'].value) / 3600000
            # minimum replica nodes which should send an ACK to say that data is sent
            working_topic["min_insync_replicas"] = int(config_response['min.insync.replicas'].value)

            # get partition metadata
            partitionsMetadata = topicMetadata.partitions


            # number of partitions inside the Topic
            working_topic["partitions"] = len(partitionsMetadata.keys())

            isTopicClean=True
            for part, partMetadata in partitionsMetadata.items():

                if partMetadata.error is not None:
                    isTopicClean=False
                    logging.getLogger(self._address).error("partition: "+str(part)+" in topic: "+topic+" has errors: "+str(partMetadata.error))
                #print(str(part) + ":" + str(partMetadata.replicas)  + ":" + str(partMetadata.error))

            working_topic["partitions_error"]= not isTopicClean

            self._active_topics.append(working_topic)
            return working_topic

        else:

            return list(filter(lambda x:x["name"]==topic,self._active_topics))[0]

    def register(self, interface_spec, connection_timeout=10):
        """
        Register an interface:
        - An interface is successfully registered if its topic matches one of the discovered topic by the network plane
        - If the topic is not discovered during network plane start (does not exist in KAFKA broker) the registration will fail and the interface will not be created)
        :param interface_spec:
        :param connection_timeout:
        :return:
        :raises: InterfaceRegistrationFailed
        """

        """ ---------------------------- Interface Registration ---------------------------- """


        interface_address=interface_spec['address']

        interface_topic=interface_spec['topic']

        try:self._interfaces_status[interface_address]
        except KeyError:
            raise InterfaceRegistrationFailed("registration rejected, interface: " + str(interface_address) + " is not recognized by network plane: " + str(self._address))



        if interface_topic in self._accessible_topics:

            if self._interfaces_status[interface_address]["registered"]==True:

                logging.getLogger(self._address).error("registration rejected, interface: " + str(interface_address) + " is already registered to network plane: " + str(self._address))

                raise InterfaceRegistrationFailed("registration rejected, interface: " + str(interface_address) + " is already registered to network plane: " + str(self._address))

            else:

                try:

                    topic_description=self.describe_topic(interface_topic, connection_timeout)
                    self._interfaces_status[interface_address]["registered"]=True

                    print("registered: "+interface_address)

                    logging.getLogger(self._address).info("interface: "+str(interface_address) + " is successfully registered to network plane: "+str(self._address)+", topic description: "+str(topic_description))

                    return topic_description

                except Exception as e:

                    logging.getLogger(self._address).error("registration failed: "+str(e))

                    raise InterfaceRegistrationFailed("registration failed: "+str(e))

        else:
            raise InterfaceRegistrationFailed("registration failed: interface with topic "+str(interface_topic)+" is not yet recognized by the network plane: "+str(self._address)+" or topic is not created in the kafka cluster")

    def reset(self,interface_address):
        self._interfaces_status[interface_address]["registered"]=False
        self._interfaces_status[interface_address]["attached"]=False




    def get_producer_config(self, network_plane_spec):
        """
        Builds kafka producer config from the network plane spec
        :param network_plane_spec:
        :return:
        """

        kconfig = {}

        # common configurations:
        kconfig['acks'] = -1
        kconfig['max.in.flight.requests.per.connection'] = 5
        kconfig['message.send.max.retries'] = 2147483647

        """ ---------------------------- ID ---------------------------- """
        # The client id is a user-specified string sent in each request to help trace calls.
        # It should logically identify the application and network plane making making the request including the name of cluster destination (to verify destination)
        kconfig['client.id'] = self._address
        # kconfig['client.rack']=network_plane_spec["region"]

        """ ---------------------------- BUFFERING ---------------------------- """

        # The maximum number of unsent messages that can be queued up the producer when using async mode before either the producer must be blocked or data must be dropped.
        kconfig['queue.buffering.max.messages'] = network_plane_spec["buffering"]["buffer-max-records"]

        # Maximum total message size sum allowed on the producer queue.
        # This queue is shared by all topics and partitions.
        # This property has higher priority than queue.buffering.max.messages.
        # default: 1048576 en Kb
        kconfig['queue.buffering.max.kbytes'] = network_plane_spec["buffering"]["buffer-max-size"]

        """ ---------------------------- BATCHING ---------------------------- """

        # Maximum number of messages batched in one MessageSet.
        # The total MessageSet size is also limited by batch.size and message.max.bytes.
        # default: 10000
        kconfig['batch.num.messages'] = network_plane_spec["batching"]["batch-max-records"]
        # Maximum size (in bytes) of all messages batched in one MessageSet, including protocol framing overhead.
        # This limit is applied after the first message has been added to the batch, regardless of the first message's size, this is to ensure that messages that exceed batch.size are produced.
        # The total MessageSet size is also limited by batch.num.messages and message.max.bytes.
        # debault: 1000000
        kconfig['batch.size'] = network_plane_spec["batching"]["batch-max-size"]

        # Delay in milliseconds to wait for messages in the producer queue to accumulate before constructing message batches (MessageSets) to transmit to brokers.
        # A higher value allows larger and more effective (less overhead, improved compression) batches of messages to accumulate at the expense of increased message delivery latency.
        # default 5
        # self._producer_config['queue.buffering.max.ms']=5
        kconfig['linger.ms'] = network_plane_spec["batching"]["batch-build-delay"]

        overhead = 512
        kconfig['message.max.bytes'] = network_plane_spec["batching"]["per-request-max-batches"] * \
                                       network_plane_spec["batching"]["batch-max-size"] + overhead

        """ ---------------------------- TIMEOUTS ---------------------------- """
        # Timeout for network requests (default: 60000 ms)
        kconfig['socket.timeout.ms'] = network_plane_spec["connection-timeout"]  # detect network failure after timeout

        # Local message timeout. This value is only enforced locally and limits the time a produced message waits for successful delivery.
        # A time of 0 is infinite. This is the maximum time librdkafka may use to deliver a message (including retries).
        # Delivery error occurs when either the retry count or the message timeout are exceeded.
        # The message timeout is automatically adjusted to transaction.timeout.ms if transactional.id is configured.
        kconfig['message.timeout.ms'] = network_plane_spec["on-failure"][
            "allow-data-loss"]  # if > 0, kafka will detect failed message after timeout and message failed to be sent will be dropped, a value of 0 will garanti that the message will not be dropped because failur because it will wait for ACK indefinitly

        """ ---------------------------- IDEMPOTENT PRODUCER ---------------------------- """

        if not network_plane_spec["on-failure"]["allow-data-duplication"]:
            kconfig['enable.idempotence'] = True
        else:
            kconfig['enable.idempotence'] = False

        """ ---------------------------- TRANSACTIONAL PRODUCER ---------------------------- """

        if network_plane_spec["type"] == "transactional":
            kconfig['transactional.id'] = self._address
            kconfig['transaction.timeout.ms'] = network_plane_spec["connection-timeout"]

        """ ---------------------------- DELIVERY REPORTS ---------------------------- """

        # Only provide delivery reports for failed messages.
        # default false
        # self._kconfig['delivery.report.only.error']=False

        """ ---------------------------- STATS COLLECTION ---------------------------- """

        if network_plane_spec["enable-stats"]:
            kconfig['statistics.interval.ms'] = 1000
            kconfig['stats_cb'] = self.__stats_callback
        else:
            kconfig['statistics.interval.ms'] = 0
            kconfig['stats_cb'] = self.__stats_callback

        """ ---------------------------- COMPRESSION ---------------------------- """
        kconfig['compression.codec'] = network_plane_spec["compression-codec"]

        """ ---------------------------- CONNECTION STRING ---------------------------- """
        connection_string = ""
        for broker in network_plane_spec["data-service"]["record-address"]:
            connection_string = connection_string + str(broker['host']) + ":" + str(broker['port']) + ","
        connection_string = connection_string[:-1]

        kconfig['bootstrap.servers'] = connection_string

        return kconfig

    def join(self):
        self._P_Live_Sync.join()

    def get_running_config(self):
        return {"producer":self._producer_config,"spec":self._network_plane_spec}

    def __stats_callback(self,stats):
        self._latest_stats=stats

    #will not be called if message.timeout.ms = 0 (kafka will wait indefinitly for message ack
    def _on_delivery_callback(self,err, msg):

        if err is not None:

            self._send_status.clear()
            logging.getLogger(self._address).error("delivery error: %s" % err)

        else:
            if not self._send_status.is_set():
                self._send_status.set()
                logging.getLogger(self._address).info("delivery resumed.")


    def metrics(self):
        stats=self._latest_stats
        return stats
    def _sync(self, __config, __burst_queue, __interruption_string, __address,__send_status,__working_status, __producer_update_task,__update_instructions):
        pass