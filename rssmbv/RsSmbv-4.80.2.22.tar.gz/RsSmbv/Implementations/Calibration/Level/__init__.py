from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Level:
	"""Level commands group definition. 10 total commands, 4 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("level", core, parent)

	@property
	def amplifier(self):
		"""amplifier commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_amplifier'):
			from .Amplifier import Amplifier
			self._amplifier = Amplifier(self._core, self._cmd_group)
		return self._amplifier

	@property
	def attenuator(self):
		"""attenuator commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_attenuator'):
			from .Attenuator import Attenuator
			self._attenuator = Attenuator(self._core, self._cmd_group)
		return self._attenuator

	@property
	def detAtt(self):
		"""detAtt commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_detAtt'):
			from .DetAtt import DetAtt
			self._detAtt = DetAtt(self._core, self._cmd_group)
		return self._detAtt

	@property
	def measure(self):
		"""measure commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_measure'):
			from .Measure import Measure
			self._measure = Measure(self._core, self._cmd_group)
		return self._measure

	# noinspection PyTypeChecker
	def get_bandwidth(self) -> enums.CalPowBandwidth:
		"""SCPI: CALibration:LEVel:BWIDth \n
		Snippet: value: enums.CalPowBandwidth = driver.calibration.level.get_bandwidth() \n
		No command help available \n
			:return: bandwidth: No help available
		"""
		response = self._core.io.query_str('CALibration:LEVel:BWIDth?')
		return Conversions.str_to_scalar_enum(response, enums.CalPowBandwidth)

	def set_bandwidth(self, bandwidth: enums.CalPowBandwidth) -> None:
		"""SCPI: CALibration:LEVel:BWIDth \n
		Snippet: driver.calibration.level.set_bandwidth(bandwidth = enums.CalPowBandwidth.AUTO) \n
		No command help available \n
			:param bandwidth: No help available
		"""
		param = Conversions.enum_scalar_to_str(bandwidth, enums.CalPowBandwidth)
		self._core.io.write(f'CALibration:LEVel:BWIDth {param}')

	# noinspection PyTypeChecker
	def get_state(self) -> enums.StateExtended:
		"""SCPI: CALibration<HW>:LEVel:STATe \n
		Snippet: value: enums.StateExtended = driver.calibration.level.get_state() \n
		No command help available \n
			:return: state: No help available
		"""
		response = self._core.io.query_str('CALibration<HwInstance>:LEVel:STATe?')
		return Conversions.str_to_scalar_enum(response, enums.StateExtended)

	def set_state(self, state: enums.StateExtended) -> None:
		"""SCPI: CALibration<HW>:LEVel:STATe \n
		Snippet: driver.calibration.level.set_state(state = enums.StateExtended._0) \n
		No command help available \n
			:param state: No help available
		"""
		param = Conversions.enum_scalar_to_str(state, enums.StateExtended)
		self._core.io.write(f'CALibration<HwInstance>:LEVel:STATe {param}')

	def clone(self) -> 'Level':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Level(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
