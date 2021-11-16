from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, use_spec_slot_idx: bool, output=repcap.Output.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TRIGger:OUTPut<CH>:SSC:USSidx:STATe \n
		Snippet: driver.source.bb.nr5G.trigger.output.ssc.ussIdx.state.set(use_spec_slot_idx = False, output = repcap.Output.Default) \n
		No command help available \n
			:param use_spec_slot_idx: No help available
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
		"""
		param = Conversions.bool_to_str(use_spec_slot_idx)
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:TRIGger:OUTPut{output_cmd_val}:SSC:USSidx:STATe {param}')

	def get(self, output=repcap.Output.Default) -> bool:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TRIGger:OUTPut<CH>:SSC:USSidx:STATe \n
		Snippet: value: bool = driver.source.bb.nr5G.trigger.output.ssc.ussIdx.state.get(output = repcap.Output.Default) \n
		No command help available \n
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
			:return: use_spec_slot_idx: No help available"""
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:TRIGger:OUTPut{output_cmd_val}:SSC:USSidx:STATe?')
		return Conversions.str_to_bool(response)
