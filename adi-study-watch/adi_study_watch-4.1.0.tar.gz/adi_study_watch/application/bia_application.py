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
from typing import List, Dict

from ..core import utils
from .csv_logging import CSVLogger
from .common_stream import CommonStream
from ..core.enums.dcb_enums import DCBCommand
from ..core.packets.command_packet import CommandPacket
from ..core.packets.stream_data_packets import BIADataPacket
from ..core.enums.common_enums import Application, Stream, CommonCommand
from ..core.enums.bia_enums import BIACommand, HSResistorTIA, BIADFTWindow
from ..core.packets.bia_packets import HSRTIAPacket, BIADCBPacket, BIADFTPacket, BIALibraryConfigPacket

logger = logging.getLogger(__name__)


class BIAApplication(CommonStream):
    """
    BIA Application class.

    .. code-block:: python3
        :emphasize-lines: 4

        from adi_study_watch import SDK

        sdk = SDK("COM4")
        application = sdk.get_bia_application()

    """

    RESISTOR_200 = HSResistorTIA.RESISTOR_200
    RESISTOR_1K = HSResistorTIA.RESISTOR_1K
    RESISTOR_5K = HSResistorTIA.RESISTOR_5K

    DFT_WINDOW_4 = BIADFTWindow.DFT_WINDOW_4
    DFT_WINDOW_8 = BIADFTWindow.DFT_WINDOW_8
    DFT_WINDOW_16 = BIADFTWindow.DFT_WINDOW_16
    DFT_WINDOW_32 = BIADFTWindow.DFT_WINDOW_32
    DFT_WINDOW_64 = BIADFTWindow.DFT_WINDOW_64
    DFT_WINDOW_128 = BIADFTWindow.DFT_WINDOW_128
    DFT_WINDOW_256 = BIADFTWindow.DFT_WINDOW_256
    DFT_WINDOW_512 = BIADFTWindow.DFT_WINDOW_512
    DFT_WINDOW_1024 = BIADFTWindow.DFT_WINDOW_1024
    DFT_WINDOW_2048 = BIADFTWindow.DFT_WINDOW_2048
    DFT_WINDOW_4096 = BIADFTWindow.DFT_WINDOW_4096
    DFT_WINDOW_8192 = BIADFTWindow.DFT_WINDOW_8192
    DFT_WINDOW_16384 = BIADFTWindow.DFT_WINDOW_16384

    def __init__(self, packet_manager):
        super().__init__(Application.BIA, Stream.BIA, packet_manager)
        self._dcb_size = 18

    @staticmethod
    def get_supported_dft_windows() -> List[BIADFTWindow]:
        """
        List all supported DFT window for BIA.

        :return: Array of DFT window enums.
        :rtype: List

        .. code-block:: python3
            :emphasize-lines: 5

            from adi_study_watch import SDK

            sdk = SDK("COM4")
            application = sdk.get_bia_application()
            x = application.get_supported_dft_windows()
            print(x)
            # [<BIADFTWindow.DFT_WINDOW_4: ['0x0', '0x0']>, ... , <BIADFTWindow.DFT_WINDOW_16384: ['0x0', '0x12']>]
        """
        return [BIAApplication.DFT_WINDOW_4, BIAApplication.DFT_WINDOW_8, BIAApplication.DFT_WINDOW_16,
                BIAApplication.DFT_WINDOW_32, BIAApplication.DFT_WINDOW_64, BIAApplication.DFT_WINDOW_128,
                BIAApplication.DFT_WINDOW_256, BIAApplication.DFT_WINDOW_512, BIAApplication.DFT_WINDOW_1024,
                BIAApplication.DFT_WINDOW_2048, BIAApplication.DFT_WINDOW_4096, BIAApplication.DFT_WINDOW_8192,
                BIAApplication.DFT_WINDOW_16384]

    @staticmethod
    def get_supported_hs_resistor_tia_ids() -> List[HSResistorTIA]:
        """
        List all supported High Speed Resistor Trans Impedance Amplifier for BIA.

        :return: Array of High Speed Resistor Trans Impedance Amplifier enums.
        :rtype: List

        .. code-block:: python3
            :emphasize-lines: 5

            from adi_study_watch import SDK

            sdk = SDK("COM4")
            application = sdk.get_bia_application()
            x = application.get_supported_hs_resistor_tia_ids()
            print(x)
            # [<HSResistorTIA.RESISTOR_200: ['0x0', '0x0']>, ... , <HSResistorTIA.RESISTOR_5K: ['0x0', '0x2']>]

        """
        return [BIAApplication.RESISTOR_200, BIAApplication.RESISTOR_1K, BIAApplication.RESISTOR_5K]

    def calibrate_hs_resistor_tia(self, hs_resistor_tia_id: HSResistorTIA) -> Dict:
        """
        Calibrate High Speed Resistor Trans Impedance Amplifier.

        :param hs_resistor_tia_id: High Speed Resistor Trans Impedance Amplifier to calibrate,
                                  | use get_supported_hs_resistor_tia_ids() to list all supported resistor.
        :type hs_resistor_tia_id: HSResistorTIA
        :return: A response packet as dictionary.
        :rtype: Dict

        .. code-block:: python3
            :emphasize-lines: 5

            from adi_study_watch import SDK

            sdk = SDK("COM4")
            application = sdk.get_bia_application()
            x = application.get_supported_hs_resistor_tia_ids()
            print(x)
            # [<HSResistorTIA.RESISTOR_200: ['0x0', '0x0']>, ... , <HSResistorTIA.RESISTOR_5K: ['0x0', '0x2']>]
            x = application.calibrate_hs_resistor_tia(application.RESISTOR_1K)
            print(x["payload"]["hs_resistor_tia"])
            # HSResistorTIA.RESISTOR_1K

        """
        request_packet = HSRTIAPacket(self._destination, BIACommand.SET_HS_TRANS_IMPEDANCE_AMPLIFIER_CAL_REQ)
        request_packet.set_payload("hs_resistor_tia", hs_resistor_tia_id)
        response_packet = HSRTIAPacket(self._destination, BIACommand.SET_HS_TRANS_IMPEDANCE_AMPLIFIER_CAL_RES)
        return self._send_packet(request_packet, response_packet)

    def set_discrete_fourier_transformation(self, dft_window: BIADFTWindow) -> Dict:
        """
        Set Discrete Fourier Transformation for BIA.

        :param dft_window: DFT window for Discrete Fourier Transformation, use get_supported_dft_windows()
                          | to list all supported DFT window.
        :type dft_window: BIADFTWindow
        :return: A response packet as dictionary.
        :rtype: Dict

        .. code-block:: python3
            :emphasize-lines: 5

            from adi_study_watch import SDK

            sdk = SDK("COM4")
            application = sdk.get_bia_application()
            x = application.get_supported_dft_windows()
            print(x)
            # [<BCMDFTWindow.DFT_WINDOW_4: ['0x0', '0x0']>, ... ,<BCMDFTWindow.DFT_WINDOW_16384: ['0x0', '0x12']>]
            x = application.set_discrete_fourier_transformation(application.DFT_WINDOW_16384)
            print(x["payload"]["dft_window"])
            # BCMDFTWindow.DFT_WINDOW_16384
        """
        request_packet = BIADFTPacket(self._destination, BIACommand.SET_DFT_NUM_REQ)
        request_packet.set_payload("dft_window", dft_window)
        response_packet = BIADFTPacket(self._destination, BIACommand.SET_DFT_NUM_RES)
        return self._send_packet(request_packet, response_packet)

    def read_library_configuration(self, fields: List[int]) -> Dict:
        """
        Reads library configuration from specified field values.

        :param fields: List of field values to read.
        :type fields: List[int]
        :return: A response packet as dictionary
        :rtype: Dict

        .. list-table::
           :widths: 50 50
           :header-rows: 1

           * - Fields Lower Limit
             - Fields Upper Limit
           * - 0x00
             - 0x12

        .. code-block:: python3
            :emphasize-lines: 5

            from adi_study_watch import SDK

            sdk = SDK("COM4")
            application = sdk.get_bia_application()
            x = application.read_library_configuration([0x00])
            print(x["payload"]["data"])
            # [['0x0', '0x0']]

        """
        data = [[field, 0] for field in fields]
        request_packet = BIALibraryConfigPacket(self._destination, CommonCommand.READ_LCFG_REQ)
        request_packet.set_payload("size", len(data))
        request_packet.set_payload("data", data)
        response_packet = BIALibraryConfigPacket(self._destination, CommonCommand.READ_LCFG_RES)
        return self._send_packet(request_packet, response_packet)

    def write_library_configuration(self, fields_values: List[List[int]]) -> Dict:
        """
        Writes library configuration from List of fields and values.

        :param fields_values: List of fields and values to write.
        :type fields_values: List[List[int]]
        :return: A response packet as dictionary.
        :rtype: Dict

        .. list-table::
           :widths: 50 50
           :header-rows: 1

           * - Fields Lower Limit
             - Fields Upper Limit
           * - 0x00
             - 0x12

        .. code-block:: python3
            :emphasize-lines: 5

            from adi_study_watch import SDK

            sdk = SDK("COM4")
            application = sdk.get_bia_application()
            x = application.write_library_configuration([[0x00, 0x1]])
            print(x["payload"]["data"])
            # [['0x0', '0x1']]

        """
        request_packet = BIALibraryConfigPacket(self._destination, CommonCommand.WRITE_LCFG_REQ)
        request_packet.set_payload("size", len(fields_values))
        request_packet.set_payload("data", fields_values)
        response_packet = BIALibraryConfigPacket(self._destination, CommonCommand.WRITE_LCFG_RES)
        return self._send_packet(request_packet, response_packet)

    def write_dcb_to_lcfg(self) -> Dict:
        """
        Writes Device configuration block data to library configuration.

        :return: A response packet as dictionary.
        :rtype: Dict

        .. code-block:: python3
            :emphasize-lines: 5

            from adi_study_watch import SDK

            sdk = SDK("COM4")
            application = sdk.get_bia_application()
            x = application.write_dcb_to_lcfg()
            print(x["payload"]["status"])
            # CommonStatus.OK
        """
        request_packet = CommandPacket(self._destination, CommonCommand.SET_LCFG_REQ)
        response_packet = CommandPacket(self._destination, CommonCommand.SET_LCFG_RES)
        return self._send_packet(request_packet, response_packet)

    def delete_device_configuration_block(self) -> Dict:
        """
        Deletes BIA Device configuration block.

        :return: A response packet as dictionary.
        :rtype: Dict

        .. code-block:: python3
            :emphasize-lines: 5

            from adi_study_watch import SDK

            sdk = SDK("COM4")
            application = sdk.get_bia_application()
            application.delete_device_configuration_block()
        """
        request_packet = CommandPacket(self._destination, DCBCommand.ERASE_CONFIG_REQ)
        response_packet = BIADCBPacket(self._destination, DCBCommand.ERASE_CONFIG_RES)
        return self._send_packet(request_packet, response_packet)

    def read_device_configuration_block(self) -> Dict:
        """
        Returns entire device configuration block.

        :return: A response packet as dictionary.
        :rtype: Dict

        .. code-block:: python3
            :emphasize-lines: 5

            from adi_study_watch import SDK

            sdk = SDK("COM4")
            application = sdk.get_bia_application()
            x = application.read_device_configuration_block()
            print(x["payload"]["data"])
            # []

        """
        request_packet = CommandPacket(self._destination, DCBCommand.READ_CONFIG_REQ)
        response_packet = BIADCBPacket(self._destination, DCBCommand.READ_CONFIG_RES)
        response_dict = self._send_packet(request_packet, response_packet)
        response_dict["payload"]["data"] = utils.add_index_to_array(response_dict["payload"]["data"], to_hex=True)
        return response_dict

    def write_device_configuration_block(self, addresses_values: List[List[int]]) -> Dict:
        """
        Writes the device configuration block values of specified addresses.
        This function takes a list of addresses and values to write, and returns a response packet as
        dictionary containing addresses and values.

        :param addresses_values: List of addresses and values to write.
        :type addresses_values: List[List[int]]
        :return: A response packet as dictionary.
        :rtype: Dict

        .. list-table::
           :widths: 50 50
           :header-rows: 1

           * - Address Lower Limit
             - Address Upper Limit
           * - 0x00
             - 0x12

        .. code-block:: python3
            :emphasize-lines: 5

            from adi_study_watch import SDK

            sdk = SDK("COM4")
            application = sdk.get_bia_application()
            x = application.write_device_configuration_block([[0x0, 2], [0x1, 0x1]])
            print(x["payload"]["size"])
            # 2

        """
        dcb_array = [0] * self._dcb_size
        for address_value in addresses_values:
            address = address_value[0]
            value = address_value[1]
            dcb_array[address] = value
        request_packet = BIADCBPacket(self._destination, DCBCommand.WRITE_CONFIG_REQ)
        request_packet.set_payload("size", len(dcb_array))
        request_packet.set_payload("data", dcb_array)
        response_packet = BIADCBPacket(self._destination, DCBCommand.WRITE_CONFIG_RES)
        return self._send_packet(request_packet, response_packet)

    def write_device_configuration_block_from_file(self, filename: str) -> Dict:
        """
        Writes the device configuration block values of specified addresses from file.

        :param filename: dcb filename
        :return: A response packet as dictionary.
        :rtype: Dict

        .. list-table::
           :widths: 50 50
           :header-rows: 1

           * - Address Lower Limit
             - Address Upper Limit
           * - 0x00
             - 0x12

        .. code-block:: python3
            :emphasize-lines: 5

            from adi_study_watch import SDK

            sdk = SDK("COM4")
            application = sdk.get_bia_application()
            application.write_device_configuration_block_from_file("bcm_dcb.dcfg")

        """
        result = self.device_configuration_file_to_list(filename)
        if result:
            return self.write_device_configuration_block(result)

    def _callback_data(self, packet, packet_id, callback_function=None, args=None):
        """
        Process and returns the data back to user's callback function.
        """
        self._callback_data_helper(packet, BIADataPacket())

    def enable_csv_logging(self, filename, header=None) -> None:
        """
        Start logging stream data into CSV.

        :param filename: Name of the CSV file.
        :param header: Header list of the CSV file.
        :return: A response packet as dictionary.
        :rtype: Dict

        .. code-block:: python3
            :emphasize-lines: 5

            from adi_study_watch import SDK

            sdk = SDK("COM4")
            application = sdk.get_bia_application()
            x = application.enable_csv_logging("bcm.csv")
        """
        if header is None:
            header = ["Timestamp", "IMP Real(Ohms)", "IMP Img(Ohms)", "IMP Module(Ohms)", "IMP Phase(Rad)",
                      "ADM Real(Ohms)", "ADM Img(Ohms)", "ADM Module(Ohms)", "ADM Phase(Rad)", "Seq No."]
        self._csv_logger[Stream.BIA] = CSVLogger(filename, header)

    def disable_csv_logging(self) -> None:
        """
        Stops logging stream data into CSV.

        :return: A response packet as dictionary.
        :rtype: Dict

        .. code-block:: python3
            :emphasize-lines: 5

            from adi_study_watch import SDK

            sdk = SDK("COM4")
            application = sdk.get_bia_application()
            x = application.disable_csv_logging()
        """
        if self._csv_logger.get(Stream.BIA):
            self._csv_logger[Stream.BIA].stop_logging()
        self._csv_logger[Stream.BIA] = None
