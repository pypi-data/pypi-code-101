from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Marker:
	"""Marker commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("marker", core, parent)

	def get_frequency(self) -> int:
		"""SCPI: [SOURce<HW>]:[ILS]:MBEacon:MARKer:FREQuency \n
		Snippet: value: int = driver.source.ils.mbeacon.marker.get_frequency() \n
		No command help available \n
			:return: frequency: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:ILS:MBEacon:MARKer:FREQuency?')
		return Conversions.str_to_int(response)

	def set_frequency(self, frequency: int) -> None:
		"""SCPI: [SOURce<HW>]:[ILS]:MBEacon:MARKer:FREQuency \n
		Snippet: driver.source.ils.mbeacon.marker.set_frequency(frequency = 1) \n
		No command help available \n
			:param frequency: No help available
		"""
		param = Conversions.decimal_value_to_str(frequency)
		self._core.io.write(f'SOURce<HwInstance>:ILS:MBEacon:MARKer:FREQuency {param}')
