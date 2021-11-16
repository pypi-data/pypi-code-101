from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Relative:
	"""Relative commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("relative", core, parent)

	def set(self, bw_pct: float, notchFilter=repcap.NotchFilter.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:OFDM:NOTCh<CH>:BWIDth:RELative \n
		Snippet: driver.source.bb.ofdm.notch.bandwidth.relative.set(bw_pct = 1.0, notchFilter = repcap.NotchFilter.Default) \n
		No command help available \n
			:param bw_pct: No help available
			:param notchFilter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Notch')
		"""
		param = Conversions.decimal_value_to_str(bw_pct)
		notchFilter_cmd_val = self._cmd_group.get_repcap_cmd_value(notchFilter, repcap.NotchFilter)
		self._core.io.write(f'SOURce<HwInstance>:BB:OFDM:NOTCh{notchFilter_cmd_val}:BWIDth:RELative {param}')

	def get(self, notchFilter=repcap.NotchFilter.Default) -> float:
		"""SCPI: [SOURce<HW>]:BB:OFDM:NOTCh<CH>:BWIDth:RELative \n
		Snippet: value: float = driver.source.bb.ofdm.notch.bandwidth.relative.get(notchFilter = repcap.NotchFilter.Default) \n
		No command help available \n
			:param notchFilter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Notch')
			:return: bw_pct: No help available"""
		notchFilter_cmd_val = self._cmd_group.get_repcap_cmd_value(notchFilter, repcap.NotchFilter)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:OFDM:NOTCh{notchFilter_cmd_val}:BWIDth:RELative?')
		return Conversions.str_to_float(response)
