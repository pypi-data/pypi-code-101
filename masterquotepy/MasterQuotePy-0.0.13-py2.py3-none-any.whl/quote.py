from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
import time
import logging
import json
import hashlib
import requests
from enum import Enum


# Import Solace Python  API modules from the solace package
from solace.messaging.messaging_service import MessagingService, ReconnectionListener, ReconnectionAttemptListener, ServiceInterruptionListener, RetryStrategy, ServiceEvent
from solace.messaging.resources.topic_subscription import TopicSubscription
from solace.messaging.receiver.message_receiver import MessageHandler, InboundMessage
from solace.messaging.receiver.direct_message_receiver import DirectMessageReceiver
from solace.messaging.publisher.outbound_message import OutboundMessage
from solace.messaging.publisher.request_reply_message_publisher import RequestReplyMessagePublisher
from solace.messaging.resources.topic import Topic


class Market(Enum):
    TWSE = 'TWS'
    TAIFEX = 'TWF'


class TickType(Enum):
    Transaction = "TX"
    Commissioned = "5Q"


class TickData:
    def __init__(self, market, type, raw):
        if(market == Market.TWSE.value):
            columns = raw.split("|")
            if(type == TickType.Transaction.value):
                self.format = TickType.Transaction.value
                self.code = columns[0]
                self.trail_flag = columns[4]
                self.q5_flag = columns[5]
                self.total_volume = columns[9]
                self.price = columns[10]
                self.volume = columns[11]
                self.buy = list()
                self.sell = list()
                buy_cnt = columns[12]
                sell_cnt = columns[23]
                for i in range(int(buy_cnt)):
                    self.buy.append((columns[13+i], columns[14+i]))
                for i in range(int(sell_cnt)):
                    self.sell.append((columns[24+i], columns[25+i]))
            if(type == TickType.Commissioned.value):
                self.format = TickType.Commissioned.value
                self.code = columns[0]
                self.trail_flag = columns[4]
                self.q5_flag = columns[5]
                self.total_volume = columns[9]
                self.buy = list()
                self.sell = list()
                buy_cnt = columns[12]
                sell_cnt = columns[23]
                for i in range(int(buy_cnt)):
                    self.buy.append((columns[13+i], columns[14+i]))
                for i in range(int(sell_cnt)):
                    self.sell.append((columns[24+i], columns[25+i]))
        elif(market == Market.TAIFEX.value):
            columns = raw.split("|")
            if(type == TickType.Transaction.value):
                self.format = TickType.Transaction.value
                self.code = columns[0]
                self.information_time = columns[2]
                self.trail_flag = columns[4]
                self.mathing_time = columns[5]
                self.total_volume = columns[7]
                self.matched_buy_cnt = columns[8]
                self.matched_sell_cnt = columns[9]
                txn_cnt = columns[11]
                self.match_data = list()
                for i in range(int(txn_cnt)):
                    self.match_data.append((columns[12+i], columns[13+i]))
            elif(type == TickType.Commissioned.value):
                self.format = TickType.Commissioned.value
                self.code = columns[0]
                self.information_time = columns[2]
                self.trail_flag = columns[4]
                self.buy = list()
                self.sell = list()
                for i in range(5):
                    self.buy.append((columns[5+i], columns[6+i]))
                for j in range(5):
                    self.sell.append((columns[15+i], columns[16+i]))

    def __str__(self):
        return __class__.__name__ + ":" + str(self.__dict__)

    def __add__(self, other):
        return str(self) + other

    def __radd__(self, other):
        return other + str(self)


