from enum import Enum


class Sink(Enum):
    ZMQSINK = "zmq"
    PRINT = "print"
    KAFKA = "kafka"
    FILESINK = "file"
    MQTT = "mqtt"
