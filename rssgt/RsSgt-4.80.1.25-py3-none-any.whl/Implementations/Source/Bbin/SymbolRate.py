from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SymbolRate:
	"""SymbolRate commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("symbolRate", core, parent)

	# noinspection PyTypeChecker
	def get_source(self) -> enums.BbinSampRateMode:
		"""SCPI: [SOURce<HW>]:BBIN:SRATe:SOURce \n
		Snippet: value: enums.BbinSampRateMode = driver.source.bbin.symbolRate.get_source() \n
		Queries the source for estimating the sample rate of the digital input signal or defining it by the user. \n
			:return: source: USER| DIN
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BBIN:SRATe:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.BbinSampRateMode)

	def set_source(self, source: enums.BbinSampRateMode) -> None:
		"""SCPI: [SOURce<HW>]:BBIN:SRATe:SOURce \n
		Snippet: driver.source.bbin.symbolRate.set_source(source = enums.BbinSampRateMode.DIN) \n
		Queries the source for estimating the sample rate of the digital input signal or defining it by the user. \n
			:param source: USER| DIN
		"""
		param = Conversions.enum_scalar_to_str(source, enums.BbinSampRateMode)
		self._core.io.write(f'SOURce<HwInstance>:BBIN:SRATe:SOURce {param}')

	def get_actual(self) -> float:
		"""SCPI: [SOURce<HW>]:BBIN:SRATe:[ACTual] \n
		Snippet: value: float = driver.source.bbin.symbolRate.get_actual() \n
		Sets the sample rate of the external digital baseband signal. \n
			:return: actual: float Range: 25E6 to 250E6
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BBIN:SRATe:ACTual?')
		return Conversions.str_to_float(response)

	def set_actual(self, actual: float) -> None:
		"""SCPI: [SOURce<HW>]:BBIN:SRATe:[ACTual] \n
		Snippet: driver.source.bbin.symbolRate.set_actual(actual = 1.0) \n
		Sets the sample rate of the external digital baseband signal. \n
			:param actual: float Range: 25E6 to 250E6
		"""
		param = Conversions.decimal_value_to_str(actual)
		self._core.io.write(f'SOURce<HwInstance>:BBIN:SRATe:ACTual {param}')