class Snapshot:
    def __init__(self, market, raw):
        if(market == Market.TWSE):
            columns = raw.split("|")
            self.code = columns[0]
            self.name_ch = columns[1]
            # self.timestamp = columns[2]
            # self.serial_no = columns[3]
            self.ref_price = columns[4]
            self.rise_stop_price = columns[5]
            self.fall_stop_price = columns[6]
            self.industry_category = columns[7]
            self.stock_category = columns[8]
            self.stock_entries = columns[9]
            self.stock_anomaly_code = columns[10]
            self.board_code = columns[11]
            self.class_code = columns[12]
            self.non_10_face_value_indicator = columns[13]
            self.abnormal_recommendation_indicator = columns[14]
            self.abnormal_securities_indicator = columns[15]
            self.day_trading_indicator = columns[16]
            self.examp_unchg_market_margin_sale_indicator = columns[17]
            self.examp_unchg_market_securities_lending_sale_indicator = columns[18]
            self.matching_cycle_seconds = columns[19]
            self.warrant_id = columns[20]
            self.warrant_strike_price = columns[21]
            self.warrant_strike_volume_before = columns[22]
            self.warrant_cancel_volume_before = columns[23]
            self.warrant_issuing_balance = columns[24]
            self.warrant_strike_ratio = columns[25]
            self.warrant_upper_limit_price = columns[26]
            self.warrant_lower_limit_price = columns[27]
            self.warrant_maturity_date = columns[28]
            self.foreign_stock_indicator = columns[29]
            self.trading_unit = columns[30]
            self.trading_currency_code = columns[31]
            self.market_information_line = columns[32]
            self.tick_size = columns[33]
        elif(market == Market.TAIFEX):
            columns = raw.split("|")
            self.code = columns[0]
            self.ref_price = columns[4]
            self.rise_stop_price = columns[5]
            self.fall_stop_price = columns[6]
            self.product_kind = columns[7]
            self.decimal_locator = columns[8]
            self.strike_price_decimal_locator = columns[9]
            self.begin_date = columns[10]
            self.end_date = columns[11]
            self.flow_group = columns[12]
            self.delivery_date = columns[13]
            self.dynamic_banding = columns[14]
            self.contract_kind_code = columns[15]
            self.contract_name_ch = columns[16]
            self.stock_code = columns[17]
            self.contract_size = columns[18]
            self.status_code = columns[19]
            self.currency_type = columns[20]
            self.accept_quote_flag = columns[21]
            self.block_trade_flag = columns[22]
            self.expiry_type = columns[23]
            self.underlying_type = columns[24]
            self.market_close_group = columns[25]
            self.end_session = columns[26]
            self.after_hour = columns[27]

    def __str__(self):
        return __class__.__name__ + ":" + str(self.__dict__)

    def __add__(self, other):
        return str(self) + other

    def __radd__(self, other):
        return other + str(self)

    @staticmethod
    def appendHL(data, market, raw):
        if market == Market.TWSE:
            columns = raw.split("|")
            data.market = columns[0]
            data.matching_time = columns[3]
            data.price = columns[6]
            data.volume = columns[7]
            data.high = columns[8]
            data.low = columns[9]
            data.total_amount = columns[10]
            data.total_volume = columns[11]
        elif(market == Market.TAIFEX):
            columns = raw.split("|")
            data.market = columns[0]
            data.matching_time = columns[6]
            data.price = columns[9]
            data.volume = columns[10]
            data.high = columns[11]
            data.low = columns[12]
            data.total_volume = columns[14]


