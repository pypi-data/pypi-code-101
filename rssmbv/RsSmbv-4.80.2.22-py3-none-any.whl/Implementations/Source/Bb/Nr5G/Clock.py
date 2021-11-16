from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Clock:
	"""Clock commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("clock", core, parent)

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.Nr5GclockMode:
		"""SCPI: [SOURce<HW>]:BB:NR5G:CLOCk:MODE \n
		Snippet: value: enums.Nr5GclockMode = driver.source.bb.nr5G.clock.get_mode() \n
		No command help available \n
			:return: clock_mode: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:CLOCk:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.Nr5GclockMode)

	def set_mode(self, clock_mode: enums.Nr5GclockMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:CLOCk:MODE \n
		Snippet: driver.source.bb.nr5G.clock.set_mode(clock_mode = enums.Nr5GclockMode.SAMPle) \n
		No command help available \n
			:param clock_mode: No help available
		"""
		param = Conversions.enum_scalar_to_str(clock_mode, enums.Nr5GclockMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:CLOCk:MODE {param}')

	def get_multiplier(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:NR5G:CLOCk:MULTiplier \n
		Snippet: value: int = driver.source.bb.nr5G.clock.get_multiplier() \n
		No command help available \n
			:return: clock_samp_mult: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:CLOCk:MULTiplier?')
		return Conversions.str_to_int(response)

	def set_multiplier(self, clock_samp_mult: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:CLOCk:MULTiplier \n
		Snippet: driver.source.bb.nr5G.clock.set_multiplier(clock_samp_mult = 1) \n
		No command help available \n
			:param clock_samp_mult: No help available
		"""
		param = Conversions.decimal_value_to_str(clock_samp_mult)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:CLOCk:MULTiplier {param}')

	# noinspection PyTypeChecker
	def get_source(self) -> enums.ClockSourceC:
		"""SCPI: [SOURce<HW>]:BB:NR5G:CLOCk:SOURce \n
		Snippet: value: enums.ClockSourceC = driver.source.bb.nr5G.clock.get_source() \n
			INTRO_CMD_HELP: Selects the clock source: \n
			- INTernal: Internal clock reference \n
			:return: clock_source: INTernal
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:CLOCk:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.ClockSourceC)

	def set_source(self, clock_source: enums.ClockSourceC) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:CLOCk:SOURce \n
		Snippet: driver.source.bb.nr5G.clock.set_source(clock_source = enums.ClockSourceC.ELCLock) \n
			INTRO_CMD_HELP: Selects the clock source: \n
			- INTernal: Internal clock reference \n
			:param clock_source: INTernal
		"""
		param = Conversions.enum_scalar_to_str(clock_source, enums.ClockSourceC)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:CLOCk:SOURce {param}')
