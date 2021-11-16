from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Attenuation:
	"""Attenuation commands group definition. 3 total commands, 1 Sub-groups, 2 group commands"""

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

	def get_digital(self) -> float:
		"""SCPI: [SOURce<HW>]:POWer:ATTenuation:DIGital \n
		Snippet: value: float = driver.source.power.attenuation.get_digital() \n
		Sets a relative attenuation value for the baseband signal. \n
			:return: att_digital: float Range: -3.522 to 80
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:POWer:ATTenuation:DIGital?')
		return Conversions.str_to_float(response)

	def set_digital(self, att_digital: float) -> None:
		"""SCPI: [SOURce<HW>]:POWer:ATTenuation:DIGital \n
		Snippet: driver.source.power.attenuation.set_digital(att_digital = 1.0) \n
		Sets a relative attenuation value for the baseband signal. \n
			:param att_digital: float Range: -3.522 to 80
		"""
		param = Conversions.decimal_value_to_str(att_digital)
		self._core.io.write(f'SOURce<HwInstance>:POWer:ATTenuation:DIGital {param}')

	def get_stage(self) -> float:
		"""SCPI: [SOURce<HW>]:POWer:ATTenuation:STAGe \n
		Snippet: value: float = driver.source.power.attenuation.get_stage() \n
		No command help available \n
			:return: stage: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:POWer:ATTenuation:STAGe?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Attenuation':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Attenuation(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
