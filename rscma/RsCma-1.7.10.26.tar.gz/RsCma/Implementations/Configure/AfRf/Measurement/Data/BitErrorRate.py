from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BitErrorRate:
	"""BitErrorRate commands group definition. 4 total commands, 0 Sub-groups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bitErrorRate", core, parent)

	# noinspection PyTypeChecker
	def get_source(self) -> enums.Source:
		"""SCPI: CONFigure:AFRF:MEASurement<Instance>:DATA:BERate:SOURce \n
		Snippet: value: enums.Source = driver.configure.afRf.measurement.data.bitErrorRate.get_source() \n
		Defines the input path for data to be analyzed. \n
			:return: source: TTLin
		"""
		response = self._core.io.query_str('CONFigure:AFRF:MEASurement<Instance>:DATA:BERate:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.Source)

	def set_source(self, source: enums.Source) -> None:
		"""SCPI: CONFigure:AFRF:MEASurement<Instance>:DATA:BERate:SOURce \n
		Snippet: driver.configure.afRf.measurement.data.bitErrorRate.set_source(source = enums.Source.TTLin) \n
		Defines the input path for data to be analyzed. \n
			:param source: TTLin
		"""
		param = Conversions.enum_scalar_to_str(source, enums.Source)
		self._core.io.write(f'CONFigure:AFRF:MEASurement<Instance>:DATA:BERate:SOURce {param}')

	# noinspection PyTypeChecker
	def get_pattern(self) -> enums.UserDefPattern:
		"""SCPI: CONFigure:AFRF:MEASurement<Instance>:DATA:BERate:PATTern \n
		Snippet: value: enums.UserDefPattern = driver.configure.afRf.measurement.data.bitErrorRate.get_pattern() \n
		Selects the bit pattern to be transmitted as payload. \n
			:return: pattern: PRBS6 | PRBS9
		"""
		response = self._core.io.query_str('CONFigure:AFRF:MEASurement<Instance>:DATA:BERate:PATTern?')
		return Conversions.str_to_scalar_enum(response, enums.UserDefPattern)

	def set_pattern(self, pattern: enums.UserDefPattern) -> None:
		"""SCPI: CONFigure:AFRF:MEASurement<Instance>:DATA:BERate:PATTern \n
		Snippet: driver.configure.afRf.measurement.data.bitErrorRate.set_pattern(pattern = enums.UserDefPattern.PRBS6) \n
		Selects the bit pattern to be transmitted as payload. \n
			:param pattern: PRBS6 | PRBS9
		"""
		param = Conversions.enum_scalar_to_str(pattern, enums.UserDefPattern)
		self._core.io.write(f'CONFigure:AFRF:MEASurement<Instance>:DATA:BERate:PATTern {param}')

	def get_drate(self) -> int:
		"""SCPI: CONFigure:AFRF:MEASurement<Instance>:DATA:BERate:DRATe \n
		Snippet: value: int = driver.configure.afRf.measurement.data.bitErrorRate.get_drate() \n
		The bit rate that is expected for the incoming data to be analyzed. \n
			:return: drate: Range: 0 bit/s to 115.2E+3 bit/s, Unit: bit/s
		"""
		response = self._core.io.query_str('CONFigure:AFRF:MEASurement<Instance>:DATA:BERate:DRATe?')
		return Conversions.str_to_int(response)

	def get_ibits(self) -> bool:
		"""SCPI: CONFigure:AFRF:MEASurement<Instance>:DATA:BERate:IBITs \n
		Snippet: value: bool = driver.configure.afRf.measurement.data.bitErrorRate.get_ibits() \n
		If set to ON, each 0 in the bit sequence is turned to 1 and vice versa. \n
			:return: invert_bits: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:AFRF:MEASurement<Instance>:DATA:BERate:IBITs?')
		return Conversions.str_to_bool(response)
