from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Base:
	"""Base commands group definition. 51 total commands, 5 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("base", core, parent)

	@property
	def multiCmw(self):
		"""multiCmw commands group. 3 Sub-classes, 1 commands."""
		if not hasattr(self, '_multiCmw'):
			from .MultiCmw import MultiCmw
			self._multiCmw = MultiCmw(self._core, self._cmd_group)
		return self._multiCmw

	@property
	def ipc(self):
		"""ipc commands group. 1 Sub-classes, 3 commands."""
		if not hasattr(self, '_ipc'):
			from .Ipc import Ipc
			self._ipc = Ipc(self._core, self._cmd_group)
		return self._ipc

	@property
	def correction(self):
		"""correction commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_correction'):
			from .Correction import Correction
			self._correction = Correction(self._core, self._cmd_group)
		return self._correction

	@property
	def salignment(self):
		"""salignment commands group. 7 Sub-classes, 4 commands."""
		if not hasattr(self, '_salignment'):
			from .Salignment import Salignment
			self._salignment = Salignment(self._core, self._cmd_group)
		return self._salignment

	@property
	def buffer(self):
		"""buffer commands group. 1 Sub-classes, 6 commands."""
		if not hasattr(self, '_buffer'):
			from .Buffer import Buffer
			self._buffer = Buffer(self._core, self._cmd_group)
		return self._buffer

	def clone(self) -> 'Base':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Base(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
