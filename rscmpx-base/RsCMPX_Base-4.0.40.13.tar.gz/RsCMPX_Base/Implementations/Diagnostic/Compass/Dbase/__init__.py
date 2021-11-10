from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dbase:
	"""Dbase commands group definition. 8 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dbase", core, parent)

	@property
	def rlogging(self):
		"""rlogging commands group. 1 Sub-classes, 3 commands."""
		if not hasattr(self, '_rlogging'):
			from .Rlogging import Rlogging
			self._rlogging = Rlogging(self._core, self._cmd_group)
		return self._rlogging

	@property
	def taLogging(self):
		"""taLogging commands group. 2 Sub-classes, 2 commands."""
		if not hasattr(self, '_taLogging'):
			from .TaLogging import TaLogging
			self._taLogging = TaLogging(self._core, self._cmd_group)
		return self._taLogging

	def clone(self) -> 'Dbase':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Dbase(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
