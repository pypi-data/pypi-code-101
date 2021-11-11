from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Voltage:
	"""Voltage commands group definition. 17 total commands, 7 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("voltage", core, parent)

	@property
	def ainput(self):
		"""ainput commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_ainput'):
			from .Ainput import Ainput
			self._ainput = Ainput(self._core, self._cmd_group)
		return self._ainput

	@property
	def sense(self):
		"""sense commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sense'):
			from .Sense import Sense
			self._sense = Sense(self._core, self._cmd_group)
		return self._sense

	@property
	def dvm(self):
		"""dvm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dvm'):
			from .Dvm import Dvm
			self._dvm = Dvm(self._core, self._cmd_group)
		return self._dvm

	@property
	def negative(self):
		"""negative commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_negative'):
			from .Negative import Negative
			self._negative = Negative(self._core, self._cmd_group)
		return self._negative

	@property
	def level(self):
		"""level commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_level'):
			from .Level import Level
			self._level = Level(self._core, self._cmd_group)
		return self._level

	@property
	def protection(self):
		"""protection commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_protection'):
			from .Protection import Protection
			self._protection = Protection(self._core, self._cmd_group)
		return self._protection

	@property
	def ramp(self):
		"""ramp commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_ramp'):
			from .Ramp import Ramp
			self._ramp = Ramp(self._core, self._cmd_group)
		return self._ramp

	def get_range(self) -> float:
		"""SCPI: [SOURce]:VOLTage:RANGe \n
		Snippet: value: float = driver.source.voltage.get_range() \n
		No command help available \n
			:return: arg_0: No help available
		"""
		response = self._core.io.query_str('SOURce:VOLTage:RANGe?')
		return Conversions.str_to_float(response)

	def set_range(self, arg_0: float) -> None:
		"""SCPI: [SOURce]:VOLTage:RANGe \n
		Snippet: driver.source.voltage.set_range(arg_0 = 1.0) \n
		No command help available \n
			:param arg_0: No help available
		"""
		param = Conversions.decimal_value_to_str(arg_0)
		self._core.io.write(f'SOURce:VOLTage:RANGe {param}')
