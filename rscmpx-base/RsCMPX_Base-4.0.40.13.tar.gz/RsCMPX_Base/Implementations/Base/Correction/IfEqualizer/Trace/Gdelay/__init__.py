from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Gdelay:
	"""Gdelay commands group definition. 4 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("gdelay", core, parent)

	@property
	def corrected(self):
		"""corrected commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_corrected'):
			from .Corrected import Corrected
			self._corrected = Corrected(self._core, self._cmd_group)
		return self._corrected

	@property
	def uncorrected(self):
		"""uncorrected commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_uncorrected'):
			from .Uncorrected import Uncorrected
			self._uncorrected = Uncorrected(self._core, self._cmd_group)
		return self._uncorrected

	def clone(self) -> 'Gdelay':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Gdelay(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
