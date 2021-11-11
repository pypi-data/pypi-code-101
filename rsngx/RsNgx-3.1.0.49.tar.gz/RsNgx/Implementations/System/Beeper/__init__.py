from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Beeper:
	"""Beeper commands group definition. 8 total commands, 5 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("beeper", core, parent)

	@property
	def output(self):
		"""output commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_output'):
			from .Output import Output
			self._output = Output(self._core, self._cmd_group)
		return self._output

	@property
	def complete(self):
		"""complete commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_complete'):
			from .Complete import Complete
			self._complete = Complete(self._core, self._cmd_group)
		return self._complete

	@property
	def warningPy(self):
		"""warningPy commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_warningPy'):
			from .WarningPy import WarningPy
			self._warningPy = WarningPy(self._core, self._cmd_group)
		return self._warningPy

	@property
	def protection(self):
		"""protection commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_protection'):
			from .Protection import Protection
			self._protection = Protection(self._core, self._cmd_group)
		return self._protection

	@property
	def current(self):
		"""current commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_current'):
			from .Current import Current
			self._current = Current(self._core, self._cmd_group)
		return self._current
