from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Help:
	"""Help commands group definition. 3 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("help", core, parent)

	@property
	def syntax(self):
		"""syntax commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_syntax'):
			from .Syntax import Syntax
			self._syntax = Syntax(self._core, self._cmd_group)
		return self._syntax

	def get_headers(self) -> str:
		"""SCPI: SYSTem:HELP:HEADers \n
		Snippet: value: str = driver.system.help.get_headers() \n
		No command help available \n
			:return: headers: No help available
		"""
		response = self._core.io.query_str('SYSTem:HELP:HEADers?')
		return trim_str_response(response)

	def clone(self) -> 'Help':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Help(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
