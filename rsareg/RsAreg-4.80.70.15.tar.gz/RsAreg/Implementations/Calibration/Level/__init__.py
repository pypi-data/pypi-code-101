from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Level:
	"""Level commands group definition. 2 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("level", core, parent)

	@property
	def attenuator(self):
		"""attenuator commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_attenuator'):
			from .Attenuator import Attenuator
			self._attenuator = Attenuator(self._core, self._cmd_group)
		return self._attenuator

	# noinspection PyTypeChecker
	def get_state(self) -> enums.StateExtended:
		"""SCPI: CALibration<HW>:LEVel:STATe \n
		Snippet: value: enums.StateExtended = driver.calibration.level.get_state() \n
		No command help available \n
			:return: areg_cal_pow_ext_us: No help available
		"""
		response = self._core.io.query_str('CALibration<HwInstance>:LEVel:STATe?')
		return Conversions.str_to_scalar_enum(response, enums.StateExtended)

	def set_state(self, areg_cal_pow_ext_us: enums.StateExtended) -> None:
		"""SCPI: CALibration<HW>:LEVel:STATe \n
		Snippet: driver.calibration.level.set_state(areg_cal_pow_ext_us = enums.StateExtended.DEFault) \n
		No command help available \n
			:param areg_cal_pow_ext_us: No help available
		"""
		param = Conversions.enum_scalar_to_str(areg_cal_pow_ext_us, enums.StateExtended)
		self._core.io.write(f'CALibration<HwInstance>:LEVel:STATe {param}')

	def clone(self) -> 'Level':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Level(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
