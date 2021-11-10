from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Routing:
	"""Routing commands group definition. 1 total commands, 1 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("routing", core, parent)

	@property
	def possible(self):
		"""possible commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_possible'):
			from .Possible import Possible
			self._possible = Possible(self._core, self._cmd_group)
		return self._possible

	def clone(self) -> 'Routing':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Routing(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
