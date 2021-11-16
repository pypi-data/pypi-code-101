from typing import List

from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ...Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BgInfo:
	"""BgInfo commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bgInfo", core, parent)

	def get_catalog(self) -> List[str]:
		"""SCPI: DIAGnostic<HW>:BGINfo:CATalog \n
		Snippet: value: List[str] = driver.diagnostic.bgInfo.get_catalog() \n
		No command help available \n
			:return: catalog: No help available
		"""
		response = self._core.io.query_str('DIAGnostic<HwInstance>:BGINfo:CATalog?')
		return Conversions.str_to_str_list(response)

	def get_value(self) -> str:
		"""SCPI: DIAGnostic<HW>:BGINfo \n
		Snippet: value: str = driver.diagnostic.bgInfo.get_value() \n
		No command help available \n
			:return: bg_info: No help available
		"""
		response = self._core.io.query_str('DIAGnostic<HwInstance>:BGINfo?')
		return trim_str_response(response)
