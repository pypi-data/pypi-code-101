from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Utilities import trim_str_response
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Generator:
	"""Generator commands group definition. 5 total commands, 0 Sub-groups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("generator", core, parent)

	def get_arbitrary(self) -> str:
		"""SCPI: TEST:BB:GENerator:ARBitrary \n
		Snippet: value: str = driver.test.bb.generator.get_arbitrary() \n
		No command help available \n
			:return: filename: No help available
		"""
		response = self._core.io.query_str('TEST:BB:GENerator:ARBitrary?')
		return trim_str_response(response)

	def set_arbitrary(self, filename: str) -> None:
		"""SCPI: TEST:BB:GENerator:ARBitrary \n
		Snippet: driver.test.bb.generator.set_arbitrary(filename = '1') \n
		No command help available \n
			:param filename: No help available
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'TEST:BB:GENerator:ARBitrary {param}')

	def get_frequency(self) -> float:
		"""SCPI: TEST:BB:GENerator:FREQuency \n
		Snippet: value: float = driver.test.bb.generator.get_frequency() \n
		No command help available \n
			:return: frequency: No help available
		"""
		response = self._core.io.query_str('TEST:BB:GENerator:FREQuency?')
		return Conversions.str_to_float(response)

	def set_frequency(self, frequency: float) -> None:
		"""SCPI: TEST:BB:GENerator:FREQuency \n
		Snippet: driver.test.bb.generator.set_frequency(frequency = 1.0) \n
		No command help available \n
			:param frequency: No help available
		"""
		param = Conversions.decimal_value_to_str(frequency)
		self._core.io.write(f'TEST:BB:GENerator:FREQuency {param}')

	def get_gain(self) -> float:
		"""SCPI: TEST:BB:GENerator:GAIN \n
		Snippet: value: float = driver.test.bb.generator.get_gain() \n
		No command help available \n
			:return: gain: No help available
		"""
		response = self._core.io.query_str('TEST:BB:GENerator:GAIN?')
		return Conversions.str_to_float(response)

	def set_gain(self, gain: float) -> None:
		"""SCPI: TEST:BB:GENerator:GAIN \n
		Snippet: driver.test.bb.generator.set_gain(gain = 1.0) \n
		No command help available \n
			:param gain: No help available
		"""
		param = Conversions.decimal_value_to_str(gain)
		self._core.io.write(f'TEST:BB:GENerator:GAIN {param}')

	# noinspection PyTypeChecker
	def get_source(self) -> enums.TestBbGenIqSour:
		"""SCPI: TEST:BB:GENerator:SOURce \n
		Snippet: value: enums.TestBbGenIqSour = driver.test.bb.generator.get_source() \n
		No command help available \n
			:return: iq_source: No help available
		"""
		response = self._core.io.query_str('TEST:BB:GENerator:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.TestBbGenIqSour)

	def set_source(self, iq_source: enums.TestBbGenIqSour) -> None:
		"""SCPI: TEST:BB:GENerator:SOURce \n
		Snippet: driver.test.bb.generator.set_source(iq_source = enums.TestBbGenIqSour.ARB) \n
		No command help available \n
			:param iq_source: No help available
		"""
		param = Conversions.enum_scalar_to_str(iq_source, enums.TestBbGenIqSour)
		self._core.io.write(f'TEST:BB:GENerator:SOURce {param}')

	def get_state(self) -> bool:
		"""SCPI: TEST:BB:GENerator:STATe \n
		Snippet: value: bool = driver.test.bb.generator.get_state() \n
		No command help available \n
			:return: state: No help available
		"""
		response = self._core.io.query_str('TEST:BB:GENerator:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: TEST:BB:GENerator:STATe \n
		Snippet: driver.test.bb.generator.set_state(state = False) \n
		No command help available \n
			:param state: No help available
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'TEST:BB:GENerator:STATe {param}')
