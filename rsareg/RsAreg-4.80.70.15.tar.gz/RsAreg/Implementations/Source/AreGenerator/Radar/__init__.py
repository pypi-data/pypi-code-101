from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Radar:
	"""Radar commands group definition. 10 total commands, 6 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("radar", core, parent)

	@property
	def antenna(self):
		"""antenna commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_antenna'):
			from .Antenna import Antenna
			self._antenna = Antenna(self._core, self._cmd_group)
		return self._antenna

	@property
	def base(self):
		"""base commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_base'):
			from .Base import Base
			self._base = Base(self._core, self._cmd_group)
		return self._base

	@property
	def dbypass(self):
		"""dbypass commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dbypass'):
			from .Dbypass import Dbypass
			self._dbypass = Dbypass(self._core, self._cmd_group)
		return self._dbypass

	@property
	def eirp(self):
		"""eirp commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_eirp'):
			from .Eirp import Eirp
			self._eirp = Eirp(self._core, self._cmd_group)
		return self._eirp

	@property
	def ota(self):
		"""ota commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ota'):
			from .Ota import Ota
			self._ota = Ota(self._core, self._cmd_group)
		return self._ota

	@property
	def power(self):
		"""power commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_power'):
			from .Power import Power
			self._power = Power(self._core, self._cmd_group)
		return self._power

	def get_lsensitivity(self) -> bool:
		"""SCPI: [SOURce<HW>]:AREGenerator:RADar:LSENsitivity \n
		Snippet: value: bool = driver.source.areGenerator.radar.get_lsensitivity() \n
		Defines if low sensitivity is used or not. \n
			:return: areg_radar_low_sen: 0| 1| OFF| ON
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:AREGenerator:RADar:LSENsitivity?')
		return Conversions.str_to_bool(response)

	def set_lsensitivity(self, areg_radar_low_sen: bool) -> None:
		"""SCPI: [SOURce<HW>]:AREGenerator:RADar:LSENsitivity \n
		Snippet: driver.source.areGenerator.radar.set_lsensitivity(areg_radar_low_sen = False) \n
		Defines if low sensitivity is used or not. \n
			:param areg_radar_low_sen: 0| 1| OFF| ON
		"""
		param = Conversions.bool_to_str(areg_radar_low_sen)
		self._core.io.write(f'SOURce<HwInstance>:AREGenerator:RADar:LSENsitivity {param}')

	def clone(self) -> 'Radar':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Radar(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
