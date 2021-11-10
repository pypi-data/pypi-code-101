from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Init:
	"""Init commands group definition. 1 total commands, 1 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("init", core, parent)

	@property
	def selftest(self):
		"""selftest commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_selftest'):
			from .Selftest import Selftest
			self._selftest = Selftest(self._core, self._cmd_group)
		return self._selftest

	def clone(self) -> 'Init':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Init(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
