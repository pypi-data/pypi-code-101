from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Omode:
	"""Omode commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("omode", core, parent)

	def set(self, omode: enums.UserPlug, userIx=repcap.UserIx.Default) -> None:
		"""SCPI: CONNector:USER<CH>:OMODe \n
		Snippet: driver.connector.user.omode.set(omode = enums.UserPlug.CIN, userIx = repcap.UserIx.Default) \n
		Sets the operation mode of the user connector. \n
			:param omode: MKR1| MKR2| TRIGger| CIN| COUT| SIN| SOUT| NEXT| LOW| MLATency| MARRived| HIGH| SVALid| SNValid| PVOut| PETRigger| PEMSource| TOUT MKR1/2 Marker 1/2 TRIGger Trigger TOUT Trigger out CIN Clock in COUT Clock out SIN Sync in SOUT Sync out NEXT Next trigger SVALid|SNValid Signal valid /not valid PVOut Pulse generator video out PETRigger Pulse generator external trigger PEMSource External pulse modulator source
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
		"""
		param = Conversions.enum_scalar_to_str(omode, enums.UserPlug)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		self._core.io.write(f'CONNector:USER{userIx_cmd_val}:OMODe {param}')

	# noinspection PyTypeChecker
	def get(self, userIx=repcap.UserIx.Default) -> enums.UserPlug:
		"""SCPI: CONNector:USER<CH>:OMODe \n
		Snippet: value: enums.UserPlug = driver.connector.user.omode.get(userIx = repcap.UserIx.Default) \n
		Sets the operation mode of the user connector. \n
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:return: omode: MKR1| MKR2| TRIGger| CIN| COUT| SIN| SOUT| NEXT| LOW| MLATency| MARRived| HIGH| SVALid| SNValid| PVOut| PETRigger| PEMSource| TOUT MKR1/2 Marker 1/2 TRIGger Trigger TOUT Trigger out CIN Clock in COUT Clock out SIN Sync in SOUT Sync out NEXT Next trigger SVALid|SNValid Signal valid /not valid PVOut Pulse generator video out PETRigger Pulse generator external trigger PEMSource External pulse modulator source"""
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		response = self._core.io.query_str(f'CONNector:USER{userIx_cmd_val}:OMODe?')
		return Conversions.str_to_scalar_enum(response, enums.UserPlug)
