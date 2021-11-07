"""
Module for bulbs of different type.
"""
import logging
import time
from collections import deque

import yeelight
from PIL import Image, ImageDraw
from sqlalchemy import Column, String, DateTime
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from yeelight import Bulb as BulbYee, BulbException

from .color import Color
from .const import Settings
from .exception import BulbConnectionLostException
from .generator import ColorGenerator

# Declaring of local sqlite to storage list of used bulbs.
engine = create_engine('sqlite:///local.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class Bulb(Base):
    """
    Base class of bulb.
    """
    __tablename__ = 'bulb'

    id = Column(String, primary_key=True)
    model = Column(String)
    name = Column(String)
    last_ip = Column(String)
    last_usage = Column(DateTime)
    bulb_obj_ = None
    colors_queue = deque()
    default_effect = "smooth"

    @property
    def queue_size(self):
        return Settings.QUEUE_SIZE_CONST

    @property
    def bulb_obj(self):
        if self.bulb_obj_ is None:
            self.init_obj()
        return self.bulb_obj_

    def init_obj(self, ip: str = None, effect: str = None) -> BulbYee:
        """
        :param ip: IP address of bulb in local network.
        :param effect: Effect of changing color. Can be "smooth" or "sudden".
        :return:
        """
        ip = ip if ip else self.last_ip
        effect = effect if effect else self.default_effect

        for i in range(5):
            try:
                logging.info(f"Connecting: {ip}")
                self.bulb_obj_ = BulbYee(ip, effect=effect, auto_on=True)
                self.bulb_obj_.set_power_mode(yeelight.PowerMode.RGB)
                self.bulb_obj_.start_music()
                logging.info(f"Connected: {ip}")
                return self.bulb_obj_
            except (BulbException, ConnectionResetError, TypeError):
                time.sleep(5)

        raise BulbConnectionLostException(f"No connection established with {ip}")

    def show_queue(self) -> None:
        """
        Draw the state of colors queue. Queue is used to determine the current color (as avg of all in queue).
        Function for debugging purposes.
        :return: None, shows image with Image.show()
        """
        im = Image.new('RGB', (self.queue_size * 10, 50), (224, 224, 224))
        draw = ImageDraw.Draw(im)
        for i, color in enumerate(self.colors_queue):
            hor_shift = 10 * i
            box = (hor_shift, 50, hor_shift + 10, 0)
            fill = color.tuple()
            draw.rectangle(box, fill=fill)
        im.show()

    def change_color(self, color: Color):
        """
        The interface for smooth changing the color of the light bulb.
        Saturates the transmitted color, adds to the color queue.
        :param color: Object Color.
        :return: None
        """
        color = color.saturated()
        self.colors_queue.append(color)
        if len(self.colors_queue) > self.queue_size:
            self.colors_queue.popleft()
        if Settings.SHOW_COLORS_QUEUE:
            self.show_queue()
        color = ColorGenerator.extract_avg_color(list(self.colors_queue))
        self.bulb_obj.set_rgb(*color.tuple())

    def __repr__(self):
        return f"<Bulb(id='{self.id}', name='{self.name}', last_ip='{self.last_ip}, last_usage='{self.last_usage}')>"

    def is_valid(self):
        """
        Checks if bulb last_ip and last_usage are not None.
        :return:
        """
        return True if self.last_ip and self.last_usage and self.id else False


Base.metadata.create_all(engine)
