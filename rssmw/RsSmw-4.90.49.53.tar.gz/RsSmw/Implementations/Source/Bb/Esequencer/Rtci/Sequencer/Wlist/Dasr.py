from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dasr:
	"""Dasr commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dasr", core, parent)

	def set(self, streaming_rate: enums.ExtSeqPdwRate, sequencer=repcap.Sequencer.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:ESEQuencer:RTCI:[SEQuencer<ST>]:WLISt:DASR \n
		Snippet: driver.source.bb.esequencer.rtci.sequencer.wlist.dasr.set(streaming_rate = enums.ExtSeqPdwRate.SR1M, sequencer = repcap.Sequencer.Default) \n
		The desired ARB Streaming rate directly influences the Minimum common clock rate all waveforms are resampled to.
		The higher the desired rate, the higher the common sample rate, in order to optimize the ARB PDW Streaming rate. At the
		same time, the required Memory will also increase. \n
			:param streaming_rate: SR250K| SR750K| SR500K| SR1M
			:param sequencer: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sequencer')
		"""
		param = Conversions.enum_scalar_to_str(streaming_rate, enums.ExtSeqPdwRate)
		sequencer_cmd_val = self._cmd_group.get_repcap_cmd_value(sequencer, repcap.Sequencer)
		self._core.io.write(f'SOURce<HwInstance>:BB:ESEQuencer:RTCI:SEQuencer{sequencer_cmd_val}:WLISt:DASR {param}')

	# noinspection PyTypeChecker
	def get(self, sequencer=repcap.Sequencer.Default) -> enums.ExtSeqPdwRate:
		"""SCPI: [SOURce<HW>]:BB:ESEQuencer:RTCI:[SEQuencer<ST>]:WLISt:DASR \n
		Snippet: value: enums.ExtSeqPdwRate = driver.source.bb.esequencer.rtci.sequencer.wlist.dasr.get(sequencer = repcap.Sequencer.Default) \n
		The desired ARB Streaming rate directly influences the Minimum common clock rate all waveforms are resampled to.
		The higher the desired rate, the higher the common sample rate, in order to optimize the ARB PDW Streaming rate. At the
		same time, the required Memory will also increase. \n
			:param sequencer: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sequencer')
			:return: streaming_rate: SR250K| SR750K| SR500K| SR1M"""
		sequencer_cmd_val = self._cmd_group.get_repcap_cmd_value(sequencer, repcap.Sequencer)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:ESEQuencer:RTCI:SEQuencer{sequencer_cmd_val}:WLISt:DASR?')
		return Conversions.str_to_scalar_enum(response, enums.ExtSeqPdwRate)
