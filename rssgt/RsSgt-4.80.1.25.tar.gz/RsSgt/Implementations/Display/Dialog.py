from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dialog:
	"""Dialog commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dialog", core, parent)

	def get_id(self) -> str:
		"""SCPI: DISPlay:DIALog:ID \n
		Snippet: value: str = driver.display.dialog.get_id() \n
		No command help available \n
			:return: dialog_id_list: No help available
		"""
		response = self._core.io.query_str('DISPlay:DIALog:ID?')
		return trim_str_response(response)
