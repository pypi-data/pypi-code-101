from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Base:
	"""Base commands group definition. 11 total commands, 4 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("base", core, parent)

	@property
	def extA(self):
		"""extA commands group. 1 Sub-classes, 3 commands."""
		if not hasattr(self, '_extA'):
			from .ExtA import ExtA
			self._extA = ExtA(self._core, self._cmd_group)
		return self._extA

	@property
	def extB(self):
		"""extB commands group. 1 Sub-classes, 3 commands."""
		if not hasattr(self, '_extB'):
			from .ExtB import ExtB
			self._extB = ExtB(self._core, self._cmd_group)
		return self._extB

	@property
	def uinitiated(self):
		"""uinitiated commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_uinitiated'):
			from .Uinitiated import Uinitiated
			self._uinitiated = Uinitiated(self._core, self._cmd_group)
		return self._uinitiated

	@property
	def eout(self):
		"""eout commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_eout'):
			from .Eout import Eout
			self._eout = Eout(self._core, self._cmd_group)
		return self._eout

	def clone(self) -> 'Base':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Base(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
