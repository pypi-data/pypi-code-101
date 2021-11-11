from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Select:
	"""Select commands group definition. 1 total commands, 1 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("select", core, parent)

	@property
	def ch(self):
		"""ch commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ch'):
			from .Ch import Ch
			self._ch = Ch(self._core, self._cmd_group)
		return self._ch
