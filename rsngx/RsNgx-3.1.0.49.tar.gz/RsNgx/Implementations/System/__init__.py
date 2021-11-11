from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class System:
	"""System commands group definition. 46 total commands, 12 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("system", core, parent)

	@property
	def beeper(self):
		"""beeper commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_beeper'):
			from .Beeper import Beeper
			self._beeper = Beeper(self._core, self._cmd_group)
		return self._beeper

	@property
	def touch(self):
		"""touch commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_touch'):
			from .Touch import Touch
			self._touch = Touch(self._core, self._cmd_group)
		return self._touch

	@property
	def communicate(self):
		"""communicate commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_communicate'):
			from .Communicate import Communicate
			self._communicate = Communicate(self._core, self._cmd_group)
		return self._communicate

	@property
	def date(self):
		"""date commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_date'):
			from .Date import Date
			self._date = Date(self._core, self._cmd_group)
		return self._date

	@property
	def key(self):
		"""key commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_key'):
			from .Key import Key
			self._key = Key(self._core, self._cmd_group)
		return self._key

	@property
	def local(self):
		"""local commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_local'):
			from .Local import Local
			self._local = Local(self._core, self._cmd_group)
		return self._local

	@property
	def remote(self):
		"""remote commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_remote'):
			from .Remote import Remote
			self._remote = Remote(self._core, self._cmd_group)
		return self._remote

	@property
	def rwLock(self):
		"""rwLock commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rwLock'):
			from .RwLock import RwLock
			self._rwLock = RwLock(self._core, self._cmd_group)
		return self._rwLock

	@property
	def time(self):
		"""time commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_time'):
			from .Time import Time
			self._time = Time(self._core, self._cmd_group)
		return self._time

	@property
	def restart(self):
		"""restart commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_restart'):
			from .Restart import Restart
			self._restart = Restart(self._core, self._cmd_group)
		return self._restart

	@property
	def setting(self):
		"""setting commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_setting'):
			from .Setting import Setting
			self._setting = Setting(self._core, self._cmd_group)
		return self._setting

	@property
	def vnc(self):
		"""vnc commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_vnc'):
			from .Vnc import Vnc
			self._vnc = Vnc(self._core, self._cmd_group)
		return self._vnc

	def get_up_time(self) -> str:
		"""SCPI: SYSTem:UPTime \n
		Snippet: value: str = driver.system.get_up_time() \n
		Queries system uptime. \n
			:return: result: No help available
		"""
		response = self._core.io.query_str('SYSTem:UPTime?')
		return trim_str_response(response)
