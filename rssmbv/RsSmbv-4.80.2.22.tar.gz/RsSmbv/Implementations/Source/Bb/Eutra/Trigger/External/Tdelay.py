from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tdelay:
	"""Tdelay commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tdelay", core, parent)

	def set(self, delay: float, external=repcap.External.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TRIGger:EXTernal<CH>:TDELay \n
		Snippet: driver.source.bb.eutra.trigger.external.tdelay.set(delay = 1.0, external = repcap.External.Default) \n
		Specifies the trigger delay for external triggering. The value affects all external trigger signals. \n
			:param delay: float Range: 0 to 688, Unit: s
			:param external: optional repeated capability selector. Default value: Nr1 (settable in the interface 'External')
		"""
		param = Conversions.decimal_value_to_str(delay)
		external_cmd_val = self._cmd_group.get_repcap_cmd_value(external, repcap.External)
		self._core.io.write(f'SOURce<HwInstance>:BB:EUTRa:TRIGger:EXTernal{external_cmd_val}:TDELay {param}')

	def get(self, external=repcap.External.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:EUTRa:TRIGger:EXTernal<CH>:TDELay \n
		Snippet: value: float = driver.source.bb.eutra.trigger.external.tdelay.get(external = repcap.External.Default) \n
		Specifies the trigger delay for external triggering. The value affects all external trigger signals. \n
			:param external: optional repeated capability selector. Default value: Nr1 (settable in the interface 'External')
			:return: delay: float Range: 0 to 688, Unit: s"""
		external_cmd_val = self._cmd_group.get_repcap_cmd_value(external, repcap.External)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:EUTRa:TRIGger:EXTernal{external_cmd_val}:TDELay?')
		return Conversions.str_to_float(response)
