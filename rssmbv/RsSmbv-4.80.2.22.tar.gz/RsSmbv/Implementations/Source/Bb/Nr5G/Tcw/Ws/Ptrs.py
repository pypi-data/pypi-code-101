from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ptrs:
	"""Ptrs commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ptrs", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TCW:WS:PTRS:STATe \n
		Snippet: value: bool = driver.source.bb.nr5G.tcw.ws.ptrs.get_state() \n
		No command help available \n
			:return: ptrs: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:TCW:WS:PTRS:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, ptrs: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:TCW:WS:PTRS:STATe \n
		Snippet: driver.source.bb.nr5G.tcw.ws.ptrs.set_state(ptrs = False) \n
		No command help available \n
			:param ptrs: No help available
		"""
		param = Conversions.bool_to_str(ptrs)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:TCW:WS:PTRS:STATe {param}')
