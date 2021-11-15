from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NulSymbols:
	"""NulSymbols commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nulSymbols", core, parent)

	def set(self, ul_symbols: int, output=repcap.Output.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TRIGger:OUTPut<CH>:SSC:NULSymbols \n
		Snippet: driver.source.bb.nr5G.trigger.output.ssc.nulSymbols.set(ul_symbols = 1, output = repcap.Output.Default) \n
		Queries the number of UL symbols in the special slot of a UL/DL pattern containing a marker. \n
			:param ul_symbols: integer Range: 0 to 14
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
		"""
		param = Conversions.decimal_value_to_str(ul_symbols)
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:TRIGger:OUTPut{output_cmd_val}:SSC:NULSymbols {param}')

	def get(self, output=repcap.Output.Default) -> int:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TRIGger:OUTPut<CH>:SSC:NULSymbols \n
		Snippet: value: int = driver.source.bb.nr5G.trigger.output.ssc.nulSymbols.get(output = repcap.Output.Default) \n
		Queries the number of UL symbols in the special slot of a UL/DL pattern containing a marker. \n
			:param output: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
			:return: ul_symbols: integer Range: 0 to 14"""
		output_cmd_val = self._cmd_group.get_repcap_cmd_value(output, repcap.Output)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:TRIGger:OUTPut{output_cmd_val}:SSC:NULSymbols?')
		return Conversions.str_to_int(response)
