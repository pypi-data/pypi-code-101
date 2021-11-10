from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Record:
	"""Record commands group definition. 2 total commands, 1 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("record", core, parent)

	@property
	def macro(self):
		"""macro commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_macro'):
			from .Macro import Macro
			self._macro = Macro(self._core, self._cmd_group)
		return self._macro

	def clone(self) -> 'Record':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Record(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
