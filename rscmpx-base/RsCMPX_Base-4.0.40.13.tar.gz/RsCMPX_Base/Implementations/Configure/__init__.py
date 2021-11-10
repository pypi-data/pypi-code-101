from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Configure:
	"""Configure commands group definition. 67 total commands, 8 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("configure", core, parent)

	@property
	def spoint(self):
		"""spoint commands group. 3 Sub-classes, 2 commands."""
		if not hasattr(self, '_spoint'):
			from .Spoint import Spoint
			self._spoint = Spoint(self._core, self._cmd_group)
		return self._spoint

	@property
	def semaphore(self):
		"""semaphore commands group. 4 Sub-classes, 2 commands."""
		if not hasattr(self, '_semaphore'):
			from .Semaphore import Semaphore
			self._semaphore = Semaphore(self._core, self._cmd_group)
		return self._semaphore

	@property
	def mutex(self):
		"""mutex commands group. 3 Sub-classes, 3 commands."""
		if not hasattr(self, '_mutex'):
			from .Mutex import Mutex
			self._mutex = Mutex(self._core, self._cmd_group)
		return self._mutex

	@property
	def base(self):
		"""base commands group. 8 Sub-classes, 1 commands."""
		if not hasattr(self, '_base'):
			from .Base import Base
			self._base = Base(self._core, self._cmd_group)
		return self._base

	@property
	def freqCorrection(self):
		"""freqCorrection commands group. 2 Sub-classes, 2 commands."""
		if not hasattr(self, '_freqCorrection'):
			from .FreqCorrection import FreqCorrection
			self._freqCorrection = FreqCorrection(self._core, self._cmd_group)
		return self._freqCorrection

	@property
	def singleCmw(self):
		"""singleCmw commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_singleCmw'):
			from .SingleCmw import SingleCmw
			self._singleCmw = SingleCmw(self._core, self._cmd_group)
		return self._singleCmw

	@property
	def cmwd(self):
		"""cmwd commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cmwd'):
			from .Cmwd import Cmwd
			self._cmwd = Cmwd(self._core, self._cmd_group)
		return self._cmwd

	@property
	def selftest(self):
		"""selftest commands group. 3 Sub-classes, 5 commands."""
		if not hasattr(self, '_selftest'):
			from .Selftest import Selftest
			self._selftest = Selftest(self._core, self._cmd_group)
		return self._selftest

	def clone(self) -> 'Configure':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Configure(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
