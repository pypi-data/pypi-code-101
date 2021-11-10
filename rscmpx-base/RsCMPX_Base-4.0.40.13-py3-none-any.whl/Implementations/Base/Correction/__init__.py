from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Correction:
	"""Correction commands group definition. 13 total commands, 1 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("correction", core, parent)

	@property
	def ifEqualizer(self):
		"""ifEqualizer commands group. 3 Sub-classes, 2 commands."""
		if not hasattr(self, '_ifEqualizer'):
			from .IfEqualizer import IfEqualizer
			self._ifEqualizer = IfEqualizer(self._core, self._cmd_group)
		return self._ifEqualizer

	def clone(self) -> 'Correction':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Correction(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
