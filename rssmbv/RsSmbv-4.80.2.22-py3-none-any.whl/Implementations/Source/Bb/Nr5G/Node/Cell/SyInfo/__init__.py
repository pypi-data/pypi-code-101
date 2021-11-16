from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SyInfo:
	"""SyInfo commands group definition. 3 total commands, 3 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("syInfo", core, parent)

	@property
	def hacbook(self):
		"""hacbook commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hacbook'):
			from .Hacbook import Hacbook
			self._hacbook = Hacbook(self._core, self._cmd_group)
		return self._hacbook

	@property
	def sfOffset(self):
		"""sfOffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sfOffset'):
			from .SfOffset import SfOffset
			self._sfOffset = SfOffset(self._core, self._cmd_group)
		return self._sfOffset

	@property
	def sul(self):
		"""sul commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_sul'):
			from .Sul import Sul
			self._sul = Sul(self._core, self._cmd_group)
		return self._sul

	def clone(self) -> 'SyInfo':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SyInfo(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
