from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Gain:
	"""Gain commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("gain", core, parent)

	def get_rx(self) -> int:
		"""SCPI: [SOURce<HW>]:AREGenerator:RADar:ANTenna:REG:GAIN:RX \n
		Snippet: value: int = driver.source.areGenerator.radar.antenna.reg.gain.get_rx() \n
		Queries the antenna gain of the transmitting/receiving antenna.
		If [:SOURce<hw>]:AREGenerator:RADar:ANTenna:CUSTom[:STATe]1, you can define a customer-specific antenna gain value. \n
			:return: areg_ant_gain_rx: integer Range: 0 to 30
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:AREGenerator:RADar:ANTenna:REG:GAIN:RX?')
		return Conversions.str_to_int(response)

	def set_rx(self, areg_ant_gain_rx: int) -> None:
		"""SCPI: [SOURce<HW>]:AREGenerator:RADar:ANTenna:REG:GAIN:RX \n
		Snippet: driver.source.areGenerator.radar.antenna.reg.gain.set_rx(areg_ant_gain_rx = 1) \n
		Queries the antenna gain of the transmitting/receiving antenna.
		If [:SOURce<hw>]:AREGenerator:RADar:ANTenna:CUSTom[:STATe]1, you can define a customer-specific antenna gain value. \n
			:param areg_ant_gain_rx: integer Range: 0 to 30
		"""
		param = Conversions.decimal_value_to_str(areg_ant_gain_rx)
		self._core.io.write(f'SOURce<HwInstance>:AREGenerator:RADar:ANTenna:REG:GAIN:RX {param}')

	def get_tx(self) -> int:
		"""SCPI: [SOURce<HW>]:AREGenerator:RADar:ANTenna:REG:GAIN:TX \n
		Snippet: value: int = driver.source.areGenerator.radar.antenna.reg.gain.get_tx() \n
		Queries the antenna gain of the transmitting/receiving antenna.
		If [:SOURce<hw>]:AREGenerator:RADar:ANTenna:CUSTom[:STATe]1, you can define a customer-specific antenna gain value. \n
			:return: areg_ant_gain_tx: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:AREGenerator:RADar:ANTenna:REG:GAIN:TX?')
		return Conversions.str_to_int(response)

	def set_tx(self, areg_ant_gain_tx: int) -> None:
		"""SCPI: [SOURce<HW>]:AREGenerator:RADar:ANTenna:REG:GAIN:TX \n
		Snippet: driver.source.areGenerator.radar.antenna.reg.gain.set_tx(areg_ant_gain_tx = 1) \n
		Queries the antenna gain of the transmitting/receiving antenna.
		If [:SOURce<hw>]:AREGenerator:RADar:ANTenna:CUSTom[:STATe]1, you can define a customer-specific antenna gain value. \n
			:param areg_ant_gain_tx: integer Range: 0 to 30
		"""
		param = Conversions.decimal_value_to_str(areg_ant_gain_tx)
		self._core.io.write(f'SOURce<HwInstance>:AREGenerator:RADar:ANTenna:REG:GAIN:TX {param}')
