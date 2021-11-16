from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PointA:
	"""PointA commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pointA", core, parent)

	def set(self, lte_offs_to_point_a: int, cellNull=repcap.CellNull.Nr0) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CELL<CH0>:LTE:POINta \n
		Snippet: driver.source.bb.nr5G.node.cell.lte.pointA.set(lte_offs_to_point_a = 1, cellNull = repcap.CellNull.Nr0) \n
		Sets the LTE carrier center subcarrier location. \n
			:param lte_offs_to_point_a: integer Range: 0 to 30300
			:param cellNull: optional repeated capability selector. Default value: Nr0
		"""
		param = Conversions.decimal_value_to_str(lte_offs_to_point_a)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:NODE:CELL{cellNull_cmd_val}:LTE:POINta {param}')

	def get(self, cellNull=repcap.CellNull.Nr0) -> int:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CELL<CH0>:LTE:POINta \n
		Snippet: value: int = driver.source.bb.nr5G.node.cell.lte.pointA.get(cellNull = repcap.CellNull.Nr0) \n
		Sets the LTE carrier center subcarrier location. \n
			:param cellNull: optional repeated capability selector. Default value: Nr0
			:return: lte_offs_to_point_a: integer Range: 0 to 30300"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:NODE:CELL{cellNull_cmd_val}:LTE:POINta?')
		return Conversions.str_to_int(response)
