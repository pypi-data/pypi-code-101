from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mue:
	"""Mue commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mue", core, parent)

	def get_tsrs(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TCW:MUE:TSRS \n
		Snippet: value: bool = driver.source.bb.nr5G.tcw.mue.get_tsrs() \n
		No command help available \n
			:return: transmit_srs: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:TCW:MUE:TSRS?')
		return Conversions.str_to_bool(response)

	def set_tsrs(self, transmit_srs: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TCW:MUE:TSRS \n
		Snippet: driver.source.bb.nr5G.tcw.mue.set_tsrs(transmit_srs = False) \n
		No command help available \n
			:param transmit_srs: No help available
		"""
		param = Conversions.bool_to_str(transmit_srs)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:TCW:MUE:TSRS {param}')
