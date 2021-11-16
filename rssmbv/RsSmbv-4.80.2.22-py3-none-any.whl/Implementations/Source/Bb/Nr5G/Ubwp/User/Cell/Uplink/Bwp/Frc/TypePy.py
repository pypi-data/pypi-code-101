from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ........... import enums
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TypePy:
	"""TypePy commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("typePy", core, parent)

	def set(self, frc_type: enums.FrcType, userNull=repcap.UserNull.Default, cellNull=repcap.CellNull.Default, bwPartNull=repcap.BwPartNull.Default) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:UBWP:USER<CH0>:CELL<ST0>:UL:BWP<DIR0>:FRC:TYPE \n
		Snippet: driver.source.bb.nr5G.ubwp.user.cell.uplink.bwp.frc.typePy.set(frc_type = enums.FrcType.FR1A11, userNull = repcap.UserNull.Default, cellNull = repcap.CellNull.Default, bwPartNull = repcap.BwPartNull.Default) \n
		Selects the fixed reference measurement channel (FRC) . The currently available FRCs depend on the selected BWP
		subcarrier spacing SCS) and selected number of resource blocks. \n
			:param frc_type: FR1A11| FR1A12| FR1A13| FR1A14| FR1A15| FR1A16| FR1A17| FR1A18| FR1A19| FR2A11| FR2A12| FR2A13| FR2A14| FR2A15| FR1A21| FR1A22| FR1A23| FR1A24| FR1A25| FR1A26| NA| FR1A38| FR1A39| FR1A310| FR1A311| FR1A312| FR1A313| FR1A314| FR1A322| FR1A323| FR1A324| FR1A325| FR1A326| FR1A327| FR1A328| FR1A48| FR1A49| FR1A410| FR1A411| FR1A412| FR1A413| FR1A414| FR1A422| FR1A423| FR1A424| FR1A425| FR1A426| FR1A427| FR1A428| FR1A58| FR1A59| FR1A510| FR1A511| FR1A512| FR1A513| FR1A514| FR1A331| FR1A332| FR2A31| FR2A32| FR2A33| FR2A34| FR2A35| FR2A36| FR2A37| FR2A38| FR2A39| FR2A310| FR2A311| FR2A312| FR2A41| FR2A42| FR2A43| FR2A44| FR2A45| FR2A46| FR2A47| FR2A48| FR2A49| FR2A410| FR2A51| FR2A52| FR2A53| FR2A54| FR2A55| FR2A313| FR2A314| FR2A315| FR2A316| FR2A317| FR2A318| FR2A319| FR2A320| FR2A321| FR2A322| FR2A323| FR2A324| FR2A411| FR2A412| FR2A413| FR2A414| FR2A415| FR2A416| FR2A417| FR2A418| FR2A419| FR2A420| FR2A56| FR2A57| FR2A58| FR2A59| FR2A510
			:param userNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'User')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:param bwPartNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Bwp')
		"""
		param = Conversions.enum_scalar_to_str(frc_type, enums.FrcType)
		userNull_cmd_val = self._cmd_group.get_repcap_cmd_value(userNull, repcap.UserNull)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		bwPartNull_cmd_val = self._cmd_group.get_repcap_cmd_value(bwPartNull, repcap.BwPartNull)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:UBWP:USER{userNull_cmd_val}:CELL{cellNull_cmd_val}:UL:BWP{bwPartNull_cmd_val}:FRC:TYPE {param}')

	# noinspection PyTypeChecker
	def get(self, userNull=repcap.UserNull.Default, cellNull=repcap.CellNull.Default, bwPartNull=repcap.BwPartNull.Default) -> enums.FrcType:
		"""SCPI: [SOURce<HW>]:BB:NR5G:UBWP:USER<CH0>:CELL<ST0>:UL:BWP<DIR0>:FRC:TYPE \n
		Snippet: value: enums.FrcType = driver.source.bb.nr5G.ubwp.user.cell.uplink.bwp.frc.typePy.get(userNull = repcap.UserNull.Default, cellNull = repcap.CellNull.Default, bwPartNull = repcap.BwPartNull.Default) \n
		Selects the fixed reference measurement channel (FRC) . The currently available FRCs depend on the selected BWP
		subcarrier spacing SCS) and selected number of resource blocks. \n
			:param userNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'User')
			:param cellNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Cell')
			:param bwPartNull: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Bwp')
			:return: frc_type: FR1A11| FR1A12| FR1A13| FR1A14| FR1A15| FR1A16| FR1A17| FR1A18| FR1A19| FR2A11| FR2A12| FR2A13| FR2A14| FR2A15| FR1A21| FR1A22| FR1A23| FR1A24| FR1A25| FR1A26| NA| FR1A38| FR1A39| FR1A310| FR1A311| FR1A312| FR1A313| FR1A314| FR1A322| FR1A323| FR1A324| FR1A325| FR1A326| FR1A327| FR1A328| FR1A48| FR1A49| FR1A410| FR1A411| FR1A412| FR1A413| FR1A414| FR1A422| FR1A423| FR1A424| FR1A425| FR1A426| FR1A427| FR1A428| FR1A58| FR1A59| FR1A510| FR1A511| FR1A512| FR1A513| FR1A514| FR1A331| FR1A332| FR2A31| FR2A32| FR2A33| FR2A34| FR2A35| FR2A36| FR2A37| FR2A38| FR2A39| FR2A310| FR2A311| FR2A312| FR2A41| FR2A42| FR2A43| FR2A44| FR2A45| FR2A46| FR2A47| FR2A48| FR2A49| FR2A410| FR2A51| FR2A52| FR2A53| FR2A54| FR2A55| FR2A313| FR2A314| FR2A315| FR2A316| FR2A317| FR2A318| FR2A319| FR2A320| FR2A321| FR2A322| FR2A323| FR2A324| FR2A411| FR2A412| FR2A413| FR2A414| FR2A415| FR2A416| FR2A417| FR2A418| FR2A419| FR2A420| FR2A56| FR2A57| FR2A58| FR2A59| FR2A510"""
		userNull_cmd_val = self._cmd_group.get_repcap_cmd_value(userNull, repcap.UserNull)
		cellNull_cmd_val = self._cmd_group.get_repcap_cmd_value(cellNull, repcap.CellNull)
		bwPartNull_cmd_val = self._cmd_group.get_repcap_cmd_value(bwPartNull, repcap.BwPartNull)
		response = self._core.io.query_str(f'SOURce<HwInstance>:BB:NR5G:UBWP:USER{userNull_cmd_val}:CELL{cellNull_cmd_val}:UL:BWP{bwPartNull_cmd_val}:FRC:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.FrcType)
