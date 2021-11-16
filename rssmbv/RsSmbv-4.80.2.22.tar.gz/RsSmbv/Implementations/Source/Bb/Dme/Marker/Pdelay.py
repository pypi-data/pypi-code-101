from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pdelay:
	"""Pdelay commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pdelay", core, parent)

	def get(self, marker=repcap.Marker.Default) -> float:
		"""SCPI: [SOURce<HW>]:[BB]:DME:MARKer<CH>:PDELay \n
		Snippet: value: float = driver.source.bb.dme.marker.pdelay.get(marker = repcap.Marker.Default) \n
		Queries the marker processing delay, internally measured value. This command is available only for DME:MARKer<ch>:MODE. \n
			:param marker: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Marker')
			:return: processed_delay: float Range: 0 to 1"""
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:DME:MARKer{marker_cmd_val}:PDELay?')
		return Conversions.str_to_float(response)
