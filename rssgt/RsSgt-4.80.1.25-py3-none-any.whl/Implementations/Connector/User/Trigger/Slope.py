from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Slope:
	"""Slope commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("slope", core, parent)

	def set(self, slope: enums.SlopeType, userIx=repcap.UserIx.Default) -> None:
		"""SCPI: CONNector:USER<CH>:TRIGger:SLOPe \n
		Snippet: driver.connector.user.trigger.slope.set(slope = enums.SlopeType.NEGative, userIx = repcap.UserIx.Default) \n
		Sets the polarity of the active slope of an applied instrument trigger/clock. \n
			:param slope: NEGative| POSitive
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
		"""
		param = Conversions.enum_scalar_to_str(slope, enums.SlopeType)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		self._core.io.write(f'CONNector:USER{userIx_cmd_val}:TRIGger:SLOPe {param}')

	# noinspection PyTypeChecker
	def get(self, userIx=repcap.UserIx.Default) -> enums.SlopeType:
		"""SCPI: CONNector:USER<CH>:TRIGger:SLOPe \n
		Snippet: value: enums.SlopeType = driver.connector.user.trigger.slope.get(userIx = repcap.UserIx.Default) \n
		Sets the polarity of the active slope of an applied instrument trigger/clock. \n
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:return: slope: NEGative| POSitive"""
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		response = self._core.io.query_str(f'CONNector:USER{userIx_cmd_val}:TRIGger:SLOPe?')
		return Conversions.str_to_scalar_enum(response, enums.SlopeType)
