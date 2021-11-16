from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rdelay:
	"""Rdelay commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rdelay", core, parent)

	def get(self, external=repcap.External.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TRIGger:EXTernal<CH>:RDELay \n
		Snippet: value: float = driver.source.bb.eutra.trigger.external.rdelay.get(external = repcap.External.Default) \n
		Queries the time (in seconds) of an external trigger event is delayed for. \n
			:param external: optional repeated capability selector. Default value: Nr1 (settable in the interface 'External')
			:return: ext_result_delay: float Range: 0 to 688"""
		external_cmd_val = self._cmd_group.get_repcap_cmd_value(external, repcap.External)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:TRIGger:EXTernal{external_cmd_val}:RDELay?')
		return Conversions.str_to_float(response)
