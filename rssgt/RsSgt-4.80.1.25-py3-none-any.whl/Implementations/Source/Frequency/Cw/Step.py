from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Step:
	"""Step commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("step", core, parent)

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.FreqStepMode:
		"""SCPI: [SOURce<HW>]:FREQuency:[CW]:STEP:MODE \n
		Snippet: value: enums.FreqStepMode = driver.source.frequency.cw.step.get_mode() \n
		No command help available \n
			:return: freq_step_mode: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FREQuency:CW:STEP:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.FreqStepMode)

	def set_mode(self, freq_step_mode: enums.FreqStepMode) -> None:
		"""SCPI: [SOURce<HW>]:FREQuency:[CW]:STEP:MODE \n
		Snippet: driver.source.frequency.cw.step.set_mode(freq_step_mode = enums.FreqStepMode.DECimal) \n
		No command help available \n
			:param freq_step_mode: No help available
		"""
		param = Conversions.enum_scalar_to_str(freq_step_mode, enums.FreqStepMode)
		self._core.io.write(f'SOURce<HwInstance>:FREQuency:CW:STEP:MODE {param}')

	def get_increment(self) -> float:
		"""SCPI: [SOURce<HW>]:FREQuency:[CW]:STEP:[INCRement] \n
		Snippet: value: float = driver.source.frequency.cw.step.get_increment() \n
		No command help available \n
			:return: freq_step: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FREQuency:CW:STEP:INCRement?')
		return Conversions.str_to_float(response)

	def set_increment(self, freq_step: float) -> None:
		"""SCPI: [SOURce<HW>]:FREQuency:[CW]:STEP:[INCRement] \n
		Snippet: driver.source.frequency.cw.step.set_increment(freq_step = 1.0) \n
		No command help available \n
			:param freq_step: No help available
		"""
		param = Conversions.decimal_value_to_str(freq_step)
		self._core.io.write(f'SOURce<HwInstance>:FREQuency:CW:STEP:INCRement {param}')
