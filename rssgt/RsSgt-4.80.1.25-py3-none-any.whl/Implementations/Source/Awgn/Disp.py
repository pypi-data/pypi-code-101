from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Disp:
	"""Disp commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("disp", core, parent)

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.NoisAwgnDispModeRfBb:
		"""SCPI: [SOURce<HW>]:AWGN:DISP:MODE \n
		Snippet: value: enums.NoisAwgnDispModeRfBb = driver.source.awgn.disp.get_mode() \n
		Selects the display mode to Bseband or RF. \n
			:return: mode: RF| BB
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:AWGN:DISP:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.NoisAwgnDispModeRfBb)

	# noinspection PyTypeChecker
	def get_oresults(self) -> enums.AnalogDigitalMode:
		"""SCPI: [SOURce<HW>]:AWGN:DISP:ORESults \n
		Snippet: value: enums.AnalogDigitalMode = driver.source.awgn.disp.get_oresults() \n
		(requires option R&S SGT-K18, Digital Baseband Connectivity) In additive Noise and Noise Only (SOUR:AWGN:MODE ADD|ONLY)
		modes and for Display Mode set to Baseband (AWGN:DISP:MODE BB) , selects the display of output results for the analog
		(DACIF) or the digital (BBOUT) signal path. \n
			:return: oresults: ANALog| DIGital
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:AWGN:DISP:ORESults?')
		return Conversions.str_to_scalar_enum(response, enums.AnalogDigitalMode)

	def set_oresults(self, oresults: enums.AnalogDigitalMode) -> None:
		"""SCPI: [SOURce<HW>]:AWGN:DISP:ORESults \n
		Snippet: driver.source.awgn.disp.set_oresults(oresults = enums.AnalogDigitalMode.ANALog) \n
		(requires option R&S SGT-K18, Digital Baseband Connectivity) In additive Noise and Noise Only (SOUR:AWGN:MODE ADD|ONLY)
		modes and for Display Mode set to Baseband (AWGN:DISP:MODE BB) , selects the display of output results for the analog
		(DACIF) or the digital (BBOUT) signal path. \n
			:param oresults: ANALog| DIGital
		"""
		param = Conversions.enum_scalar_to_str(oresults, enums.AnalogDigitalMode)
		self._core.io.write(f'SOURce<HwInstance>:AWGN:DISP:ORESults {param}')
