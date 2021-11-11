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
import math
import logging
from typing import List, Dict, Callable

from tqdm import tqdm

from .common_application import CommonApplication
from ..core.packets.common_packets import StreamPacket
from ..core.packets.command_packet import CommandPacket
from ..core.enums.common_enums import Application, Stream
from ..core.enums.fs_enums import FSCommand, FSStatus, FSLogging
from ..core.packets.fs_packets import FSStreamStatusPacket, FileCountPacket, ConfigFilePacket, LSRequestPacket, \
    LSResponsePacket, StreamFileRequestPacket, StreamFileResponsePacket, KeyValuePairResponsePacket
from ..core.packets.fs_packets import StreamFileChunkPacket, KeyValuePairPacket, LoggingPacket, VolumeInfoPacket

logger = logging.getLogger(__name__)


class FSApplication(CommonApplication):
    """
    FS Application class.

    .. code-block:: python3
        :emphasize-lines: 4

        from adi_study_watch import SDK

        sdk = SDK("COM4")
        application = sdk.get_fs_application()

    """

    STREAM_EDA = Stream.EDA
    STREAM_BIA = Stream.BIA
    STREAM_ECG = Stream.ECG
    STREAM_PPG = Stream.PPG
    STREAM_SQI = Stream.SQI
    STREAM_ADXL = Stream.ADXL
    STREAM_ADPD1 = Stream.ADPD1
    STREAM_ADPD2 = Stream.ADPD2
    STREAM_ADPD3 = Stream.ADPD3
    STREAM_ADPD4 = Stream.ADPD4
    STREAM_ADPD5 = Stream.ADPD5
    STREAM_ADPD6 = Stream.ADPD6
    STREAM_ADPD7 = Stream.ADPD7
    STREAM_ADPD8 = Stream.ADPD8
    STREAM_ADPD9 = Stream.ADPD9
    STREAM_ADPD10 = Stream.ADPD10
    STREAM_ADPD11 = Stream.ADPD11
    STREAM_ADPD12 = Stream.ADPD12
    STREAM_PEDOMETER = Stream.PEDOMETER
    STREAM_TEMPERATURE = Stream.TEMPERATURE
    STREAM_STATIC_AGC = Stream.STATIC_AGC_STREAM
    STREAM_DYNAMIC_AGC = Stream.DYNAMIC_AGC_STREAM
    STREAM_HRV = Stream.HRV
    STREAM_BATTERY = Stream.BATTERY

    def __init__(self, packet_manager):
        super().__init__(Application.FS, packet_manager)
        self._stream = Stream.FS
        self.stream_progress = 0
        self.total_size = 0
        self._file_stream_callback = None

    def _stream_helper(self, stream: Stream) -> Stream:
        """
        Confirms stream is from list of Enums.
        """
        if stream in self.get_supported_streams():
            return stream
        else:
            logger.warning(f"{stream} is not supported stream, choosing {self.get_supported_streams()[13]} "
                           f"as default stream. use get_supported_streams() to know all supported streams.")
            return self.get_supported_streams()[13]

    @staticmethod
    def get_supported_streams() -> List[Stream]:
        """
        List all supported streams for FS.

        :return: Array of stream ID enums.
        :rtype: List

        .. code-block:: python3
            :emphasize-lines: 5

            from adi_study_watch import SDK

            sdk = SDK("COM4")
            application = sdk.get_fs_application()
            x = application.get_supported_streams()
            print(x)
            # [<Stream.ADPD1: ['0xC2', '0x11']>, ... , <Stream.SQI: ['0xC8', '0xD']>]
        """
        return [FSApplication.STREAM_ADPD1, FSApplication.STREAM_ADPD2, FSApplication.STREAM_ADPD3,
                FSApplication.STREAM_ADPD4, FSApplication.STREAM_ADPD5, FSApplication.STREAM_ADPD6,
                FSApplication.STREAM_ADPD7, FSApplication.STREAM_ADPD8, FSApplication.STREAM_ADPD9,
                FSApplication.STREAM_ADPD10, FSApplication.STREAM_ADPD11, FSApplication.STREAM_ADPD12,
                FSApplication.STREAM_ADXL, FSApplication.STREAM_BIA, FSApplication.STREAM_ECG, FSApplication.STREAM_EDA,
                FSApplication.STREAM_PEDOMETER, FSApplication.STREAM_PPG, FSApplication.STREAM_TEMPERATURE,
                FSApplication.STREAM_SQI, FSApplication.STREAM_HRV, FSApplication.STREAM_STATIC_AGC,
                FSApplication.STREAM_DYNAMIC_AGC, FSApplication.STREAM_BATTERY]

    def abort_logging(self) -> Dict:
        """
        Aborts all logging process.

        :return: A response packet as dictionary.
        :rtype: Dict

        .. code-block:: python3
            :emphasize-lines: 5

            from adi_study_watch import SDK

            sdk = SDK("COM4")
            application = sdk.get_fs_application()
            application.abort_logging()

        """
        request_packet = CommandPacket(self._destination, FSCommand.FORCE_STOP_LOG_REQ)
        response_packet = CommandPacket(self._destination, FSCommand.FORCE_STOP_LOG_RES)
        return self._send_packet(request_packet, response_packet)

    def delete_config_file(self) -> Dict:
        """
        Deletes config file.

        :return: A response packet as dictionary.
        :rtype: Dict

        .. code-block:: python3
            :emphasize-lines: 5

            from adi_study_watch import SDK

            sdk = SDK("COM4")
            application = sdk.get_fs_application()
            application.delete_config_file()
        """
        request_packet = CommandPacket(self._destination, FSCommand.DELETE_CONFIG_FILE_REQ)
        response_packet = CommandPacket(self._destination, FSCommand.DELETE_CONFIG_FILE_RES)
        return self._send_packet(request_packet, response_packet)

    def disable_config_log(self) -> Dict:
        """
        Disables config log.

        :return: A response packet as dictionary.
        :rtype: Dict

        .. code-block:: python3
            :emphasize-lines: 5

            from adi_study_watch import SDK

            sdk = SDK("COM4")
            application = sdk.get_fs_application()
            application.disable_config_log()
        """
        request_packet = CommandPacket(self._destination, FSCommand.DCFG_STOP_LOG_REQ)
        response_packet = CommandPacket(self._destination, FSCommand.DCFG_STOP_LOG_RES)
        return self._send_packet(request_packet, response_packet)

    def _write_config_file(self, commands) -> [Dict]:
        packet_size = 70
        packets = math.ceil(len(commands) / packet_size)
        packet_array = []
        for packet in range(packets):
            packet_array.append(commands[packet * packet_size:(packet + 1) * packet_size])
        result = []
        for i, byte in enumerate(packet_array):
            request_packet = ConfigFilePacket(self._destination, FSCommand.LOG_USER_CONFIG_DATA_REQ)
            request_packet.set_payload("length", len(byte))
            request_packet.set_payload("bytes", byte)
            if i + 1 == packets:
                request_packet.set_payload("status", FSStatus.END_OF_FILE)
            else:
                request_packet.set_payload("status", FSStatus.OK)
            response_packet = CommandPacket(self._destination, FSCommand.LOG_USER_CONFIG_DATA_RES)
            result.append(self._send_packet(request_packet, response_packet))
        return result

    def write_config_file(self, filename: str) -> [Dict]:
        """
        Writes user config file into FS.

        :param filename: file to write.
        :return: A response packet as dictionary.
        :rtype: [Dict]

        .. code-block:: python3
            :emphasize-lines: 5

            from adi_study_watch import SDK

            sdk = SDK("COM4")
            application = sdk.get_fs_application()
            x = application.write_config_file("config.lcfg")
        """
        with open(filename, 'rb') as file:
            data = file.readlines()
            result = []
            for value in data:
                result += value
            return self._write_config_file(result)

    def stop_logging(self) -> Dict:
        """
        Stops current logging process.

        :return: A response packet as dictionary.
        :rtype: Dict

        .. code-block:: python3
            :emphasize-lines: 5

            from adi_study_watch import SDK

            sdk = SDK("COM4")
            application = sdk.get_fs_application()
            application.stop_logging()
        """
        request_packet = LoggingPacket(self._destination, FSCommand.STOP_LOGGING_REQ)
        request_packet.set_payload("logging_type", FSLogging.STOP_LOGGING)
        response_packet = LoggingPacket(self._destination, FSCommand.STOP_LOGGING_RES)
        return self._send_packet(request_packet, response_packet)

    def enable_config_log(self) -> Dict:
        """
        Enables config log.

        :return: A response packet as dictionary.
        :rtype: Dict

        .. code-block:: python3
            :emphasize-lines: 5

            from adi_study_watch import SDK

            sdk = SDK("COM4")
            application = sdk.get_fs_application()
            application.enable_config_log()
        """
        request_packet = CommandPacket(self._destination, FSCommand.DCFG_START_LOG_REQ)
        response_packet = CommandPacket(self._destination, FSCommand.DCFG_START_LOG_RES)
        return self._send_packet(request_packet, response_packet)

    def start_logging(self) -> Dict:
        """
        Starts current logging process.

        :return: A response packet as dictionary.
        :rtype: Dict

        .. code-block:: python3
            :emphasize-lines: 5

            from adi_study_watch import SDK

            sdk = SDK("COM4")
            application = sdk.get_fs_application()
            application.start_logging()
        """
        request_packet = CommandPacket(self._destination, FSCommand.START_LOGGING_REQ)
        response_packet = CommandPacket(self._destination, FSCommand.START_LOGGING_RES)
        return self._send_packet(request_packet, response_packet)

    def get_file_count(self) -> Dict:
        """
        Returns a packet containing number of file present on the device.

        :return: A response packet as dictionary.
        :rtype: Dict

        .. code-block:: python3
            :emphasize-lines: 5

            from adi_study_watch import SDK

            sdk = SDK("COM4")
            application = sdk.get_fs_application()
            x = application.get_file_count()
            print(x["payload"]["file_count"])
            # 3
        """
        request_packet = CommandPacket(self._destination, FSCommand.GET_NUMBER_OF_FILE_REQ)
        response_packet = FileCountPacket(self._destination, FSCommand.GET_NUMBER_OF_FILE_RES)
        return self._send_packet(request_packet, response_packet)

    def append_file(self) -> Dict:
        """
        append_file

        :return: A response packet as dictionary.
        :rtype: Dict

        .. code-block:: python3
            :emphasize-lines: 5

            from adi_study_watch import SDK

            sdk = SDK("COM4")
            application = sdk.get_fs_application()
            application.append_file()
        """
        request_packet = CommandPacket(self._destination, FSCommand.APPEND_FILE_REQ)
        response_packet = CommandPacket(self._destination, FSCommand.APPEND_FILE_RES)
        return self._send_packet(request_packet, response_packet)

    def format(self) -> Dict:
        """
        Format the entire file system.

        :return: A response packet as dictionary.
        :rtype: Dict

        .. code-block:: python3
            :emphasize-lines: 5

            from adi_study_watch import SDK

            sdk = SDK("COM4")
            application = sdk.get_fs_application()
            application.format()
        """
        request_packet = CommandPacket(self._destination, FSCommand.FORMAT_REQ)
        response_packet = CommandPacket(self._destination, FSCommand.FORMAT_RES)
        return self._send_packet(request_packet, response_packet)

    def get_stream_status(self, stream: Stream) -> Dict:
        """
        Returns specified stream status information.

        :param stream: stream to obtain status information, use get_supported_streams() to list all supported streams.
        :type stream: Stream
        :return: A response packet as dictionary.
        :rtype: Dict

        .. code-block:: python3
            :emphasize-lines: 5

            from adi_study_watch import SDK

            sdk = SDK("COM4")
            application = sdk.get_fs_application()
            x = application.get_supported_streams()
            print(x)
            # [<Stream.ADPD1: ['0xC2', '0x11']>, ... , <Stream.SQI: ['0xC8', '0x0D']>]
            x = application.get_stream_status(application.STREAM_ADXL)
            print(x["payload"]["stream_address"], x["payload"]["num_subscribers"], x["payload"]["num_start_registered"])
            # Stream.ADXL 0 0
        """
        stream = self._stream_helper(stream)
        request_packet = FSStreamStatusPacket(self._destination, FSCommand.GET_STREAM_SUB_STATUS_REQ)
        request_packet.set_payload("stream_address", stream)
        response_packet = FSStreamStatusPacket(self._destination, FSCommand.GET_STREAM_SUB_STATUS_RES)
        return self._send_packet(request_packet, response_packet)

    def inject_key_value_pair(self, value_id: int) -> Dict:
        """
        Inject Key Value Pair into the log.

        :param value_id: Key Value pair to inject in log.
        :type value_id: int
        :return: A response packet as dictionary.
        :rtype: Dict

        .. code-block:: python3
            :emphasize-lines: 5

            from adi_study_watch import SDK

            sdk = SDK("COM4")
            application = sdk.get_fs_application()
            x = application.inject_key_value_pair(1234)
            print(x["payload"]["status"])
            # FSStatus.OK
        """
        request_packet = KeyValuePairPacket(self._destination, FSCommand.SET_KEY_VALUE_PAIR_REQ)
        request_packet.set_payload("value_id", value_id)
        response_packet = KeyValuePairResponsePacket(self._destination, FSCommand.SET_KEY_VALUE_PAIR_RES)
        return self._send_packet(request_packet, response_packet)

    def ls(self) -> List[Dict]:
        """
        List all the files present on the device.

        :return: list of response packet as dictionary.
        :rtype: List

        .. code-block:: python3
            :emphasize-lines: 5

            from adi_study_watch import SDK

            sdk = SDK("COM4")
            application = sdk.get_fs_application()
            files = application.ls()
            for file in files:
                print(file["payload"]["filename"], file["payload"]["filetype"], file["payload"]["file_size"])

            # 1216471B.LOG FileType.DATA_FILE 5242880
            # 121647E1.LOG FileType.DATA_FILE 477636
            # 121647ED.LOG FileType.DATA_FILE 140206

        """
        request_packet = LSRequestPacket(self._destination, FSCommand.LS_REQ)
        packet_id = self._get_packet_id(FSCommand.LS_RES)
        queue = self._get_queue(packet_id)
        self._packet_manager.subscribe(packet_id, self._callback_command)
        self._packet_manager.send_packet(request_packet)
        result = []
        while True:
            data = self._get_queue_data(queue)
            response_packet = LSResponsePacket()
            response_packet.decode_packet(data)
            packet_dict = response_packet.get_dict()
            if not packet_dict["payload"]["status"] == FSStatus.OK:
                break
            result.append(packet_dict)
        self._packet_manager.unsubscribe(packet_id, self._callback_command)
        return result

    def mount(self) -> Dict:
        """
        Mounts the File system.

        :return: A response packet as dictionary.
        :rtype: Dict

        .. code-block:: python3
            :emphasize-lines: 5

            from adi_study_watch import SDK

            sdk = SDK("COM4")
            application = sdk.get_fs_application()
            application.mount()
        """
        request_packet = CommandPacket(self._destination, FSCommand.MOUNT_REQ)
        response_packet = CommandPacket(self._destination, FSCommand.MOUNT_RES)
        return self._send_packet(request_packet, response_packet)

    def get_status(self) -> Dict:
        """
        Returns current logging status.

        :return: A response packet as dictionary.
        :rtype: Dict

        .. code-block:: python3
            :emphasize-lines: 5

            from adi_study_watch import SDK

            sdk = SDK("COM4")
            application = sdk.get_fs_application()
            x = application.get_status()
            print(x["payload"]["status"])
            # FSStatus.LOGGING_IN_PROGRESS
        """
        request_packet = CommandPacket(self._destination, FSCommand.GET_STATUS_REQ)
        response_packet = CommandPacket(self._destination, FSCommand.GET_STATUS_RES)
        return self._send_packet(request_packet, response_packet)

    def stream_file(self, filename: str, file_stream_callback: Callable) -> None:
        """
        Stream specified file from the device.

        :param filename: filename to download, use ls() to obtain list of all files.
        :type filename: str
        :param file_stream_callback: callback for streaming file
        :type file_stream_callback: Callable

        .. code-block:: python3
            :emphasize-lines: 5

            from adi_study_watch import SDK

            def file_callback(data, total_size, stream_progress):
                print(data)
                # [{'header': {'source': <Stream.FS: ['0xC6', '0x1']>, .. , 'crc16': 18166}}]


            sdk = SDK("COM4")
            application = sdk.get_fs_application()
            # alternately yo can use download_file if you don't want to stream file content
            application.stream_file("1216471B.LOG", file_callback)

            # wait for stream to finish
            while True:
                pass

        """
        if self._packet_manager.source == Application.APP_BLE:
            logger.error(f"Can't stream file over BLE.")
            return

        files = self.ls()
        file_size = None
        for file in files:
            if file["payload"]["filename"] == filename.strip():
                file_size = file["payload"]["file_size"]

        if file_size is None:
            logger.error(f"{filename} is not present on the device, use ls() to list all the files.")
            return

        self._file_stream_callback = file_stream_callback
        request_packet = StreamFileRequestPacket(self._destination, FSCommand.DOWNLOAD_LOG_REQ)
        request_packet.set_payload("filename", filename)
        data_packet_id = self._get_packet_id(FSCommand.DOWNLOAD_LOG_RES, self._stream)
        self.stream_progress = 0
        self.total_size = file_size
        self._packet_manager.subscribe(data_packet_id, self._file_callback)
        self._packet_manager.send_packet(request_packet)

    def _file_callback(self, response_data, packet_id):
        response_packet = StreamFileResponsePacket()
        response_packet.decode_packet(response_data)
        packet_dict = response_packet.get_dict()
        self.stream_progress += packet_dict["payload"]["stream_length"]
        if self._file_stream_callback:
            self._file_stream_callback(packet_dict, self.total_size, self.stream_progress)
        else:
            logger.error(f"No callback to stream file.")
        if not packet_dict["payload"]["status"] == FSStatus.OK:
            self._packet_manager.unsubscribe(packet_id, self._file_callback)

    @staticmethod
    def _get_crc(response_data, data_length):
        crc16_data_array = response_data
        for index in range(0, 8, 2):
            crc16_data_array[index], crc16_data_array[index + 1] = crc16_data_array[index + 1], crc16_data_array[index]
        computed_crc = int(0xFFFF)
        for i in range(data_length):
            computed_crc = ((computed_crc >> 8) | (computed_crc << 8)) & 0xFFFF
            computed_crc = computed_crc ^ crc16_data_array[i]
            computed_crc ^= (computed_crc & 0xFF) >> 4
            computed_crc ^= ((computed_crc << 8) << 4) & 0xFFFF
            computed_crc ^= ((computed_crc & 0xFF) << 4) << 1

        return computed_crc

    def _fix_crc_failure(self, filename, crc_fail):
        progress_bar = tqdm(total=len(crc_fail))
        progress_bar.set_description("CRC check")
        for key, val in crc_fail.items():
            packet, response_bytes = self.download_file_chunk(filename, 0, *val)
            page_chunk_size = packet["payload"]["page_chunk_size"]
            computed_crc = self._get_crc(response_bytes, page_chunk_size + 15)
            if not computed_crc == packet["payload"]["crc16"]:
                crc_fail[key] = 0
                logger.error(f"CRC failure, while downloading the file Index - {key}.")
            if not packet["payload"]["status"] == FSStatus.OK:
                crc_fail[key] = 0
                logger.error(f"CRC failure, while downloading the file Index - {key}.")
            crc_fail[key] = packet["payload"]["page_chunk_bytes"]
            progress_bar.update(1)

        progress_bar.close()

    def _fix_sequence_number_failure(self, filename, sequence_number_fail):
        progress_bar = tqdm(total=len(sequence_number_fail))
        progress_bar.set_description("Sequence check")
        for key, val in list(sequence_number_fail.items()):
            roll_over, chunk_number, page_number, sequence_missing = val
            for i in range(sequence_missing):
                packet, response_bytes = self.download_file_chunk(filename, 1, roll_over, chunk_number, page_number)
                if page_number == 65535:
                    roll_over += 1
                chunk_number = packet["payload"]["page_chunk_number"]
                page_number = packet["payload"]["page_number"]
                page_chunk_size = packet["payload"]["page_chunk_size"]
                computed_crc = self._get_crc(response_bytes, page_chunk_size + 15)
                if not packet["payload"]["status"] == FSStatus.OK:
                    sequence_number_fail[key + i] = 0
                    logger.error(f"Missing sequence number, while downloading the file Index - {key}.")
                if not computed_crc == packet["payload"]["crc16"]:
                    sequence_number_fail[key + i] = 0
                    logger.error(f"Missing sequence number, while downloading the file Index - {key}.")
                sequence_number_fail[key + i] = packet["payload"]["page_chunk_bytes"]
            progress_bar.update(1)

        progress_bar.close()

    @staticmethod
    def _join_file(filename, filename_temp, crc_fail, sequence_number_fail, total_index):
        progress_bar = tqdm(total=total_index)
        progress_bar.set_description("Generating LOG file")
        file_reader = open(filename_temp, 'r')
        file_writer = open(filename, 'wb')
        idx = 0

        for line in file_reader:
            new_line = [int(x) for x in line.split(",")]
            is_crc = crc_fail.get(idx, None)
            if is_crc:
                file_writer.write(bytearray(is_crc))
                idx += 1

            is_seq_number = sequence_number_fail.get(idx, None)
            if is_seq_number:
                while sequence_number_fail.get(idx, None):
                    seq_number = sequence_number_fail.get(idx, None)
                    file_writer.write(bytearray(seq_number))
                    idx += 1
                file_writer.write(bytearray(new_line))

            if not is_crc and not is_seq_number:
                file_writer.write(bytearray(new_line))
                idx += 1
            progress_bar.update(1)

        while sequence_number_fail.get(idx, None):
            seq_number = sequence_number_fail.get(idx, None)
            file_writer.write(bytearray(seq_number))
            idx += 1

        file_writer.close()
        file_reader.close()
        os.remove(filename_temp)
        progress_bar.close()

    def download_file(self, filename: str, download_to_file: bool = False, display_progress: bool = False) \
            -> List[Dict]:
        """
        Download specified file from the device.

        :param filename: filename to download, use ls() to obtain list of all files.
        :type filename: str
        :param download_to_file: save the payload.data_stream to the file
        :type download_to_file: bool
        :param display_progress: display progress of download.
        :type display_progress: bool
        :return: list of response packet as dictionary.
        :rtype: List

        .. code-block:: python3
            :emphasize-lines: 5

            from adi_study_watch import SDK

            sdk = SDK("COM4")
            application = sdk.get_fs_application()
            x = application.download_file("1216471B.LOG")
            print(x)
            # [{'header': {'source': <Stream.FS: ['0xC6', '0x1']>, .. , 'crc16': 18166}}]
        """
        if self._packet_manager.source == Application.APP_BLE:
            logger.error(f"Can't Download file over BLE.")
            return []

        files = self.ls()
        file_size = None
        for file in files:
            if file["payload"]["filename"] == filename.strip():
                file_size = file["payload"]["file_size"]

        if file_size is None:
            logger.error(f"{filename} is not present on the device, use ls() to list all the files.")
            return []

        request_packet = StreamFileRequestPacket(self._destination, FSCommand.DOWNLOAD_LOG_REQ)
        request_packet.set_payload("filename", filename)
        data_packet_id = self._get_packet_id(FSCommand.DOWNLOAD_LOG_RES, self._stream)
        self._packet_manager.subscribe(data_packet_id, self._callback_command)
        self._packet_manager.send_packet(request_packet)
        queue = self._get_queue(data_packet_id)
        data = []
        progress_bar = None
        file_writer = None
        filename_temp = filename + "_TEMP"
        if download_to_file:
            try:
                file_writer = open(filename_temp, 'w')
            except Exception as e:
                logger.error(f"Can't open file {filename_temp} with write binary permission, reason :: {e}.")
        if display_progress:
            progress_bar = tqdm(total=file_size)
            progress_bar.set_description("Packet download")
        crc_fail = {}
        sequence_number_fail = {}
        sequence_number = 0
        prev_page_number = None
        prev_page_roll_over = None
        page_roll_over = 0
        prev_page_chunk_number = None
        idx = 0
        while True:
            response_data = self._get_queue_data(queue)
            response_packet = StreamFileResponsePacket()
            response_packet.decode_packet(response_data)
            packet_dict = response_packet.get_dict()
            page_chunk_size = packet_dict["payload"]["page_chunk_size"]
            if display_progress:
                progress_bar.update(page_chunk_size)
            if download_to_file:
                page_chunk_bytes = packet_dict["payload"]["page_chunk_bytes"]
                if not page_chunk_size == len(page_chunk_bytes):
                    page_chunk_bytes = page_chunk_bytes[:page_chunk_size]
                if len(page_chunk_bytes) > 0:
                    file_writer.write(",".join([str(x) for x in page_chunk_bytes]))
                    file_writer.write("\n")
                else:
                    logger.error(f"Page chunk read is empty :: {packet_dict}")
            else:
                data.append(packet_dict)

            computed_crc = self._get_crc(response_data, page_chunk_size + 15)
            page_number = packet_dict["payload"]["page_number"]
            page_chunk_number = packet_dict["payload"]["page_chunk_number"]

            if not computed_crc == packet_dict["payload"]["crc16"]:
                crc_fail[idx] = (page_roll_over, page_chunk_number, page_number)
            if not sequence_number == packet_dict["header"]["checksum"]:
                number_of_sequence_missing = 0
                while not sequence_number == packet_dict["header"]["checksum"]:
                    number_of_sequence_missing += 1
                    sequence_number = (sequence_number + 1) % 65536

                number_of_sequence_missing = packet_dict["header"]["checksum"] - sequence_number
                number_of_sequence_missing = abs(number_of_sequence_missing)
                sequence_number_fail[idx] = (prev_page_roll_over, prev_page_chunk_number, prev_page_number,
                                             number_of_sequence_missing)
                sequence_number = (packet_dict["header"]["checksum"] + 1) % 65536
                idx += number_of_sequence_missing + 1
            else:
                sequence_number = (sequence_number + 1) % 65536
                idx += 1

            if packet_dict["payload"]["page_number"] == 65535:
                page_roll_over += 1

            prev_page_roll_over = page_roll_over
            prev_page_number = page_number
            prev_page_chunk_number = page_chunk_number

            if not packet_dict["payload"]["status"] == FSStatus.OK:
                break

        if download_to_file:
            file_writer.close()

        if display_progress:
            progress_bar.clear()
            progress_bar.close()

        self._fix_crc_failure(filename, crc_fail)
        self._fix_sequence_number_failure(filename, sequence_number_fail)
        self._join_file(filename, filename_temp, crc_fail, sequence_number_fail, idx)

        self._packet_manager.unsubscribe(data_packet_id, self._callback_command)
        return data

    def download_file_chunk(self, filename: str, retransmit_type: int, page_roll_over: int, page_chunk_number: int,
                            page_number: int) -> Dict:
        """
        Download specified chunk of file from the device.

        :param page_number:
        :param page_chunk_number:
        :param page_roll_over:
        :param retransmit_type:
        :param filename: filename to download, use ls() to obtain list of all files.
        :type filename: str
        :return: A response packet as dictionary.
        :rtype: Dict

        .. code-block:: python3
            :emphasize-lines: 5

            from adi_study_watch import SDK

            sdk = SDK("COM4")
            application = sdk.get_fs_application()
            x = application.download_file_chunk(0, 50, "1216471B.LOG")
            print(x)
            # {'header': {'source': <Stream.FS: ['0xC6', '0x1']>, .. , 'crc16': 18166}}
        """
        request_packet = StreamFileChunkPacket(self._destination, FSCommand.CHUNK_RETRANSMIT_REQ)
        request_packet.set_payload("retransmit_type", retransmit_type)
        request_packet.set_payload("page_roll_over", page_roll_over)
        request_packet.set_payload("page_chunk_number", page_chunk_number)
        request_packet.set_payload("page_number", page_number)
        request_packet.set_payload("filename", filename)
        response_packet = StreamFileResponsePacket(self._destination, FSCommand.CHUNK_RETRANSMIT_RES)
        return self._send_packet(request_packet, response_packet, get_bytes=True)

    def subscribe_stream(self, stream: Stream) -> Dict:
        """
        Subscribe to the specified stream.

        :param stream: Stream to subscribe.
        :type stream: Stream
        :return: A response packet as dictionary.
        :rtype: Dict

        .. code-block:: python3
            :emphasize-lines: 5

            from adi_study_watch import SDK

            sdk = SDK("COM4")
            application = sdk.get_fs_application()
            x = application.get_supported_streams()
            print(x)
            # [<Stream.ADPD1: ['0xC2', '0x11']>, ... , <Stream.SQI: ['0xC8', '0xD']>]
            x = application.subscribe_stream(application.STREAM_ADXL)
            print(x["payload"]["status"], x["payload"]["stream_address"])
            # CommonStatus.SUBSCRIBER_ADDED Stream.ADXL
        """
        stream = self._stream_helper(stream)
        request_packet = StreamPacket(self._destination, FSCommand.START_STREAM_LOGGING_REQ)
        request_packet.set_payload("stream_address", stream)
        response_packet = StreamPacket(self._destination, FSCommand.START_STREAM_LOGGING_RES)
        return self._send_packet(request_packet, response_packet)

    def unsubscribe_stream(self, stream: Stream) -> Dict:
        """
        UnSubscribe to the specified stream.

        :param stream: Stream to unsubscribe.
        :type stream: Stream
        :return: A response packet as dictionary.
        :rtype: Dict

        .. code-block:: python3
            :emphasize-lines: 5

            from adi_study_watch import SDK

            sdk = SDK("COM4")
            application = sdk.get_fs_application()
            x = application.get_supported_streams()
            print(x)
            # [<Stream.ADPD1: ['0xC2', '0x11']>, ... , <Stream.SQI: ['0xC8', '0xD']>]
            x = application.unsubscribe_stream(application.STREAM_ADXL)
            print(x["payload"]["status"], x["payload"]["stream_address"])
            # CommonStatus.SUBSCRIBER_COUNT_DECREMENT Stream.ADXL
        """
        stream = self._stream_helper(stream)
        request_packet = StreamPacket(self._destination, FSCommand.STOP_STREAM_LOGGING_REQ)
        request_packet.set_payload("stream_address", stream)
        response_packet = StreamPacket(self._destination, FSCommand.STOP_STREAM_LOGGING_RES)
        return self._send_packet(request_packet, response_packet)

    def volume_info(self) -> Dict:
        """
        Returns file system volume information.

        :return: A response packet as dictionary.
        :rtype: Dict

        .. code-block:: python3
            :emphasize-lines: 5

            from adi_study_watch import SDK

            sdk = SDK("COM4")
            application = sdk.get_fs_application()
            x = application.volume_info()
            print(f'{x["payload"]["total_memory"]}, {x["payload"]["used_memory"]}, {x["payload"]["available_memory"]}%')
            # 536870656, 6197248, 98%
        """
        request_packet = CommandPacket(self._destination, FSCommand.VOL_INFO_REQ)
        response_packet = VolumeInfoPacket(self._destination, FSCommand.VOL_INFO_RES)
        return self._send_packet(request_packet, response_packet)
