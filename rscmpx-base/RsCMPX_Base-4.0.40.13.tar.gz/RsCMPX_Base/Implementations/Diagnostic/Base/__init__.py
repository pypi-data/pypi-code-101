from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Base:
	"""Base commands group definition. 7 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("base", core, parent)

	@property
	def mmi(self):
		"""mmi commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mmi'):
			from .Mmi import Mmi
			self._mmi = Mmi(self._core, self._cmd_group)
		return self._mmi

	@property
	def salignment(self):
		"""salignment commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_salignment'):
			from .Salignment import Salignment
			self._salignment = Salignment(self._core, self._cmd_group)
		return self._salignment

	def clone(self) -> 'Base':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Base(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
