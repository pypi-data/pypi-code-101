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

	def get_divider(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:GSM:CLOCk:DIVider \n
		Snippet: value: int = driver.source.bb.gsm.clock.get_divider() \n
		No command help available \n
			:return: divider: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GSM:CLOCk:DIVider?')
		return Conversions.str_to_int(response)

	def set_divider(self, divider: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:GSM:CLOCk:DIVider \n
		Snippet: driver.source.bb.gsm.clock.set_divider(divider = 1) \n
		No command help available \n
			:param divider: No help available
		"""
		param = Conversions.decimal_value_to_str(divider)
		self._core.io.write(f'SOURce<HwInstance>:BB:GSM:CLOCk:DIVider {param}')

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.ClocMode:
		"""SCPI: [SOURce<HW>]:BB:GSM:CLOCk:MODE \n
		Snippet: value: enums.ClocMode = driver.source.bb.gsm.clock.get_mode() \n
		No command help available \n
			:return: mode: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GSM:CLOCk:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.ClocMode)

	def set_mode(self, mode: enums.ClocMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:GSM:CLOCk:MODE \n
		Snippet: driver.source.bb.gsm.clock.set_mode(mode = enums.ClocMode.BIT) \n
		No command help available \n
			:param mode: No help available
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.ClocMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:GSM:CLOCk:MODE {param}')

	def get_multiplier(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:GSM:CLOCk:MULTiplier \n
		Snippet: value: int = driver.source.bb.gsm.clock.get_multiplier() \n
		No command help available \n
			:return: multiplier: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GSM:CLOCk:MULTiplier?')
		return Conversions.str_to_int(response)

	def set_multiplier(self, multiplier: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:GSM:CLOCk:MULTiplier \n
		Snippet: driver.source.bb.gsm.clock.set_multiplier(multiplier = 1) \n
		No command help available \n
			:param multiplier: No help available
		"""
		param = Conversions.decimal_value_to_str(multiplier)
		self._core.io.write(f'SOURce<HwInstance>:BB:GSM:CLOCk:MULTiplier {param}')

	# noinspection PyTypeChecker
	def get_source(self) -> enums.ClockSourceA:
		"""SCPI: [SOURce<HW>]:BB:GSM:CLOCk:SOURce \n
		Snippet: value: enums.ClockSourceA = driver.source.bb.gsm.clock.get_source() \n
			INTRO_CMD_HELP: Selects the clock source: \n
			- INTernal: Internal clock reference \n
			:return: source: INTernal
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:GSM:CLOCk:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.ClockSourceA)

	def set_source(self, source: enums.ClockSourceA) -> None:
		"""SCPI: [SOURce<HW>]:BB:GSM:CLOCk:SOURce \n
		Snippet: driver.source.bb.gsm.clock.set_source(source = enums.ClockSourceA.INTernal) \n
			INTRO_CMD_HELP: Selects the clock source: \n
			- INTernal: Internal clock reference \n
			:param source: INTernal
		"""
		param = Conversions.enum_scalar_to_str(source, enums.ClockSourceA)
		self._core.io.write(f'SOURce<HwInstance>:BB:GSM:CLOCk:SOURce {param}')
