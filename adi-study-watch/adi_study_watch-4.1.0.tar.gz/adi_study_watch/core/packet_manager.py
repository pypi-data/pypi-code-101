# ******************************************************************************
# Copyright (c) 2019 Analog Devices, Inc.  All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# - Redistributions of source code must retain the above copyright notice, this
#  list of conditions and the following disclaimer.
# - Redistributions in binary form must reproduce the above copyright notice,
#  this list of conditions and the following disclaimer in the documentation
#  and/or other materials provided with the distribution.
# - Modified versions of the software must be conspicuously marked as such.
# - This software is licensed solely and exclusively for use with
#  processors/products manufactured by or for Analog Devices, Inc.
# - This software may not be combined or merged with other code in any manner
#  that would cause the software to become subject to terms and conditions
#  which differ from those listed here.
# - Neither the name of Analog Devices, Inc. nor the names of its contributors
#  may be used to endorse or promote products derived from this software
#  without specific prior written permission.
# - The use of this software may or may not infringe the patent rights of one
#  or more patent holders.  This license does not release you from the
#  requirement that you obtain separate licenses from these patent holders to
#  use this software.
#
# THIS SOFTWARE IS PROVIDED BY ANALOG DEVICES, INC. AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
# NONINFRINGEMENT, TITLE, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL ANALOG DEVICES, INC. OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, PUNITIVE OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, DAMAGES ARISING OUT OF
# CLAIMS OF INTELLECTUAL PROPERTY RIGHTS INFRINGEMENT; PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ******************************************************************************

import os
import logging
import threading
from queue import Queue

from tqdm import tqdm

from . import utils
from .enums.common_enums import Application, Stream
from .enums.low_touch_enum import CommandType

logger = logging.getLogger(__name__)


