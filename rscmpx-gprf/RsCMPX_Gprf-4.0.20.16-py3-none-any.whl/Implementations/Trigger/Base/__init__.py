from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Base:
	"""Base commands group definition. 4 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("base", core, parent)

	@property
	def extA(self):
		"""extA commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_extA'):
			from .ExtA import ExtA
			self._extA = ExtA(self._core, self._cmd_group)
		return self._extA

	@property
	def extB(self):
		"""extB commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_extB'):
			from .ExtB import ExtB
			self._extB = ExtB(self._core, self._cmd_group)
		return self._extB

	def clone(self) -> 'Base':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Base(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
