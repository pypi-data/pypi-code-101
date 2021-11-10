from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Source:
	"""Source commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("source", core, parent)

	# noinspection PyTypeChecker
	def get(self, audioOutput=repcap.AudioOutput.Default) -> enums.AudioSource:
		"""SCPI: CONFigure:AFRF:MEASurement<Instance>:AOUT<nr>:SOURce \n
		Snippet: value: enums.AudioSource = driver.configure.afRf.measurement.audioOutput.source.get(audioOutput = repcap.AudioOutput.Default) \n
		Queries the audio signal source for an AF OUT connector. \n
			:param audioOutput: optional repeated capability selector. Default value: Nr1 (settable in the interface 'AudioOutput')
			:return: source: DEM | DEML | DEMR DEM Demodulator output (FM, PM, ...) DEML Demodulator output, left channel (FM stereo) DEMR Demodulator output, right channel (FM stereo)"""
		audioOutput_cmd_val = self._cmd_group.get_repcap_cmd_value(audioOutput, repcap.AudioOutput)
		response = self._core.io.query_str(f'CONFigure:AFRF:MEASurement<Instance>:AOUT{audioOutput_cmd_val}:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.AudioSource)
