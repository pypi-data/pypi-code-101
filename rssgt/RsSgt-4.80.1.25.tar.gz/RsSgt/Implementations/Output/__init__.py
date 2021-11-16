from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Output:
	"""Output commands group definition. 6 total commands, 3 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("output", core, parent)

	@property
	def afixed(self):
		"""afixed commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_afixed'):
			from .Afixed import Afixed
			self._afixed = Afixed(self._core, self._cmd_group)
		return self._afixed

	@property
	def protection(self):
		"""protection commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_protection'):
			from .Protection import Protection
			self._protection = Protection(self._core, self._cmd_group)
		return self._protection

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	# noinspection PyTypeChecker
	def get_amode(self) -> enums.AttMode:
		"""SCPI: OUTPut<HW>:AMODe \n
		Snippet: value: enums.AttMode = driver.output.get_amode() \n
		Switches the mode of the attenuator at the RF output. \n
			:return: amode: AUTO| FIXed| APASsive AUTO The attenuator is switched automatically. The level settings are made in the full range. APASsive The attenuator is switched automatically. The level settings are made only for the passive reference circuits. The high-level ranges are not available. FIXed The level settings are made without switching the attenuator. When this operating mode is switched on, the attenuator is fixed to its current position and the resulting variation range is defined.
		"""
		response = self._core.io.query_str('OUTPut<HwInstance>:AMODe?')
		return Conversions.str_to_scalar_enum(response, enums.AttMode)

	def set_amode(self, amode: enums.AttMode) -> None:
		"""SCPI: OUTPut<HW>:AMODe \n
		Snippet: driver.output.set_amode(amode = enums.AttMode.APASsive) \n
		Switches the mode of the attenuator at the RF output. \n
			:param amode: AUTO| FIXed| APASsive AUTO The attenuator is switched automatically. The level settings are made in the full range. APASsive The attenuator is switched automatically. The level settings are made only for the passive reference circuits. The high-level ranges are not available. FIXed The level settings are made without switching the attenuator. When this operating mode is switched on, the attenuator is fixed to its current position and the resulting variation range is defined.
		"""
		param = Conversions.enum_scalar_to_str(amode, enums.AttMode)
		self._core.io.write(f'OUTPut<HwInstance>:AMODe {param}')

	def clone(self) -> 'Output':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Output(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
