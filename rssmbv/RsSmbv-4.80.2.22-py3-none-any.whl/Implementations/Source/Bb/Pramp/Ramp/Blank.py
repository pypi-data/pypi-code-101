from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Blank:
	"""Blank commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("blank", core, parent)

	def get_time(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:PRAMp:RAMP:BLANk:TIME \n
		Snippet: value: float = driver.source.bb.pramp.ramp.blank.get_time() \n
		No command help available \n
			:return: rf_blanking: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:PRAMp:RAMP:BLANk:TIME?')
		return Conversions.str_to_float(response)

	def set_time(self, rf_blanking: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:PRAMp:RAMP:BLANk:TIME \n
		Snippet: driver.source.bb.pramp.ramp.blank.set_time(rf_blanking = 1.0) \n
		No command help available \n
			:param rf_blanking: No help available
		"""
		param = Conversions.decimal_value_to_str(rf_blanking)
		self._core.io.write(f'SOURce<HwInstance>:BB:PRAMp:RAMP:BLANk:TIME {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:PRAMp:RAMP:BLANk:[STATe] \n
		Snippet: value: bool = driver.source.bb.pramp.ramp.blank.get_state() \n
		No command help available \n
			:return: enable_rf_blank: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:PRAMp:RAMP:BLANk:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, enable_rf_blank: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:PRAMp:RAMP:BLANk:[STATe] \n
		Snippet: driver.source.bb.pramp.ramp.blank.set_state(enable_rf_blank = False) \n
		No command help available \n
			:param enable_rf_blank: No help available
		"""
		param = Conversions.bool_to_str(enable_rf_blank)
		self._core.io.write(f'SOURce<HwInstance>:BB:PRAMp:RAMP:BLANk:STATe {param}')
