from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Generator:
	"""Generator commands group definition. 15 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("generator", core, parent)

	@property
	def arb(self):
		"""arb commands group. 3 Sub-classes, 5 commands."""
		if not hasattr(self, '_arb'):
			from .Arb import Arb
			self._arb = Arb(self._core, self._cmd_group)
		return self._arb

	@property
	def sequencer(self):
		"""sequencer commands group. 3 Sub-classes, 1 commands."""
		if not hasattr(self, '_sequencer'):
			from .Sequencer import Sequencer
			self._sequencer = Sequencer(self._core, self._cmd_group)
		return self._sequencer

	def clone(self) -> 'Generator':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Generator(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
