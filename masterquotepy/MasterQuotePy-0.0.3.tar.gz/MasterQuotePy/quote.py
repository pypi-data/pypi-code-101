from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
import time
import logging
import model
import json
import requests


# Import Solace Python  API modules from the solace package
from solace.messaging.messaging_service import MessagingService, ReconnectionListener, ReconnectionAttemptListener, ServiceInterruptionListener, RetryStrategy, ServiceEvent
from solace.messaging.resources.topic_subscription import TopicSubscription
from solace.messaging.receiver.message_receiver import MessageHandler, InboundMessage
from solace.messaging.receiver.direct_message_receiver import DirectMessageReceiver
from solace.messaging.publisher.outbound_message import OutboundMessage
from solace.messaging.publisher.request_reply_message_publisher import RequestReplyMessagePublisher
from solace.messaging.resources.topic import Topic

class Quote(ABC):
    # The Quote interface declares a set of methods for managing observers.
    @abstractmethod
    def attach(self, observer: QuoteObserver) -> None:
        # Attach an observer to the subject.
        pass

    @abstractmethod
    def detach(self, observer: QuoteObserver) -> None:
        # Detach an observer from the subject.
        pass

    @abstractmethod
    def notify(self) -> None:
        # Notify all observers about an event.
        pass


class QuoteObserver(ABC):
    """
    The Observer interface declares the update method, used by subjects.
    """

    @abstractmethod
    def update(self, quote: Quote) -> None:
        """
        Receive update from subject.
        """
        pass


class MarketQuote(Quote, MessageHandler):
    # The Subject owns some important state and notifies observers when the statechanges.
    _is_connected: bool = False
    _state: int = None
    _tick: str = None
    _snapshot: dict()
    _reply_timeout = 10000
    _products: List[str] = []
    _message_receiver: DirectMessageReceiver
    _message_service: MessagingService
    _message_requester: RequestReplyMessagePublisher

    TWS_TOPIC_PATTERN = "Quote/{{market}}/*/*/{{product_code}}"
    TWF_TOPIC_PATTERN = "Quote/{{market}}/*/{{product_code}}"

    # For the sake of simplicity, the Subject's state, essential to all subscribers, is stored in this variable.
    _observers: List[QuoteObserver] = []
    # List of subscribers. In real life, the list of subscribers can be stored more comprehensively(categorized by event type, etc.).

    def __init__(self, ip, username, password):
        host = "http://" + ip + ":80"
        # host = ip + ":55555"
        # Broker Config
        broker_props = {
            "solace.messaging.transport.host": host,
            "solace.messaging.service.vpn-name": "quote",
            "solace.messaging.authentication.scheme.basic.username": username,
            "solace.messaging.authentication.scheme.basic.password": password,
        }
        self._message_service = MessagingService.builder().from_properties(broker_props)\
            .with_reconnection_retry_strategy(RetryStrategy.parametrized_retry(20, 3000))\
            .build()
        self._message_service.connect()
        self._message_receiver = self._message_service.create_direct_message_receiver_builder().build()
        self._message_receiver.start()
        self._message_receiver.receive_async(self)
        self._message_requester = self._message_service.request_reply() \
            .create_request_reply_message_publisher_builder().build().start()
        self._is_connected = self._message_service.is_connected

    def receive_async(self):
        self._message_receiver.receive_async(self)

    def attach(self, observer: QuoteObserver) -> None:
        print("Quote: Attached an QuoteObserver.")
        self._observers.append(observer)

    def detach(self, observer: QuoteObserver) -> None:
        self._observers.remove(observer)

    # The subscription management methods.
    def notify(self) -> None:
        # Trigger an update in each subscriber.
        print("Quote: Notifying observers...")
        for observer in self._observers:
            observer.update(self)

    def on_message(self, message: 'InboundMessage'):
        topic = message.get_destination_name()
        topic_cols = topic.split("/")
        market = topic_cols[1]
        encoding = 'utf-8'
        payload_str = message.get_payload_as_bytes().decode(encoding)
        self._tick = payload_str
        type = topic[-2:]
        self._tick_data = model.TickData(market, type, payload_str)
        self.notify()

    def get_last_data(self, market, product_list=[]):
        responses = []
        messages = [None]*len(product_list)
        if market == "TWS":
            topic = "Quote_TWS_RECOVER"
            message_pattern = self.TWS_TOPIC_PATTERN
        elif market == "TWF":
            topic = "Quote_TWF_RECOVER"
            message_pattern = self.TWF_TOPIC_PATTERN
        for i in range(len(product_list)):
            messages[i] = message_pattern.replace(
                "{{product_code}}", product_list[i])
            messages[i] = messages[i].replace("{{market}}", market)
        for m in messages:
            payloadByte = bytearray(f'{m}/RECOVER', 'utf-8')
            message: OutboundMessage = self._message_service.message_builder().build(
                payload=payloadByte)
            reply = self._message_requester.publish_await_response(request_message=message,
                                                                   request_destination=Topic.of(
                                                                       topic),
                                                                   reply_timeout=self._reply_timeout)
            encoding = 'utf-8'
            payload_str = reply.get_payload_as_bytes().decode(encoding)
            print(f"reply: {payload_str}")
            responses.append(payload_str)
  
        quote_data = dict()
        for data in responses:
            model.decode_snapshot(quote_data, market, data)
    
        return quote_data

    def add_product(self, market, product_list=[], with_TX=True, with_5Q=False):
        topics = [None]*len(product_list)
        topic_pattern = ""
        if market == "TWS":
            topic_pattern = self.TWS_TOPIC_PATTERN
        elif market == "TWF":
            topic_pattern = self.TWF_TOPIC_PATTERN
        for i in range(len(topics)):
            topics[i] = topic_pattern.replace(
                "{{product_code}}", product_list[i])
            topics[i] = topics[i].replace("{{market}}", market)
        for t in topics:
            if(with_TX):
                self._message_receiver.add_subscription(
                    TopicSubscription.of(t + "/TX"))
            if(with_5Q):
                self._message_receiver.add_subscription(
                    TopicSubscription.of(t + "/5Q"))

    def remove_product(self, market, product_list=[], with_TX=True, with_5Q=False):
        topics = [None]*len(product_list)
        topic_pattern = ""
        if market == "TWS":
            topic_pattern = self.TWS_TOPIC_PATTERN
        elif market == "TWF":
            topic_pattern = self.TWF_TOPIC_PATTERN
        for i in range(len(topics)):
            topics[i] = topic_pattern.replace(
                "{{product_code}}", product_list[i])
            topics[i] = topics[i].replace("{{market}}", market)
        for t in topics:
            if(with_TX):
                self._message_receiver.remove_subscription(
                    TopicSubscription.of(t + "/TX"))
            if(with_5Q):
                self._message_receiver.remove_subscription(
                    TopicSubscription.of(t + "/5Q"))

    def list_subscriptions(self) -> list:
        subscriptions = []
        for item in self._message_receiver._topic_dict.items():
            topicArray = item[0].split("/")
            if(topicArray[1] == "TWF"):
                topic = ("TWF", topicArray[3])
            elif(topicArray[1] == "TWS"):
                topic = ("TWS", topicArray[4])

            if(item[1] == True):
                subscriptions.append(topic)

        return subscriptions

    # def send_request(self, topic, payload):

    def terminate(self):
        self._message_receiver.terminate()

    def disconnect(self):
        self._message_service.disconnect()