class PacketManager:
    """

    PacketManager

    """

    def __init__(self, serial_object, filename=None):
        """
        Initialization of packet Manager

        :param serial_object: Serial port object
        :type serial_object: Serial
        """
        self.queue = Queue()
        self.filename = filename
        self.command_type = None
        self.subscribe_source = {}
        self.lock = threading.Lock()
        self.command_logging = None
        self.log_command_packet = None
        self.source = Application.APP_USB
        self.serial_object = serial_object
        self._kill_threads = threading.Event()
        self.receive_thread = threading.Thread(target=self.receive_packet, name=f"receive_thread")

    def set_usb_source(self):
        self.source = Application.APP_USB

    def set_ble_source(self):
        self.source = Application.APP_BLE

    def enable_command_logging(self, command_type):
        self.command_logging = True
        self.command_type = command_type

    def disable_command_logging(self, command_type):
        self.command_logging = False
        self.command_type = command_type

    def subscribe_command_logger(self, log_command):
        self.log_command_packet = log_command

    def unsubscribe_command_logger(self):
        self.command_type = None
        self.command_logging = None
        self.log_command_packet = None

    def process_queue(self):
        """
        Reads the packet from queue and send to relevant callback function.
        """
        while True:
            try:
                pkt = self.queue.get()
                if self._kill_threads.isSet():
                    break
                pkt = list(pkt)
                logger.info(f"RX :: {':'.join(utils.convert_int_array_to_hex(pkt))}")
                self.send_packet_to_callback(pkt)
            except Exception as e:
                logger.critical(f"Process_queue thread failed : {e}.", exc_info=True)

    def send_packet_to_callback(self, pkt):
        """
        Sends Packet to callback
        """
        try:
            packet_id = pkt[0] + (pkt[1] << 8) + (pkt[8] << 16)
            callbacks = self.subscribe_source.get(packet_id, [])
            for callback in callbacks:
                callback(pkt, packet_id)
            if not len(callbacks):
                logger.warning(f"Received an unexpected packet {pkt} with packet ID {packet_id}")
        except Exception as e:
            logger.critical(f"RX {':'.join(utils.convert_int_array_to_hex(pkt))} callback error : {e}.", exc_info=True)

    def receive_packet(self):
        """
        Reads packet from serial port and store it in queue.
        """
        while True:
            try:
                if self._kill_threads.isSet():
                    break
                pkt = self.serial_object.read(8)
                if len(pkt):
                    length = (pkt[4] << 8) + pkt[5]
                    pkt += self.serial_object.read(length - 8)
                    self.queue.put(pkt)
            except Exception as e:
                logger.critical(f"Receive_packet thread failed : {e}.", exc_info=True)
                break

    # noinspection PyBroadException
    @staticmethod
    def _check_stream(packet):
        try:
            source = Stream(list(packet))
            if source == Stream.NULL:
                return False
            return True
        except:
            return False

    # noinspection PyBroadException
    @staticmethod
    def _check_application(packet):
        try:
            source = Application(list(packet))
            if source == Application.NULL:
                return False
            return True
        except:
            return False

    # noinspection PyBroadException
    def find_source(self, packet, file):
        logger.warning("File corruption detected. Trying to recover data.")
        packet = list(packet)
        for i in range(len(packet) - 1):
            source = packet[i:i + 1]
            if self._check_stream(source) or self._check_application(source):
                result_packet = packet[i:]
                to_read = 8 - len(result_packet)
                return result_packet + file.read(to_read)

        first_val = file.read(1)
        while True:
            try:
                second_val = file.read(1)
                source = list(first_val) + list(second_val)
                if self._check_stream(source) or self._check_application(source):
                    return source + list(file.read(6))
                first_val = second_val
            except:
                raise Exception("Can't recover corrupted file.")

    def process_file(self):
        """
        Reads packet from file and store it in file queue.
        """
        file_size = os.path.getsize(self.filename)
        progress_bar = tqdm(total=file_size)
        progress_bar.set_description("Reading file")
        file = open(self.filename, 'rb')
        while True:
            try:
                pkt = file.read(8)
                if len(pkt):
                    # recovery mode
                    source = pkt[0:2]
                    if not self._check_stream(source) and not self._check_application(source):
                        progress_bar.set_description("Recovery Mode")
                        pkt = self.find_source(pkt, file)
                        progress_bar.set_description("Reading file")
                    length = (int(pkt[4]) << 8) + int(pkt[5])
                    if length < 8:
                        continue
                    progress_bar.update(length)
                    pkt += file.read(length - 8)
                    pkt = list(pkt)
                    self.send_packet_to_callback(pkt)
                else:
                    logger.debug(f"ELSE case in process_file")
                    break
            except Exception as e:
                logger.critical(f"process_file method failed : {e}.", exc_info=True)
                break

        file.close()
        progress_bar.close()

    def send_packet(self, packet):
        """
        Receives packet from sdk and send it to the serial to port for device to process.
        """
        packet.set_header("source", self.source)
        logger.debug(f"Packet ready : {packet}")
        packet = packet.to_list()
        # if not convert_log_to_csv
        if not self.filename:
            self.serial_object.write(packet)
        # logging for LT enable_command_logging
        if self.command_logging is True and self.command_type == CommandType.START:
            self.log_command_packet.add_start_command(packet)
        elif self.command_logging is True and self.command_type == CommandType.STOP:
            self.log_command_packet.add_stop_command(packet)
        logger.info(f"TX :: {':'.join(utils.convert_int_array_to_hex(packet))}")

    def start_receive_and_process_threads(self):
        """
        start process and receive thread.
        """
        self.receive_thread.setDaemon(True)
        self.receive_thread.start()
        thread = threading.Thread(target=self.process_queue)
        thread.setDaemon(True)
        thread.name = f"process_thread"
        thread.start()

    def subscribe(self, packet_id, callback):
        """
        Subscribe packet id to the callback.
        """
        callbacks = self.subscribe_source.get(packet_id, [])
        callbacks.append(callback)
        self.subscribe_source[packet_id] = callbacks

    def unsubscribe(self, packet_id, application_callback):
        """
        Unsubscribe packet id and removes the callback.
        """
        callbacks = self.subscribe_source.get(packet_id, [])
        for i, callback in enumerate(callbacks):
            if callback == application_callback:
                del callbacks[i]
                break
        self.subscribe_source[packet_id] = callbacks

    def close(self):
        """Closes serial port"""
        self._kill_threads.set()
        # to free up queue.get() lock in process_queue add -1 to queue
        self.queue.put(-1)
        self.serial_object.close()
