from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Status:
	"""Status commands group definition. 20 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("status", core, parent)

	@property
	def operation(self):
		"""operation commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_operation'):
			from .Operation import Operation
			self._operation = Operation(self._core, self._cmd_group)
		return self._operation

	@property
	def questionable(self):
		"""questionable commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_questionable'):
			from .Questionable import Questionable
			self._questionable = Questionable(self._core, self._cmd_group)
		return self._questionable
