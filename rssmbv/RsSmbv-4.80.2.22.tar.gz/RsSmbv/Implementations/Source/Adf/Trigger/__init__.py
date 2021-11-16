from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Trigger:
	"""Trigger commands group definition. 9 total commands, 3 Sub-groups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("trigger", core, parent)

	@property
	def arm(self):
		"""arm commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_arm'):
			from .Arm import Arm
			self._arm = Arm(self._core, self._cmd_group)
		return self._arm

	@property
	def execute(self):
		"""execute commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_execute'):
			from .Execute import Execute
			self._execute = Execute(self._core, self._cmd_group)
		return self._execute

	@property
	def external(self):
		"""external commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_external'):
			from .External import External
			self._external = External(self._core, self._cmd_group)
		return self._external

	# noinspection PyTypeChecker
	def get_rmode(self) -> enums.TrigRunMode:
		"""SCPI: [SOURce<HW>]:ADF:TRIGger:RMODe \n
		Snippet: value: enums.TrigRunMode = driver.source.adf.trigger.get_rmode() \n
		No command help available \n
			:return: run_mode: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:ADF:TRIGger:RMODe?')
		return Conversions.str_to_scalar_enum(response, enums.TrigRunMode)

	def get_slength(self) -> int:
		"""SCPI: [SOURce<HW>]:ADF:TRIGger:SLENgth \n
		Snippet: value: int = driver.source.adf.trigger.get_slength() \n
		No command help available \n
			:return: seq_length: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:ADF:TRIGger:SLENgth?')
		return Conversions.str_to_int(response)

	def set_slength(self, seq_length: int) -> None:
		"""SCPI: [SOURce<HW>]:ADF:TRIGger:SLENgth \n
		Snippet: driver.source.adf.trigger.set_slength(seq_length = 1) \n
		No command help available \n
			:param seq_length: No help available
		"""
		param = Conversions.decimal_value_to_str(seq_length)
		self._core.io.write(f'SOURce<HwInstance>:ADF:TRIGger:SLENgth {param}')

	# noinspection PyTypeChecker
	def get_source(self) -> enums.TriggerSourceA:
		"""SCPI: [SOURce<HW>]:ADF:TRIGger:SOURce \n
		Snippet: value: enums.TriggerSourceA = driver.source.adf.trigger.get_source() \n
		No command help available \n
			:return: trigger_source: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:ADF:TRIGger:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.TriggerSourceA)

	def set_source(self, trigger_source: enums.TriggerSourceA) -> None:
		"""SCPI: [SOURce<HW>]:ADF:TRIGger:SOURce \n
		Snippet: driver.source.adf.trigger.set_source(trigger_source = enums.TriggerSourceA.BBSY) \n
		No command help available \n
			:param trigger_source: No help available
		"""
		param = Conversions.enum_scalar_to_str(trigger_source, enums.TriggerSourceA)
		self._core.io.write(f'SOURce<HwInstance>:ADF:TRIGger:SOURce {param}')

	# noinspection PyTypeChecker
	def get_sequence(self) -> enums.DmTrigMode:
		"""SCPI: [SOURce<HW>]:ADF:[TRIGger]:SEQuence \n
		Snippet: value: enums.DmTrigMode = driver.source.adf.trigger.get_sequence() \n
		No command help available \n
			:return: trigger_mode: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:ADF:TRIGger:SEQuence?')
		return Conversions.str_to_scalar_enum(response, enums.DmTrigMode)

	def set_sequence(self, trigger_mode: enums.DmTrigMode) -> None:
		"""SCPI: [SOURce<HW>]:ADF:[TRIGger]:SEQuence \n
		Snippet: driver.source.adf.trigger.set_sequence(trigger_mode = enums.DmTrigMode.AAUTo) \n
		No command help available \n
			:param trigger_mode: No help available
		"""
		param = Conversions.enum_scalar_to_str(trigger_mode, enums.DmTrigMode)
		self._core.io.write(f'SOURce<HwInstance>:ADF:TRIGger:SEQuence {param}')

	def clone(self) -> 'Trigger':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Trigger(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
