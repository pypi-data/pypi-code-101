from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Opu:
	"""Opu commands group definition. 4 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("opu", core, parent)

	@property
	def lcon(self):
		"""lcon commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_lcon'):
			from .Lcon import Lcon
			self._lcon = Lcon(self._core, self._cmd_group)
		return self._lcon

	@property
	def stage(self):
		"""stage commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_stage'):
			from .Stage import Stage
			self._stage = Stage(self._core, self._cmd_group)
		return self._stage

	def clone(self) -> 'Opu':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Opu(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
