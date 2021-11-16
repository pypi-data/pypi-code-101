from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sover:
	"""Sover commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sover", core, parent)

	def get_offset(self) -> float:
		"""SCPI: [SOURce<HW>]:POWer:ATTenuation:SOVer:[OFFSet] \n
		Snippet: value: float = driver.source.power.attenuation.sover.get_offset() \n
		Sets the switch-over offset value of the attenuator. \n
			:return: offset: float Range: -10 to 10
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:POWer:ATTenuation:SOVer:OFFSet?')
		return Conversions.str_to_float(response)

	def set_offset(self, offset: float) -> None:
		"""SCPI: [SOURce<HW>]:POWer:ATTenuation:SOVer:[OFFSet] \n
		Snippet: driver.source.power.attenuation.sover.set_offset(offset = 1.0) \n
		Sets the switch-over offset value of the attenuator. \n
			:param offset: float Range: -10 to 10
		"""
		param = Conversions.decimal_value_to_str(offset)
		self._core.io.write(f'SOURce<HwInstance>:POWer:ATTenuation:SOVer:OFFSet {param}')
