from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cbw:
	"""Cbw commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cbw", core, parent)

	def set(self, lte_carrier_bw: enums.LteCrsCarrierBwAll, cellNull=repcap.CellNull.Nr0) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CELL<CH0>:LTE:CBW \n
		Snippet: driver.source.bb.nr5G.node.cell.lte.cbw.set(lte_carrier_bw = enums.LteCrsCarrierBwAll.N100, cellNull = repcap.CellNull.Nr0) \n
		Sets the LTE bandwidth. \n
			:param lte_carrier_bw: N6| N15| N25| N50| N75| N100
			:param cellNull: optional repeated capability selector. Default value: Nr0
		"""
		param = Conversions.enum_scalar_to_str(lte_carrier_bw, enums.LteCrsCarrierBwAll)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:NODE:CELL{cellNull_cmd_val}:LTE:CBW {param}')

	# noinspection PyTypeChecker
	def get(self, cellNull=repcap.CellNull.Nr0) -> enums.LteCrsCarrierBwAll:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CELL<CH0>:LTE:CBW \n
		Snippet: value: enums.LteCrsCarrierBwAll = driver.source.bb.nr5G.node.cell.lte.cbw.get(cellNull = repcap.CellNull.Nr0) \n
		Sets the LTE bandwidth. \n
			:param cellNull: optional repeated capability selector. Default value: Nr0
			:return: lte_carrier_bw: N6| N15| N25| N50| N75| N100"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:NODE:CELL{cellNull_cmd_val}:LTE:CBW?')
		return Conversions.str_to_scalar_enum(response, enums.LteCrsCarrierBwAll)
