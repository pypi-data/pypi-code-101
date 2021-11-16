from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bandpass:
	"""Bandpass commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bandpass", core, parent)

	def get_bandwidth(self) -> float:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQRecorder:FILTer:BANDpass:BWIDth \n
		Snippet: value: float = driver.configure.gprf.measurement.iqRecorder.filterPy.bandpass.get_bandwidth() \n
		Selects the bandwidth for a bandpass filter. \n
			:return: bandpass_bw: Only the following values can be configured: IF unit: 31.25 MHz, 62.5 MHz, 125 MHz, 250 MHz, 500 MHz, 1000 MHz R&S CMW: 1 kHz, 10 kHz, 100 kHz, 1 MHz, 10 MHz, 40 MHz, 160 MHz Other values are rounded to the next allowed value.
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:IQRecorder:FILTer:BANDpass:BWIDth?')
		return Conversions.str_to_float(response)

	def set_bandwidth(self, bandpass_bw: float) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQRecorder:FILTer:BANDpass:BWIDth \n
		Snippet: driver.configure.gprf.measurement.iqRecorder.filterPy.bandpass.set_bandwidth(bandpass_bw = 1.0) \n
		Selects the bandwidth for a bandpass filter. \n
			:param bandpass_bw: Only the following values can be configured: IF unit: 31.25 MHz, 62.5 MHz, 125 MHz, 250 MHz, 500 MHz, 1000 MHz R&S CMW: 1 kHz, 10 kHz, 100 kHz, 1 MHz, 10 MHz, 40 MHz, 160 MHz Other values are rounded to the next allowed value.
		"""
		param = Conversions.decimal_value_to_str(bandpass_bw)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:IQRecorder:FILTer:BANDpass:BWIDth {param}')
