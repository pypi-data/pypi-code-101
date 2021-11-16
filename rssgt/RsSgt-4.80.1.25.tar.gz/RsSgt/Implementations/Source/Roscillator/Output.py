from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Output:
	"""Output commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("output", core, parent)

	# noinspection PyTypeChecker
	def get_frequency(self) -> enums.RoscFreqExt:
		"""SCPI: [SOURce<HW>]:ROSCillator:OUTPut:FREQuency \n
		Snippet: value: enums.RoscFreqExt = driver.source.roscillator.output.get_frequency() \n
		Selects the output for the reference oscillator signal. \n
			:return: output_freq: 10MHZ| 100MHZ| 1000MHZ| 13MHZ 13MHZ requires RF board with part number 1419.5308.02.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:ROSCillator:OUTPut:FREQuency?')
		return Conversions.str_to_scalar_enum(response, enums.RoscFreqExt)

	def set_frequency(self, output_freq: enums.RoscFreqExt) -> None:
		"""SCPI: [SOURce<HW>]:ROSCillator:OUTPut:FREQuency \n
		Snippet: driver.source.roscillator.output.set_frequency(output_freq = enums.RoscFreqExt._1000MHZ) \n
		Selects the output for the reference oscillator signal. \n
			:param output_freq: 10MHZ| 100MHZ| 1000MHZ| 13MHZ 13MHZ requires RF board with part number 1419.5308.02.
		"""
		param = Conversions.enum_scalar_to_str(output_freq, enums.RoscFreqExt)
		self._core.io.write(f'SOURce<HwInstance>:ROSCillator:OUTPut:FREQuency {param}')
