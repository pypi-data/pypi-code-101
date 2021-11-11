from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Source:
	"""Source commands group definition. 41 total commands, 8 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("source", core, parent)

	@property
	def voltage(self):
		"""voltage commands group. 7 Sub-classes, 1 commands."""
		if not hasattr(self, '_voltage'):
			from .Voltage import Voltage
			self._voltage = Voltage(self._core, self._cmd_group)
		return self._voltage

	@property
	def protection(self):
		"""protection commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_protection'):
			from .Protection import Protection
			self._protection = Protection(self._core, self._cmd_group)
		return self._protection

	@property
	def current(self):
		"""current commands group. 3 Sub-classes, 1 commands."""
		if not hasattr(self, '_current'):
			from .Current import Current
			self._current = Current(self._core, self._cmd_group)
		return self._current

	@property
	def resistance(self):
		"""resistance commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_resistance'):
			from .Resistance import Resistance
			self._resistance = Resistance(self._core, self._cmd_group)
		return self._resistance

	@property
	def modulation(self):
		"""modulation commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_modulation'):
			from .Modulation import Modulation
			self._modulation = Modulation(self._core, self._cmd_group)
		return self._modulation

	@property
	def priority(self):
		"""priority commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_priority'):
			from .Priority import Priority
			self._priority = Priority(self._core, self._cmd_group)
		return self._priority

	@property
	def power(self):
		"""power commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_power'):
			from .Power import Power
			self._power = Power(self._core, self._cmd_group)
		return self._power

	@property
	def alimit(self):
		"""alimit commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_alimit'):
			from .Alimit import Alimit
			self._alimit = Alimit(self._core, self._cmd_group)
		return self._alimit
