from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Measurement:
	"""Measurement commands group definition. 10 total commands, 5 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("measurement", core, parent)

	@property
	def multiEval(self):
		"""multiEval commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_multiEval'):
			from .MultiEval import MultiEval
			self._multiEval = MultiEval(self._core, self._cmd_group)
		return self._multiEval

	@property
	def prach(self):
		"""prach commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_prach'):
			from .Prach import Prach
			self._prach = Prach(self._core, self._cmd_group)
		return self._prach

	@property
	def tpc(self):
		"""tpc commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_tpc'):
			from .Tpc import Tpc
			self._tpc = Tpc(self._core, self._cmd_group)
		return self._tpc

	@property
	def olpControl(self):
		"""olpControl commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_olpControl'):
			from .OlpControl import OlpControl
			self._olpControl = OlpControl(self._core, self._cmd_group)
		return self._olpControl

	@property
	def ooSync(self):
		"""ooSync commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_ooSync'):
			from .OoSync import OoSync
			self._ooSync = OoSync(self._core, self._cmd_group)
		return self._ooSync

	def clone(self) -> 'Measurement':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Measurement(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
