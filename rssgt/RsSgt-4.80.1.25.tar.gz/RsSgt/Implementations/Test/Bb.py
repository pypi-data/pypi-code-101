from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bb:
	"""Bb commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bb", core, parent)

	def get_connection(self) -> bool:
		"""SCPI: TEST:BB:CONNection \n
		Snippet: value: bool = driver.test.bb.get_connection() \n
		Queries the state of the connection between connectors [USER1] and [USER2]. A 0=PASS response indicates that the
		connection is established, whereas a response 1=FAIL stands for a faulty connection. \n
			:return: connection: 0| 1| PASS| FAIL
		"""
		response = self._core.io.query_str('TEST:BB:CONNection?')
		return Conversions.str_to_bool(response)
