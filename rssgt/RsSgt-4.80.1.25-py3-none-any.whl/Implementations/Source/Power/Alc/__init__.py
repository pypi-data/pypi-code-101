from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Alc:
	"""Alc commands group definition. 3 total commands, 1 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("alc", core, parent)

	@property
	def sonce(self):
		"""sonce commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sonce'):
			from .Sonce import Sonce
			self._sonce = Sonce(self._core, self._cmd_group)
		return self._sonce

	# noinspection PyTypeChecker
	def get_dsensitivity(self) -> enums.CalPowDetAtt:
		"""SCPI: [SOURce<HW>]:POWer:ALC:DSENsitivity \n
		Snippet: value: enums.CalPowDetAtt = driver.source.power.alc.get_dsensitivity() \n
		Sets the power detector sensitivity. Used for compatibility reasons only. \n
			:return: sensitivity: OFF| LOW| MED| HIGH
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:POWer:ALC:DSENsitivity?')
		return Conversions.str_to_scalar_enum(response, enums.CalPowDetAtt)

	def set_dsensitivity(self, sensitivity: enums.CalPowDetAtt) -> None:
		"""SCPI: [SOURce<HW>]:POWer:ALC:DSENsitivity \n
		Snippet: driver.source.power.alc.set_dsensitivity(sensitivity = enums.CalPowDetAtt.HIGH) \n
		Sets the power detector sensitivity. Used for compatibility reasons only. \n
			:param sensitivity: OFF| LOW| MED| HIGH
		"""
		param = Conversions.enum_scalar_to_str(sensitivity, enums.CalPowDetAtt)
		self._core.io.write(f'SOURce<HwInstance>:POWer:ALC:DSENsitivity {param}')

	# noinspection PyTypeChecker
	def get_state(self) -> enums.PowAlcState:
		"""SCPI: [SOURce<HW>]:POWer:ALC:[STATe] \n
		Snippet: value: enums.PowAlcState = driver.source.power.alc.get_state() \n
		Activates/deactivates automatic level control. \n
			:return: state: 1| OFFTable| OFF| ONTable| AUTO| ON
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:POWer:ALC:STATe?')
		return Conversions.str_to_scalar_enum(response, enums.PowAlcState)

	def set_state(self, state: enums.PowAlcState) -> None:
		"""SCPI: [SOURce<HW>]:POWer:ALC:[STATe] \n
		Snippet: driver.source.power.alc.set_state(state = enums.PowAlcState._1) \n
		Activates/deactivates automatic level control. \n
			:param state: 1| OFFTable| OFF| ONTable| AUTO| ON
		"""
		param = Conversions.enum_scalar_to_str(state, enums.PowAlcState)
		self._core.io.write(f'SOURce<HwInstance>:POWer:ALC:STATe {param}')

	def clone(self) -> 'Alc':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Alc(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
