from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Spath:
	"""Spath commands group definition. 2 total commands, 1 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("spath", core, parent)

	@property
	def correctionTable(self):
		"""correctionTable commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_correctionTable'):
			from .CorrectionTable import CorrectionTable
			self._correctionTable = CorrectionTable(self._core, self._cmd_group)
		return self._correctionTable

	def clone(self) -> 'Spath':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Spath(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
