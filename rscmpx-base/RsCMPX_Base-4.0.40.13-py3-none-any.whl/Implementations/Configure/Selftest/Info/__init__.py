from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Info:
	"""Info commands group definition. 3 total commands, 2 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("info", core, parent)

	@property
	def message(self):
		"""message commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_message'):
			from .Message import Message
			self._message = Message(self._core, self._cmd_group)
		return self._message

	@property
	def description(self):
		"""description commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_description'):
			from .Description import Description
			self._description = Description(self._core, self._cmd_group)
		return self._description

	def get_progress(self) -> str:
		"""SCPI: CONFigure:SELFtest:INFO:PROGress \n
		Snippet: value: str = driver.configure.selftest.info.get_progress() \n
		No command help available \n
			:return: progress: No help available
		"""
		response = self._core.io.query_str('CONFigure:SELFtest:INFO:PROGress?')
		return trim_str_response(response)

	def clone(self) -> 'Info':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Info(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
