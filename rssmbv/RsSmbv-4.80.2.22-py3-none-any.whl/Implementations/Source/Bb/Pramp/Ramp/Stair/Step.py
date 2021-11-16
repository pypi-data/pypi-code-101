from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Step:
	"""Step commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("step", core, parent)

	def get_level(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:PRAMp:RAMP:STAir:STEP:LEVel \n
		Snippet: value: float = driver.source.bb.pramp.ramp.stair.step.get_level() \n
		No command help available \n
			:return: step: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:PRAMp:RAMP:STAir:STEP:LEVel?')
		return Conversions.str_to_float(response)

	def set_level(self, step: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:PRAMp:RAMP:STAir:STEP:LEVel \n
		Snippet: driver.source.bb.pramp.ramp.stair.step.set_level(step = 1.0) \n
		No command help available \n
			:param step: No help available
		"""
		param = Conversions.decimal_value_to_str(step)
		self._core.io.write(f'SOURce<HwInstance>:BB:PRAMp:RAMP:STAir:STEP:LEVel {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:PRAMp:RAMP:STAir:STEP:[STATe] \n
		Snippet: value: bool = driver.source.bb.pramp.ramp.stair.step.get_state() \n
		No command help available \n
			:return: enable_power_step: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:PRAMp:RAMP:STAir:STEP:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, enable_power_step: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:PRAMp:RAMP:STAir:STEP:[STATe] \n
		Snippet: driver.source.bb.pramp.ramp.stair.step.set_state(enable_power_step = False) \n
		No command help available \n
			:param enable_power_step: No help available
		"""
		param = Conversions.bool_to_str(enable_power_step)
		self._core.io.write(f'SOURce<HwInstance>:BB:PRAMp:RAMP:STAir:STEP:STATe {param}')
