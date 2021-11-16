from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool, stream=repcap.Stream.Default) -> None:
		"""SCPI: SCONfiguration:OUTPut:MAPPing:DIGital:STReam<ST>:STATe \n
		Snippet: driver.sconfiguration.output.mapping.digital.stream.state.set(state = False, stream = repcap.Stream.Default) \n
		Maps the I/Q output streams to the output connectors. \n
			:param state: 0| 1| OFF| ON
			:param stream: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Stream')
		"""
		param = Conversions.bool_to_str(state)
		stream_cmd_val = self._cmd_group.get_repcap_cmd_value(stream, repcap.Stream)
		self._core.io.write(f'SCONfiguration:OUTPut:MAPPing:DIGital:STReam{stream_cmd_val}:STATe {param}')

	def get(self, stream=repcap.Stream.Default) -> bool:
		"""SCPI: SCONfiguration:OUTPut:MAPPing:DIGital:STReam<ST>:STATe \n
		Snippet: value: bool = driver.sconfiguration.output.mapping.digital.stream.state.get(stream = repcap.Stream.Default) \n
		Maps the I/Q output streams to the output connectors. \n
			:param stream: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Stream')
			:return: state: 0| 1| OFF| ON"""
		stream_cmd_val = self._cmd_group.get_repcap_cmd_value(stream, repcap.Stream)
		response = self._core.io.query_str(f'SCONfiguration:OUTPut:MAPPing:DIGital:STReam{stream_cmd_val}:STATe?')
		return Conversions.str_to_bool(response)