def decode_snapshot(data_map, market, json_data):
    json_obj = json.loads(json_data)
    base_list = json_obj["BAS"]
    for basic_raw in base_list:
        product = Snapshot(market, basic_raw)
        data_map[product.code] = product
    for hl_raw in json_obj["HL"]:
        if market == Market.TWSE:
            product = hl_raw.split("|")[2]
        if market == Market.TAIFEX:
            product = hl_raw.split("|")[3]
        Snapshot.appendHL(data_map[product], market, hl_raw)


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

    # List of subscribers. In real life, the list of subscribers can be stored more comprehensively(categorized by event type, etc.).
    _observers: List[QuoteObserver] = []

    def __init__(self, id, account, password):
        host = "http://172.18.8.42:80"
        query = {'Idno': id, 'Account': account,
                 'Password': hashlib.md5(password.encode('utf-8')).hexdigest()}
        response = requests.get(
            "http://192.168.5.135/tc4/SsoCheckSpeedyAct.jsp", params=query)
        print(response.text)
        if(not response.text.startswith('True')):
            return None
        # Broker Config
        broker_props = {
            "solace.messaging.transport.host": host,
            "solace.messaging.service.vpn-name": "quote",
            "solace.messaging.authentication.scheme.basic.username": "QuoteTC4",
            "solace.messaging.authentication.scheme.basic.password": "ml2856",
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
        for observer in self._observers:
            observer.update(self)

    def on_message(self, message: 'InboundMessage'):
        print(str(current_micro_time()))
        topic = message.get_destination_name()
        topic_cols = topic.split("/")
        market = topic_cols[1]
        encoding = 'utf-8'
        payload_str = message.get_payload_as_bytes().decode(encoding)
        self._tick = payload_str
        type = topic[-2:]
        self._tick_data = TickData(market, type, payload_str)
        self.notify()

    def get_last_data(self, market, product_list=[]):
        responses = []
        messages = [None]*len(product_list)
        if market == Market.TWSE:
            topic = "Quote_TWS_RECOVER"
            message_pattern = self.TWS_TOPIC_PATTERN
        elif market == Market.TAIFEX:
            topic = "Quote_TWF_RECOVER"
            message_pattern = self.TWF_TOPIC_PATTERN
        for i in range(len(product_list)):
            messages[i] = message_pattern.replace(
                "{{product_code}}", product_list[i])
            messages[i] = messages[i].replace("{{market}}", market.value)
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
            responses.append(payload_str)

        quote_data = dict()
        for data in responses:
            decode_snapshot(quote_data, market, data)

        return quote_data

    def subscribe(self, market, product_list=[], with_TX=True, with_5Q=False):
        topics = [None]*len(product_list)
        topic_pattern = ""
        if market == Market.TWSE:
            topic_pattern = self.TWS_TOPIC_PATTERN
        elif market == Market.TAIFEX:
            topic_pattern = self.TWF_TOPIC_PATTERN
        for i in range(len(topics)):
            topics[i] = topic_pattern.replace(
                "{{product_code}}", product_list[i])
            topics[i] = topics[i].replace("{{market}}", market.value)
        for t in topics:
            if(with_TX):
                self._message_receiver.add_subscription(
                    TopicSubscription.of(t + "/TX"))
            if(with_5Q):
                self._message_receiver.add_subscription(
                    TopicSubscription.of(t + "/5Q"))

    def unsubscribe(self, market, product_list=[], with_TX=True, with_5Q=False):
        topics = [None]*len(product_list)
        topic_pattern = ""
        if market == Market.TWSE:
            topic_pattern = self.TWS_TOPIC_PATTERN
        elif market == Market.TAIFEX:
            topic_pattern = self.TWF_TOPIC_PATTERN
        for i in range(len(topics)):
            topics[i] = topic_pattern.replace(
                "{{product_code}}", product_list[i])
            topics[i] = topics[i].replace("{{market}}", market.value)
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
            if(topicArray[1] == Market.TAIFEX.value):
                subscription = (Market.TAIFEX.name, topicArray[3])
            elif(topicArray[1] == Market.TWSE.value):
                subscription = (Market.TWSE.name, topicArray[4])

            if(item[1] == True):
                subscriptions.append(subscription)

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


def current_micro_time():
    return round(time.time() * 1000000)


class ConcreteObserver(QuoteObserver):
    def update(self, quote: Quote) -> None:
        print(str(current_micro_time()) +
              " ConcreteObserver: received msg:" + quote._tick_data)


if __name__ == "__main__":
    # logging.basicConfig(filename='Quote.log', level=logging.DEBUG)
    mq = MarketQuote("F121486499", "9700247", "000000")
    print(f"connected?{mq._is_connected}")
    if(mq._is_connected):
        # mq.subscribe(Market.TWSE, ["2330"])
        mq.subscribe(Market.TAIFEX, ["TXFK1"])
        observer = ConcreteObserver()
        mq.attach(observer)
        # print(f"topic dict:{mq._message_receiver._topic_dict}")
        # print(type(mq._message_receiver._topic_dict))

        # print(f"topic dict:{mq._message_receiver._topic_dict}")
        # print(type(mq._message_receiver._topic_dict))

        # list_subscription = mq.list_subscriptions()
        # print(list_subscription)

        # twf_data = mq.get_last_data(Market.TAIFEX, ["MXFK1", "TXFK1"])
        # for key in twf_data:
        #     print(twf_data[key])
        # quote_data = mq.get_last_data(model.Market.TWSE, ["2330", "2331"])
        # for key in quote_data:
        #     print(quote_data[key])
        # print(quote_data)

    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        print('\nDisconnecting Messaging Service')
    finally:
        print('\nTerminating receiver')
        mq.terminate()
        print('\nDisconnecting Messaging Service')
        mq.disconnect()
