from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Trigger:
	"""Trigger commands group definition. 3 total commands, 1 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("trigger", core, parent)

	@property
	def bband(self):
		"""bband commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bband'):
			from .Bband import Bband
			self._bband = Bband(self._core, self._cmd_group)
		return self._bband

	# noinspection PyTypeChecker
	def get_impedance(self) -> enums.InputImpRf:
		"""SCPI: [SOURce<HW>]:INPut:TRIGger:IMPedance \n
		Snippet: value: enums.InputImpRf = driver.source.inputPy.trigger.get_impedance() \n
		No command help available \n
			:return: impedance: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:INPut:TRIGger:IMPedance?')
		return Conversions.str_to_scalar_enum(response, enums.InputImpRf)

	def set_impedance(self, impedance: enums.InputImpRf) -> None:
		"""SCPI: [SOURce<HW>]:INPut:TRIGger:IMPedance \n
		Snippet: driver.source.inputPy.trigger.set_impedance(impedance = enums.InputImpRf.G10K) \n
		No command help available \n
			:param impedance: No help available
		"""
		param = Conversions.enum_scalar_to_str(impedance, enums.InputImpRf)
		self._core.io.write(f'SOURce<HwInstance>:INPut:TRIGger:IMPedance {param}')

	def get_level(self) -> float:
		"""SCPI: [SOURce<HW>]:INPut:TRIGger:LEVel \n
		Snippet: value: float = driver.source.inputPy.trigger.get_level() \n
		No command help available \n
			:return: level: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:INPut:TRIGger:LEVel?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Trigger':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Trigger(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
