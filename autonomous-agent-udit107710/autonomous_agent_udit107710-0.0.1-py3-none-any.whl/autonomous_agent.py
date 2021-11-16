"""
This file implements the actual agent which reacts to messages from
the environment(queue) and also proactivly generates messages to
the environment(queue)
"""

from concurrent.futures import ThreadPoolExecutor
from typing import Any, Dict, List
import time
import logging
import uuid
import random
from queue import Queue
from .behaviour import Behaviour
from .event import Event

FORMAT = '%(asctime)s [%(levelname)s] %(threadName)-8s %(name)s %(message)s'

logging.basicConfig(
    format=FORMAT,
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S'
)
LOGGER = logging.getLogger(__name__)


class Agent:

    def __init__(self, inBox: Queue, outBox: Queue):
        self.inBox: Queue = inBox
        self.outBox: Queue = outBox
        self.typeToHandler: Dict[str, Any] = {}
        self.behaviours: List[Behaviour] = []

    def register_reactive_handler(self, message_type, message_handler):
        self.typeToHandler[message_type]: Dict[str, Any] = message_handler
        LOGGER.info(f"Added a new handler for {message_type}")

    def consume_messsage(self):
        while True:
            t1 = time.time()
            event = self.inBox.get()  # This gets the last message from the list/queue
            fn = self.typeToHandler.get(event.type_)
            if not fn:
                continue
            fn(event.message)
            t2 = time.time()
            LOGGER.info(f"Consumed Event {event} in {t2-t1:5.6f}s")
            if self.inBox.empty(): # Just to reduce some load of polling. Not necessary
                time.sleep(2)

    def start_reactive_consumption(self):
        future = ThreadPoolExecutor(max_workers=1, thread_name_prefix='consumer' + str(self.__hash__())).submit(
            self.consume_messsage)
        LOGGER.info("Started new thread for reactive consumtion from inBox")
    
    def register_proactive_behaviour(self, proactive_behaviour: Behaviour):
        self.behaviours.append(proactive_behaviour)
        LOGGER.info(f"Added {proactive_behaviour} to known behaviours")

    def behaviour_polling(self):
        while True:
            if self.behaviours:
                for behaviour in self.behaviours:
                    LOGGER.info(f"Evaluating behaviour {behaviour}")
                    if eval(behaviour.condition,  behaviour.globals_, behaviour.locals_):
                        LOGGER.info(f"Acted on behaviour {behaviour}")
                        self.outBox.put({
                            "type": behaviour.message_type,
                            "content": behaviour.message_text,
                            "id": str(uuid.uuid4())
                        }, False)
                time.sleep(1)  # After going through the complete behaviours, stop for a sec

    def start_proactive_production(self):
        future = ThreadPoolExecutor(max_workers=1, thread_name_prefix='producer' + str(self.__hash__())).submit(self.behaviour_polling)
        LOGGER.info("Started new thread for reactive production to outBox")
