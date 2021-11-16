from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Threshold:
	"""Threshold commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("threshold", core, parent)

	def get(self, userIx=repcap.UserIx.Default) -> float:
		"""SCPI: CONNector:USER<CH>:THReshold \n
		Snippet: value: float = driver.connector.user.threshold.get(userIx = repcap.UserIx.Default) \n
		Sets the threshold for the user connector. \n
			:param userIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'User')
			:return: threshold: float Range: 0 to 2"""
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		response = self._core.io.query_str(f'CONNector:USER{userIx_cmd_val}:THReshold?')
		return Conversions.str_to_float(response)
