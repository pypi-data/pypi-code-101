from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Doherty:
	"""Doherty commands group definition. 31 total commands, 6 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("doherty", core, parent)

	@property
	def amam(self):
		"""amam commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_amam'):
			from .Amam import Amam
			self._amam = Amam(self._core, self._cmd_group)
		return self._amam

	@property
	def amPm(self):
		"""amPm commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_amPm'):
			from .AmPm import AmPm
			self._amPm = AmPm(self._core, self._cmd_group)
		return self._amPm

	@property
	def inputPy(self):
		"""inputPy commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_inputPy'):
			from .InputPy import InputPy
			self._inputPy = InputPy(self._core, self._cmd_group)
		return self._inputPy

	@property
	def output(self):
		"""output commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_output'):
			from .Output import Output
			self._output = Output(self._core, self._cmd_group)
		return self._output

	@property
	def pin(self):
		"""pin commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_pin'):
			from .Pin import Pin
			self._pin = Pin(self._core, self._cmd_group)
		return self._pin

	@property
	def shaping(self):
		"""shaping commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_shaping'):
			from .Shaping import Shaping
			self._shaping = Shaping(self._core, self._cmd_group)
		return self._shaping

	# noinspection PyTypeChecker
	def get_scale(self) -> enums.IqOutEnvScale:
		"""SCPI: [SOURce<HW>]:IQ:DOHerty:SCALe \n
		Snippet: value: enums.IqOutEnvScale = driver.source.iq.doherty.get_scale() \n
		No command help available \n
			:return: scale: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:DOHerty:SCALe?')
		return Conversions.str_to_scalar_enum(response, enums.IqOutEnvScale)

	def set_scale(self, scale: enums.IqOutEnvScale) -> None:
		"""SCPI: [SOURce<HW>]:IQ:DOHerty:SCALe \n
		Snippet: driver.source.iq.doherty.set_scale(scale = enums.IqOutEnvScale.POWer) \n
		No command help available \n
			:param scale: No help available
		"""
		param = Conversions.enum_scalar_to_str(scale, enums.IqOutEnvScale)
		self._core.io.write(f'SOURce<HwInstance>:IQ:DOHerty:SCALe {param}')

	def clone(self) -> 'Doherty':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Doherty(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
