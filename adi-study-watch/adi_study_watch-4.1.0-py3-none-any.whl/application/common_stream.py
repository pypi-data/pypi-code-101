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

import logging
from datetime import datetime

from .common_application import CommonApplication
from ..core.enums.common_enums import CommonCommand, Stream
from ..core.packets.common_packets import StreamPacket, StreamStatusPacket

logger = logging.getLogger(__name__)


class CommonStream(CommonApplication):
    """
    A Common Stream class for streaming data from sensors.
    """

    def __init__(self, destination, stream, packet_manager):
        """
        Initialize the common stream packet variable.

        :param destination: Address of the application.
        :param stream: Address of stream.
        :param packet_manager: PacketManager Object.
        """
        super().__init__(destination, packet_manager)
        self._args = {}
        self._stream = stream
        self._csv_logger = {}
        self._last_timestamp = {}
        self._callback_function = {}

    def set_callback(self, callback_function, args=()):
        """
        Sets the callback for the stream data.

        :param args: optional arguments that will be passed with the callback.
        :param callback_function: callback function for stream adxl data.
        :return: None

        .. code-block:: python3
            :emphasize-lines: 4,12

            from adi_study_watch import SDK

            # make sure optional arguments have default value to prevent them causing Exceptions.
            def callback(data, optional1=None, optional2=None):
                print(data)

            sdk = SDK("COM4")
            application = sdk.get_adxl_application()
            # these optional arguments can be used to pass file, matplotlib or other objects to manipulate data.
            optional_arg1 = "1"
            optional_arg2 = "2"
            application.set_callback(callback, args=(optional_arg1, optional_arg2))
        """
        self._args[self._stream] = args
        self._callback_function[self._stream] = callback_function

    def _callback_data(self, packet, packet_id, callback_function=None, args=None):
        """
        Process and returns the data back to user's callback function.
        """
        pass

    def _update_stream_data(self, result):
        """
        Add or modify stream data values.
        """
        pass

    def _callback_data_helper(self, packet, response_packet, stream=None):
        """
        Process and returns the data back to user's callback function.
        """
        stream = stream if stream else self._stream
        args = self._args.get(stream, ())
        callback_function = self._callback_function.get(stream, None)
        response_packet.decode_packet(packet)
        last_timestamp = self._last_timestamp.get(stream)
        result = response_packet.get_dict(last_timestamp)
        self._update_stream_data(result)
        csv_logger = self._csv_logger.get(stream, None)
        if csv_logger:
            csv_logger.add_row(result, last_timestamp[0])
        try:
            if callback_function:
                callback_function(result, *args)
        except Exception as e:
            logger.error(f"Can't send packet back to user callback function, reason :: {e}", exc_info=True)

        if not csv_logger and not callback_function:
            logger.warning(f"No callback function provided for {result['header']['source']}")

    def get_sensor_status(self):
        """
        Returns packet with number of subscribers and number of sensor start request registered.

        :return: A response packet as dictionary.
        :rtype: Dict

        .. code-block:: python3
            :emphasize-lines: 5

            from adi_study_watch import SDK

            sdk = SDK("COM4")
            application = sdk.get_adxl_application()
            x = application.get_sensor_status()
            print(x["payload"]["num_subscribers"], x["payload"]["num_start_registered"])
            # 0 0

        """
        request_packet = StreamStatusPacket(self._destination, CommonCommand.GET_SENSOR_STATUS_REQ)
        request_packet.set_payload("stream_address", self._destination)
        response_packet = StreamStatusPacket(self._destination, CommonCommand.GET_SENSOR_STATUS_RES)
        return self._send_packet(request_packet, response_packet)

    def start_and_subscribe_stream(self, stream=None):
        """
        Starts sensor and also subscribe to the stream.

        :return: A response packet as dictionary.
        :rtype: Tuple[Dict, Dict]

        .. code-block:: python3
            :emphasize-lines: 5

            from adi_study_watch import SDK

            sdk = SDK("COM4")
            application = sdk.get_adxl_application()
            start_sensor, subs_stream = application.start_and_subscribe_stream()
            print(start_sensor["payload"]["status"], subs_stream["payload"]["status"])
            # CommonStatus.STREAM_STARTED CommonStatus.SUBSCRIBER_ADDED
        """
        status2 = self.subscribe_stream(stream=stream)
        status1 = self.start_sensor()
        return status1, status2

    def start_sensor(self):
        """
        Starts sensor.

        :return: A response packet as dictionary.
        :rtype: Dict

        .. code-block:: python3
            :emphasize-lines: 5

            from adi_study_watch import SDK

            sdk = SDK("COM4")
            application = sdk.get_adxl_application()
            start_sensor = application.start_sensor()
            print(start_sensor["payload"]["status"])
            # CommonStatus.STREAM_STARTED
        """
        request_packet = StreamPacket(self._destination, CommonCommand.START_SENSOR_REQ)
        response_packet = StreamPacket(self._destination, CommonCommand.START_SENSOR_RES)
        return self._send_packet(request_packet, response_packet)

    def stop_and_unsubscribe_stream(self, stream=None):
        """
        Stops sensor and also Unsubscribe the stream.

        :return: A response packet as dictionary.
        :rtype: Tuple[Dict, Dict]

        .. code-block:: python3
            :emphasize-lines: 5

            from adi_study_watch import SDK

            sdk = SDK("COM4")
            application = sdk.get_adxl_application()
            stop_sensor, unsubscribe_stream = application.stop_and_unsubscribe_stream()
            print(stop_sensor["payload"]["status"], unsubscribe_stream["payload"]["status"])
            # CommonStatus.STREAM_STOPPED CommonStatus.SUBSCRIBER_REMOVED
        """
        status1 = self.stop_sensor()
        status2 = self.unsubscribe_stream(stream=stream)
        return status1, status2

    def stop_sensor(self):
        """
        Stops sensor.

        :return: A response packet as dictionary.
        :rtype: Dict

        .. code-block:: python3
            :emphasize-lines: 5

            from adi_study_watch import SDK

            sdk = SDK("COM4")
            application = sdk.get_adxl_application()
            stop_sensor = application.stop_sensor()
            print(stop_sensor["payload"]["status"])
            # CommonStatus.STREAM_STOPPED
        """
        request_packet = StreamPacket(self._destination, CommonCommand.STOP_SENSOR_REQ)
        response_packet = StreamPacket(self._destination, CommonCommand.STOP_SENSOR_RES)
        return self._send_packet(request_packet, response_packet)

    def subscribe_stream(self, stream=None):
        """
        Subscribe to the stream.

        :return: A response packet as dictionary.
        :rtype: Dict

        .. code-block:: python3
            :emphasize-lines: 5

            from adi_study_watch import SDK

            sdk = SDK("COM4")
            application = sdk.get_adxl_application()
            subs_stream = application.subscribe_stream()
            print(subs_stream["payload"]["status"])
            # CommonStatus.SUBSCRIBER_ADDED
        """
        stream = stream if stream else self._stream
        request_packet = StreamPacket(self._destination, CommonCommand.SUBSCRIBE_STREAM_REQ)
        request_packet.set_payload("stream_address", stream)
        self._subscribe_stream_data(stream=stream)
        response_packet = StreamPacket(self._destination, CommonCommand.SUBSCRIBE_STREAM_RES)
        self._update_timestamp(datetime.now(), stream=stream)
        return self._send_packet(request_packet, response_packet)

    def _update_timestamp(self, date_time, stream=None, generate_ts=False):
        stream = stream if stream else self._stream
        if generate_ts:
            ts = (32000.0 * ((date_time.hour * 3600) + (date_time.minute * 60) + date_time.second))
        else:
            ts = -1
        if stream == Stream.SYNC_PPG:
            self._last_timestamp[stream] = [date_time.timestamp(), ts, date_time.timestamp(), ts]
        else:
            self._last_timestamp[stream] = [date_time.timestamp(), ts]

    def unsubscribe_stream(self, stream=None):
        """
        Unsubscribe the stream.

        :return: A response packet as dictionary.
        :rtype: Dict

        .. code-block:: python3
            :emphasize-lines: 5

            from adi_study_watch import SDK

            sdk = SDK("COM4")
            application = sdk.get_adxl_application()
            unsubscribe_stream = application.unsubscribe_stream()
            print(unsubscribe_stream["payload"]["status"])
            # CommonStatus.SUBSCRIBER_REMOVED
        """
        stream = stream if stream else self._stream
        request_packet = StreamPacket(self._destination, CommonCommand.UNSUBSCRIBE_STREAM_REQ)
        request_packet.set_payload("stream_address", stream)
        response_packet = StreamPacket(self._destination, CommonCommand.UNSUBSCRIBE_STREAM_RES)
        response_packet = self._send_packet(request_packet, response_packet)
        self._unsubscribe_stream_data(stream=stream)
        return response_packet

    def _subscribe_stream_data(self, stream=None, callback_function=None):
        stream = stream if stream else self._stream
        callback_function = callback_function if callback_function else self._callback_data
        data_packet_id = self._get_packet_id(CommonCommand.STREAM_DATA, stream)
        self._packet_manager.subscribe(data_packet_id, callback_function)

    def _unsubscribe_stream_data(self, stream=None, callback_function=None):
        stream = stream if stream else self._stream
        callback_function = callback_function if callback_function else self._callback_data
        data_packet_id = self._get_packet_id(CommonCommand.STREAM_DATA, stream)
        self._packet_manager.unsubscribe(data_packet_id, callback_function)
