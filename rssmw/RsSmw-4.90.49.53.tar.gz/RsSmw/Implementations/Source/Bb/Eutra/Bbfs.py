from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bbfs:
	"""Bbfs commands group definition. 4 total commands, 0 Sub-groups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bbfs", core, parent)

	def get_dtime(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:BBFS:DTIMe \n
		Snippet: value: float = driver.source.bb.eutra.bbfs.get_dtime() \n
		No command help available \n
			:return: dwell_time: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:BBFS:DTIMe?')
		return Conversions.str_to_float(response)

	def set_dtime(self, dwell_time: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:BBFS:DTIMe \n
		Snippet: driver.source.bb.eutra.bbfs.set_dtime(dwell_time = 1.0) \n
		No command help available \n
			:param dwell_time: No help available
		"""
		param = Conversions.decimal_value_to_str(dwell_time)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:BBFS:DTIMe {param}')

	def get_max_shift(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:BBFS:MAXShift \n
		Snippet: value: float = driver.source.bb.eutra.bbfs.get_max_shift() \n
		No command help available \n
			:return: max_shift: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:BBFS:MAXShift?')
		return Conversions.str_to_float(response)

	def set_max_shift(self, max_shift: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:BBFS:MAXShift \n
		Snippet: driver.source.bb.eutra.bbfs.set_max_shift(max_shift = 1.0) \n
		No command help available \n
			:param max_shift: No help available
		"""
		param = Conversions.decimal_value_to_str(max_shift)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:BBFS:MAXShift {param}')

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.EutraBbFreqSweepMode:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:BBFS:MODE \n
		Snippet: value: enums.EutraBbFreqSweepMode = driver.source.bb.eutra.bbfs.get_mode() \n
		No command help available \n
			:return: mode: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:BBFS:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.EutraBbFreqSweepMode)

	def set_mode(self, mode: enums.EutraBbFreqSweepMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:BBFS:MODE \n
		Snippet: driver.source.bb.eutra.bbfs.set_mode(mode = enums.EutraBbFreqSweepMode.AFTer) \n
		No command help available \n
			:param mode: No help available
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.EutraBbFreqSweepMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:BBFS:MODE {param}')

	def get_steps(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:BBFS:STEPs \n
		Snippet: value: int = driver.source.bb.eutra.bbfs.get_steps() \n
		No command help available \n
			:return: num_steps: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:EUTRa:BBFS:STEPs?')
		return Conversions.str_to_int(response)

	def set_steps(self, num_steps: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:BBFS:STEPs \n
		Snippet: driver.source.bb.eutra.bbfs.set_steps(num_steps = 1) \n
		No command help available \n
			:param num_steps: No help available
		"""
		param = Conversions.decimal_value_to_str(num_steps)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:BBFS:STEPs {param}')
