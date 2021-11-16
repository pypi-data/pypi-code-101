from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Attenuation:
	"""Attenuation commands group definition. 3 total commands, 2 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("attenuation", core, parent)

	@property
	def rfOff(self):
		"""rfOff commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rfOff'):
			from .RfOff import RfOff
			self._rfOff = RfOff(self._core, self._cmd_group)
		return self._rfOff

	@property
	def sover(self):
		"""sover commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sover'):
			from .Sover import Sover
			self._sover = Sover(self._core, self._cmd_group)
		return self._sover

	def get_digital(self) -> float:
		"""SCPI: [SOURce<HW>]:POWer:ATTenuation:DIGital \n
		Snippet: value: float = driver.source.power.attenuation.get_digital() \n
		Sets a relative attentuation value for the baseband signal. \n
			:return: att_digital: float Range: 0 to 80, Unit: dB
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:POWer:ATTenuation:DIGital?')
		return Conversions.str_to_float(response)

	def set_digital(self, att_digital: float) -> None:
		"""SCPI: [SOURce<HW>]:POWer:ATTenuation:DIGital \n
		Snippet: driver.source.power.attenuation.set_digital(att_digital = 1.0) \n
		Sets a relative attentuation value for the baseband signal. \n
			:param att_digital: float Range: 0 to 80, Unit: dB
		"""
		param = Conversions.decimal_value_to_str(att_digital)
		self._core.io.write(f'SOURce<HwInstance>:POWer:ATTenuation:DIGital {param}')

	def clone(self) -> 'Attenuation':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Attenuation(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
