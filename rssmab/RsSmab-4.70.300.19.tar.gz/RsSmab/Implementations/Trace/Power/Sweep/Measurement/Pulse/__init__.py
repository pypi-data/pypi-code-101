from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pulse:
	"""Pulse commands group definition. 11 total commands, 7 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pulse", core, parent)

	@property
	def all(self):
		"""all commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_all'):
			from .All import All
			self._all = All(self._core, self._cmd_group)
		return self._all

	@property
	def dcycle(self):
		"""dcycle commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_dcycle'):
			from .Dcycle import Dcycle
			self._dcycle = Dcycle(self._core, self._cmd_group)
		return self._dcycle

	@property
	def display(self):
		"""display commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_display'):
			from .Display import Display
			self._display = Display(self._core, self._cmd_group)
		return self._display

	@property
	def duration(self):
		"""duration commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_duration'):
			from .Duration import Duration
			self._duration = Duration(self._core, self._cmd_group)
		return self._duration

	@property
	def period(self):
		"""period commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_period'):
			from .Period import Period
			self._period = Period(self._core, self._cmd_group)
		return self._period

	@property
	def separation(self):
		"""separation commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_separation'):
			from .Separation import Separation
			self._separation = Separation(self._core, self._cmd_group)
		return self._separation

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	def clone(self) -> 'Pulse':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pulse(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
