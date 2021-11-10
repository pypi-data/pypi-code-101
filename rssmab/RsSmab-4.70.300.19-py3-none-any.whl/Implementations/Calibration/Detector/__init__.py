from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Detector:
	"""Detector commands group definition. 2 total commands, 1 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("detector", core, parent)

	@property
	def rfLevel(self):
		"""rfLevel commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_rfLevel'):
			from .RfLevel import RfLevel
			self._rfLevel = RfLevel(self._core, self._cmd_group)
		return self._rfLevel

	def clone(self) -> 'Detector':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Detector(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
