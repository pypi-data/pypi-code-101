import logging
from os import environ
import pika


def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    formatter = logging.Formatter(
            '%(asctime)s [%(name)s] %(levelname)s: %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger


def connect():
    return pika.BlockingConnection(
            pika.ConnectionParameters(
                host=environ.get('RMQ_HOST', 'localhost'),
                credentials=pika.PlainCredentials(
                    environ.get('RMQ_USER', 'verkefni'),
                    environ.get('RMQ_PASSWORD', 'verkefni'))))


def declare_work_queue(chan, queue_name, topics):
    chan.exchange_declare(
            exchange='work', exchange_type='topic', durable=True)
    work_q = chan.queue_declare(queue_name, durable=True)
    for topic in topics:
        chan.queue_bind(exchange='work',
                        queue=work_q.method.queue,
                        routing_key=topic)
    return work_q
