from typing import List

from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Point:
	"""Point commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("point", core, parent)

	def get_catalog(self) -> List[str]:
		"""SCPI: DIAGnostic:POINt:CATalog \n
		Snippet: value: List[str] = driver.diagnostic.point.get_catalog() \n
		Queries the test points available in the instrument. \n
			:return: diag_poin_id_cat: No help available
		"""
		response = self._core.io.query_str('DIAGnostic:POINt:CATalog?')
		return Conversions.str_to_str_list(response)
