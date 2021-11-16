from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ploss:
	"""Ploss commands group definition. 3 total commands, 3 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ploss", core, parent)

	@property
	def open(self):
		"""open commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_open'):
			from .Open import Open
			self._open = Open(self._core, self._cmd_group)
		return self._open

	@property
	def short(self):
		"""short commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_short'):
			from .Short import Short
			self._short = Short(self._core, self._cmd_group)
		return self._short

	@property
	def evaluate(self):
		"""evaluate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_evaluate'):
			from .Evaluate import Evaluate
			self._evaluate = Evaluate(self._core, self._cmd_group)
		return self._evaluate

	def clone(self) -> 'Ploss':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ploss(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