class QuoteObserver(ABC):
    @ abstractmethod
    def update(self, quote: Quote) -> None:
        # Receive update from subject.
        pass


class ConcreteObserver(QuoteObserver):
    def update(self, quote: Quote) -> None:
        print("ConcreteObserver: received msg:" + quote._tick_data)

if __name__ == "__main__":
    logging.basicConfig(filename='Quote.log', level=logging.DEBUG)
    mq = MarketQuote("203.75.95.139", "QuoteTC4", "ml2856")
    logging.info(f"connected?{mq._is_connected}")
    # mq.add_product("TWS", ["2330"], True, True)
    mq.add_product("TWF", ["MXFK1"], True, True)
    observer = ConcreteObserver()
    mq.attach(observer)
    # print(f"topic dict:{mq._message_receiver._topic_dict}")
    # print(type(mq._message_receiver._topic_dict))

    # mq.remove_product("TWF", ["MXFK1"], False, True)
    # print(f"topic dict:{mq._message_receiver._topic_dict}")
    # print(type(mq._message_receiver._topic_dict))

    # list_subscription = mq.list_subscriptions()
    # logging.info(list_subscription)

    # twf_data = mq.get_last_data('TWF', ["MXFK1", "TXFK1"])
    # quote_data = mq.get_last_data('TWS', ["2330", "2331"])
    # print(quote_data)
    # query = {'q': 'requests+language:java'}
    # response = requests.get("https://api.github.com/search/repositories", params=query)
    # print(response.text)
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print('\nDisconnecting Messaging Service')
    finally:
        print('\nTerminating receiver')
        mq.terminate()
        print('\nDisconnecting Messaging Service')
        mq.disconnect()
