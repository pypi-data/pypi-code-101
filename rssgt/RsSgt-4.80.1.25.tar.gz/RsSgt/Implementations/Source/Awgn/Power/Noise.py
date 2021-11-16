from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Noise:
	"""Noise commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("noise", core, parent)

	def get_total(self) -> float:
		"""SCPI: [SOURce<HW>]:AWGN:POWer:NOISe:TOTal \n
		Snippet: value: float = driver.source.awgn.power.noise.get_total() \n
		In Additive Noise and CW Interferer (SOUR:AWGN:MODE ADD|CW) modes, queries the noise power in the total bandwidth. Tip:
		Use the command AWGN:DISP:ORESults to define the analog or digital signal path before. \n
			:return: total: float Range: -145 to 20
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:AWGN:POWer:NOISe:TOTal?')
		return Conversions.str_to_float(response)

	def get_value(self) -> float:
		"""SCPI: [SOURce<HW>]:AWGN:POWer:NOISe \n
		Snippet: value: float = driver.source.awgn.power.noise.get_value() \n
			INTRO_CMD_HELP: Sets or queries the noise power in the system bandwidth depending on the selected mode: \n
			- SOUR:AWGN:MODE ADD|CW
			- 'Noise Only' mode The command sets the noise power. \n
			:return: noise: float Unit: dBm
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:AWGN:POWer:NOISe?')
		return Conversions.str_to_float(response)

	def set_value(self, noise: float) -> None:
		"""SCPI: [SOURce<HW>]:AWGN:POWer:NOISe \n
		Snippet: driver.source.awgn.power.noise.set_value(noise = 1.0) \n
			INTRO_CMD_HELP: Sets or queries the noise power in the system bandwidth depending on the selected mode: \n
			- SOUR:AWGN:MODE ADD|CW
			- 'Noise Only' mode The command sets the noise power. \n
			:param noise: float Unit: dBm
		"""
		param = Conversions.decimal_value_to_str(noise)
		self._core.io.write(f'SOURce<HwInstance>:AWGN:POWer:NOISe {param}')
