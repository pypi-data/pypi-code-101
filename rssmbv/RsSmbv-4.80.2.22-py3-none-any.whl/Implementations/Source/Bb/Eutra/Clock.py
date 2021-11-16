from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Clock:
	"""Clock commands group definition. 4 total commands, 0 Sub-groups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("clock", core, parent)

	def get_custom(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:CLOCk:CUSTom \n
		Snippet: value: int = driver.source.bb.eutra.clock.get_custom() \n
		No command help available \n
			:return: custom: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:CLOCk:CUSTom?')
		return Conversions.str_to_int(response)

	def set_custom(self, custom: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:CLOCk:CUSTom \n
		Snippet: driver.source.bb.eutra.clock.set_custom(custom = 1) \n
		No command help available \n
			:param custom: No help available
		"""
		param = Conversions.decimal_value_to_str(custom)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:CLOCk:CUSTom {param}')

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.EuTraClockMode:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:CLOCk:MODE \n
		Snippet: value: enums.EuTraClockMode = driver.source.bb.eutra.clock.get_mode() \n
		No command help available \n
			:return: mode: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:CLOCk:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.EuTraClockMode)

	def set_mode(self, mode: enums.EuTraClockMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:CLOCk:MODE \n
		Snippet: driver.source.bb.eutra.clock.set_mode(mode = enums.EuTraClockMode.CUSTom) \n
		No command help available \n
			:param mode: No help available
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.EuTraClockMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:CLOCk:MODE {param}')

	def get_multiplier(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:CLOCk:MULTiplier \n
		Snippet: value: int = driver.source.bb.eutra.clock.get_multiplier() \n
		No command help available \n
			:return: multiplier: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:CLOCk:MULTiplier?')
		return Conversions.str_to_int(response)

	def set_multiplier(self, multiplier: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:CLOCk:MULTiplier \n
		Snippet: driver.source.bb.eutra.clock.set_multiplier(multiplier = 1) \n
		No command help available \n
			:param multiplier: No help available
		"""
		param = Conversions.decimal_value_to_str(multiplier)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:CLOCk:MULTiplier {param}')

	# noinspection PyTypeChecker
	def get_source(self) -> enums.ClockSourceA:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:CLOCk:SOURce \n
		Snippet: value: enums.ClockSourceA = driver.source.bb.eutra.clock.get_source() \n
			INTRO_CMD_HELP: Selects the clock source: \n
			- INTernal: Internal clock reference \n
			:return: source: INTernal
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:CLOCk:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.ClockSourceA)

	def set_source(self, source: enums.ClockSourceA) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:CLOCk:SOURce \n
		Snippet: driver.source.bb.eutra.clock.set_source(source = enums.ClockSourceA.INTernal) \n
			INTRO_CMD_HELP: Selects the clock source: \n
			- INTernal: Internal clock reference \n
			:param source: INTernal
		"""
		param = Conversions.enum_scalar_to_str(source, enums.ClockSourceA)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:CLOCk:SOURce {param}')
