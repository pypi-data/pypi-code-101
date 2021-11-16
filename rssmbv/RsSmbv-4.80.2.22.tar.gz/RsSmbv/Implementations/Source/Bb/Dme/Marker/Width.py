from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Width:
	"""Width commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("width", core, parent)

	def set(self, width: int, marker=repcap.Marker.Default) -> None:
		"""SCPI: [SOURce<HW>]:[BB]:DME:MARKer<CH>:WIDTh \n
		Snippet: driver.source.bb.dme.marker.width.set(width = 1, marker = repcap.Marker.Default) \n
		Sets the width of the corresponding marker in chips (0.05us) . \n
			:param width: integer Range: 1 to 127
			:param marker: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Marker')
		"""
		param = Conversions.decimal_value_to_str(width)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		self._core.io.write(f'SOURce<HwInstance>:BB:DME:MARKer{marker_cmd_val}:WIDTh {param}')

	def get(self, marker=repcap.Marker.Default) -> int:
		"""SCPI: [SOURce<HW>]:[BB]:DME:MARKer<CH>:WIDTh \n
		Snippet: value: int = driver.source.bb.dme.marker.width.get(marker = repcap.Marker.Default) \n
		Sets the width of the corresponding marker in chips (0.05us) . \n
			:param marker: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Marker')
			:return: width: integer Range: 1 to 127"""
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:DME:MARKer{marker_cmd_val}:WIDTh?')
		return Conversions.str_to_int(response)
