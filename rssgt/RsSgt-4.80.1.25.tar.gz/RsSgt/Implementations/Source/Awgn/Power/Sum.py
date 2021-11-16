from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sum:
	"""Sum commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sum", core, parent)

	def get_pep(self) -> float:
		"""SCPI: [SOURce<HW>]:AWGN:POWer:SUM:PEP \n
		Snippet: value: float = driver.source.awgn.power.sum.get_pep() \n
		In Additive Noise and CW Interferer (SOUR:AWGN:MODE ADD|CW) modes, queries the peak envelope power of the overall signal
		comprised of noise signal plus useful signal. \n
			:return: pep: float Range: -145 to 20
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:AWGN:POWer:SUM:PEP?')
		return Conversions.str_to_float(response)

	def get_value(self) -> float:
		"""SCPI: [SOURce<HW>]:AWGN:POWer:SUM \n
		Snippet: value: float = driver.source.awgn.power.sum.get_value() \n
		In Additive Noise and CW Interferer (SOUR:AWGN:MODE ADD|CW) modes, queries the overall power of the noise signal plus
		useful signal. \n
			:return: sum: float Range: -145 to 20
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:AWGN:POWer:SUM?')
		return Conversions.str_to_float(response)
