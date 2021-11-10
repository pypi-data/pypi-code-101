from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AreGenerator:
	"""AreGenerator commands group definition. 21 total commands, 3 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("areGenerator", core, parent)

	@property
	def object(self):
		"""object commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_object'):
			from .Object import Object
			self._object = Object(self._core, self._cmd_group)
		return self._object

	@property
	def radar(self):
		"""radar commands group. 6 Sub-classes, 1 commands."""
		if not hasattr(self, '_radar'):
			from .Radar import Radar
			self._radar = Radar(self._core, self._cmd_group)
		return self._radar

	@property
	def units(self):
		"""units commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_units'):
			from .Units import Units
			self._units = Units(self._core, self._cmd_group)
		return self._units

	def clone(self) -> 'AreGenerator':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = AreGenerator(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
