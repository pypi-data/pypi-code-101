from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Vshift:
	"""Vshift commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("vshift", core, parent)

	def set(self, lte_vshift: int, cellNull=repcap.CellNull.Nr0) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CELL<CH0>:LTE:VSHift \n
		Snippet: driver.source.bb.nr5G.node.cell.lte.vshift.set(lte_vshift = 1, cellNull = repcap.CellNull.Nr0) \n
		Sets the parameter v-Shift. \n
			:param lte_vshift: integer Range: 0 to 5
			:param cellNull: optional repeated capability selector. Default value: Nr0
		"""
		param = Conversions.decimal_value_to_str(lte_vshift)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:NODE:CELL{cellNull_cmd_val}:LTE:VSHift {param}')

	def get(self, cellNull=repcap.CellNull.Nr0) -> int:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CELL<CH0>:LTE:VSHift \n
		Snippet: value: int = driver.source.bb.nr5G.node.cell.lte.vshift.get(cellNull = repcap.CellNull.Nr0) \n
		Sets the parameter v-Shift. \n
			:param cellNull: optional repeated capability selector. Default value: Nr0
			:return: lte_vshift: integer Range: 0 to 5"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:NODE:CELL{cellNull_cmd_val}:LTE:VSHift?')
		return Conversions.str_to_int(response)
