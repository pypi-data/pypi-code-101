from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Nap:
	"""Nap commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nap", core, parent)

	def set(self, lte_antenna_ports: enums.NumberOfPorts, cellNull=repcap.CellNull.Nr0) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CELL<CH0>:LTE:NAP \n
		Snippet: driver.source.bb.nr5G.node.cell.lte.nap.set(lte_antenna_ports = enums.NumberOfPorts.AP1, cellNull = repcap.CellNull.Nr0) \n
		Sets the number of antenna ports used for LTE-CRS. \n
			:param lte_antenna_ports: AP1| AP2| AP4
			:param cellNull: optional repeated capability selector. Default value: Nr0
		"""
		param = Conversions.enum_scalar_to_str(lte_antenna_ports, enums.NumberOfPorts)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:NODE:CELL{cellNull_cmd_val}:LTE:NAP {param}')

	# noinspection PyTypeChecker
	def get(self, cellNull=repcap.CellNull.Nr0) -> enums.NumberOfPorts:
		"""SCPI: [SOURce<HW>]:BB:NR5G:NODE:CELL<CH0>:LTE:NAP \n
		Snippet: value: enums.NumberOfPorts = driver.source.bb.nr5G.node.cell.lte.nap.get(cellNull = repcap.CellNull.Nr0) \n
		Sets the number of antenna ports used for LTE-CRS. \n
			:param cellNull: optional repeated capability selector. Default value: Nr0
			:return: lte_antenna_ports: AP1| AP2| AP4"""
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:NODE:CELL{cellNull_cmd_val}:LTE:NAP?')
		return Conversions.str_to_scalar_enum(response, enums.NumberOfPorts)
