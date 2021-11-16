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
	def get_mode(self) -> enums.EuTraClockMode:
		"""SCPI: [SOURce<HW>]:BB:OFDM:CLOCk:MODE \n
		Snippet: value: enums.EuTraClockMode = driver.source.bb.ofdm.clock.get_mode() \n
		No command help available \n
			:return: clock_mode: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:OFDM:CLOCk:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.EuTraClockMode)

	def set_mode(self, clock_mode: enums.EuTraClockMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:OFDM:CLOCk:MODE \n
		Snippet: driver.source.bb.ofdm.clock.set_mode(clock_mode = enums.EuTraClockMode.CUSTom) \n
		No command help available \n
			:param clock_mode: No help available
		"""
		param = Conversions.enum_scalar_to_str(clock_mode, enums.EuTraClockMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:OFDM:CLOCk:MODE {param}')

	def get_multiplier(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:OFDM:CLOCk:MULTiplier \n
		Snippet: value: int = driver.source.bb.ofdm.clock.get_multiplier() \n
		No command help available \n
			:return: clock_samp_mult: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:OFDM:CLOCk:MULTiplier?')
		return Conversions.str_to_int(response)

	def set_multiplier(self, clock_samp_mult: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:OFDM:CLOCk:MULTiplier \n
		Snippet: driver.source.bb.ofdm.clock.set_multiplier(clock_samp_mult = 1) \n
		No command help available \n
			:param clock_samp_mult: No help available
		"""
		param = Conversions.decimal_value_to_str(clock_samp_mult)
		self._core.io.write(f'SOURce<HwInstance>:BB:OFDM:CLOCk:MULTiplier {param}')

	# noinspection PyTypeChecker
	def get_source(self) -> enums.ClockSourceA:
		"""SCPI: [SOURce<HW>]:BB:OFDM:CLOCk:SOURce \n
		Snippet: value: enums.ClockSourceA = driver.source.bb.ofdm.clock.get_source() \n
			INTRO_CMD_HELP: Selects the clock source: \n
			- INTernal: Internal clock reference \n
			:return: clock_source: INTernal
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:OFDM:CLOCk:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.ClockSourceA)

	def set_source(self, clock_source: enums.ClockSourceA) -> None:
		"""SCPI: [SOURce<HW>]:BB:OFDM:CLOCk:SOURce \n
		Snippet: driver.source.bb.ofdm.clock.set_source(clock_source = enums.ClockSourceA.INTernal) \n
			INTRO_CMD_HELP: Selects the clock source: \n
			- INTernal: Internal clock reference \n
			:param clock_source: INTernal
		"""
		param = Conversions.enum_scalar_to_str(clock_source, enums.ClockSourceA)
		self._core.io.write(f'SOURce<HwInstance>:BB:OFDM:CLOCk:SOURce {param}')
