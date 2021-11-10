from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IpSet:
	"""IpSet commands group definition. 1 total commands, 1 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ipSet", core, parent)

	@property
	def subMonitor(self):
		"""subMonitor commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_subMonitor'):
			from .SubMonitor import SubMonitor
			self._subMonitor = SubMonitor(self._core, self._cmd_group)
		return self._subMonitor

	def clone(self) -> 'IpSet':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = IpSet(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
