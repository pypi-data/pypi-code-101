from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UseCase:
	"""UseCase commands group definition. 2 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("useCase", core, parent)

	@property
	def data(self):
		"""data commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_data'):
			from .Data import Data
			self._data = Data(self._core, self._cmd_group)
		return self._data

	def get_ids(self) -> List[int]:
		"""SCPI: DIAGnostic:FOOTprint:USECase:IDS \n
		Snippet: value: List[int] = driver.diagnostic.footPrint.useCase.get_ids() \n
		No command help available \n
			:return: ids: No help available
		"""
		response = self._core.io.query_bin_or_ascii_int_list('DIAGnostic:FOOTprint:USECase:IDS?')
		return response

	def clone(self) -> 'UseCase':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = UseCase(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
