from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dwell:
	"""Dwell commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dwell", core, parent)

	def get_time(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:PRAMp:RAMP:STAir:DWELl:TIME \n
		Snippet: value: float = driver.source.bb.pramp.ramp.stair.dwell.get_time() \n
		No command help available \n
			:return: dwell_time: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:PRAMp:RAMP:STAir:DWELl:TIME?')
		return Conversions.str_to_float(response)

	def set_time(self, dwell_time: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:PRAMp:RAMP:STAir:DWELl:TIME \n
		Snippet: driver.source.bb.pramp.ramp.stair.dwell.set_time(dwell_time = 1.0) \n
		No command help available \n
			:param dwell_time: No help available
		"""
		param = Conversions.decimal_value_to_str(dwell_time)
		self._core.io.write(f'SOURce<HwInstance>:BB:PRAMp:RAMP:STAir:DWELl:TIME {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:PRAMp:RAMP:STAir:DWELl:[STATe] \n
		Snippet: value: bool = driver.source.bb.pramp.ramp.stair.dwell.get_state() \n
		No command help available \n
			:return: enable_dwell: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:PRAMp:RAMP:STAir:DWELl:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, enable_dwell: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:PRAMp:RAMP:STAir:DWELl:[STATe] \n
		Snippet: driver.source.bb.pramp.ramp.stair.dwell.set_state(enable_dwell = False) \n
		No command help available \n
			:param enable_dwell: No help available
		"""
		param = Conversions.bool_to_str(enable_dwell)
		self._core.io.write(f'SOURce<HwInstance>:BB:PRAMp:RAMP:STAir:DWELl:STATe {param}')
