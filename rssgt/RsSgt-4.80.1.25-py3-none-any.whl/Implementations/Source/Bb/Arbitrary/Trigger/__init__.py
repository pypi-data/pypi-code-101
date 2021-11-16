from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Trigger:
	"""Trigger commands group definition. 18 total commands, 6 Sub-groups, 6 group commands"""

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
	def delay(self):
		"""delay commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_delay'):
			from .Delay import Delay
			self._delay = Delay(self._core, self._cmd_group)
		return self._delay

	@property
	def execute(self):
		"""execute commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_execute'):
			from .Execute import Execute
			self._execute = Execute(self._core, self._cmd_group)
		return self._execute

	@property
	def obaseband(self):
		"""obaseband commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_obaseband'):
			from .Obaseband import Obaseband
			self._obaseband = Obaseband(self._core, self._cmd_group)
		return self._obaseband

	@property
	def output(self):
		"""output commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_output'):
			from .Output import Output
			self._output = Output(self._core, self._cmd_group)
		return self._output

	@property
	def external(self):
		"""external commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_external'):
			from .External import External
			self._external = External(self._core, self._cmd_group)
		return self._external

	# noinspection PyTypeChecker
	def get_rmode(self) -> enums.TrigRunMode:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:TRIGger:RMODe \n
		Snippet: value: enums.TrigRunMode = driver.source.bb.arbitrary.trigger.get_rmode() \n
		The command queries the status of waveform output or all trigger modes with ARB on. \n
			:return: rmode: STOP| RUN RUN The waveform is output. A trigger event occurred in the triggered mode. STOP The waveform is not output. A trigger event did not occur in the triggered modes, or waveform output was stopped by the command:BB:ARB:TRIG:ARM:EXECute (armed trigger modes only) .
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ARBitrary:TRIGger:RMODe?')
		return Conversions.str_to_scalar_enum(response, enums.TrigRunMode)

	def get_slength(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:TRIGger:SLENgth \n
		Snippet: value: int = driver.source.bb.arbitrary.trigger.get_slength() \n
		The command defines the length of the signal sequence to be output in the Single trigger mode. The unit is defined with
		command SOUR:BB:ARB:TRIG:SLUNit. It is possible to output deliberately just part of the waveform, an exact sequence of
		the waveform, or a defined number of repetitions of the waveform. \n
			:return: slength: integer Range: 1 to dynamic, Unit: sample
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ARBitrary:TRIGger:SLENgth?')
		return Conversions.str_to_int(response)

	def set_slength(self, slength: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:TRIGger:SLENgth \n
		Snippet: driver.source.bb.arbitrary.trigger.set_slength(slength = 1) \n
		The command defines the length of the signal sequence to be output in the Single trigger mode. The unit is defined with
		command SOUR:BB:ARB:TRIG:SLUNit. It is possible to output deliberately just part of the waveform, an exact sequence of
		the waveform, or a defined number of repetitions of the waveform. \n
			:param slength: integer Range: 1 to dynamic, Unit: sample
		"""
		param = Conversions.decimal_value_to_str(slength)
		self._core.io.write(f'SOURce<HwInstance>:BB:ARBitrary:TRIGger:SLENgth {param}')

	# noinspection PyTypeChecker
	def get_sl_unit(self) -> enums.UnitSlB:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:TRIGger:SLUNit \n
		Snippet: value: enums.UnitSlB = driver.source.bb.arbitrary.trigger.get_sl_unit() \n
		The command defines the unit for the entry of the length of the signal sequence (SOUR:BB:ARB:TRIG:SLEN) to be output in
		the 'Single' trigger mode (SOUR:BB:ARB:SEQ SING) . \n
			:return: sl_unit: SEQuence| SAMPle
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ARBitrary:TRIGger:SLUNit?')
		return Conversions.str_to_scalar_enum(response, enums.UnitSlB)

	def set_sl_unit(self, sl_unit: enums.UnitSlB) -> None:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:TRIGger:SLUNit \n
		Snippet: driver.source.bb.arbitrary.trigger.set_sl_unit(sl_unit = enums.UnitSlB.SAMPle) \n
		The command defines the unit for the entry of the length of the signal sequence (SOUR:BB:ARB:TRIG:SLEN) to be output in
		the 'Single' trigger mode (SOUR:BB:ARB:SEQ SING) . \n
			:param sl_unit: SEQuence| SAMPle
		"""
		param = Conversions.enum_scalar_to_str(sl_unit, enums.UnitSlB)
		self._core.io.write(f'SOURce<HwInstance>:BB:ARBitrary:TRIGger:SLUNit {param}')

	# noinspection PyTypeChecker
	def get_smode(self) -> enums.ArbTrigSegmModeNoEhop:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:TRIGger:SMODe \n
		Snippet: value: enums.ArbTrigSegmModeNoEhop = driver.source.bb.arbitrary.trigger.get_smode() \n
		The command selects the extended trigger mode for multi segment waveforms. \n
			:return: smode: SAME| NEXT| NSEam| SEQuencer NSEam = Next Segment Seamless
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ARBitrary:TRIGger:SMODe?')
		return Conversions.str_to_scalar_enum(response, enums.ArbTrigSegmModeNoEhop)

	def set_smode(self, smode: enums.ArbTrigSegmModeNoEhop) -> None:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:TRIGger:SMODe \n
		Snippet: driver.source.bb.arbitrary.trigger.set_smode(smode = enums.ArbTrigSegmModeNoEhop.NEXT) \n
		The command selects the extended trigger mode for multi segment waveforms. \n
			:param smode: SAME| NEXT| NSEam| SEQuencer NSEam = Next Segment Seamless
		"""
		param = Conversions.enum_scalar_to_str(smode, enums.ArbTrigSegmModeNoEhop)
		self._core.io.write(f'SOURce<HwInstance>:BB:ARBitrary:TRIGger:SMODe {param}')

	# noinspection PyTypeChecker
	def get_source(self) -> enums.TriggerSourceB:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:TRIGger:SOURce \n
		Snippet: value: enums.TriggerSourceB = driver.source.bb.arbitrary.trigger.get_source() \n
		Selects the trigger source. \n
			:return: source: INTernal| EXTernal INTernal manual trigger or *TRG. EXTernal trigger signal on the USER 1/2 connector.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ARBitrary:TRIGger:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.TriggerSourceB)

	def set_source(self, source: enums.TriggerSourceB) -> None:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:TRIGger:SOURce \n
		Snippet: driver.source.bb.arbitrary.trigger.set_source(source = enums.TriggerSourceB.BEXTernal) \n
		Selects the trigger source. \n
			:param source: INTernal| EXTernal INTernal manual trigger or *TRG. EXTernal trigger signal on the USER 1/2 connector.
		"""
		param = Conversions.enum_scalar_to_str(source, enums.TriggerSourceB)
		self._core.io.write(f'SOURce<HwInstance>:BB:ARBitrary:TRIGger:SOURce {param}')

	# noinspection PyTypeChecker
	def get_sequence(self) -> enums.DmTrigMode:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:[TRIGger]:SEQuence \n
		Snippet: value: enums.DmTrigMode = driver.source.bb.arbitrary.trigger.get_sequence() \n
		The command selects the trigger mode. \n
			:return: sequence: AUTO| RETRigger| AAUTo| ARETrigger| SINGle AUTO The waveform is output continuously. RETRigger The waveform is output continuously. A trigger event (internal or external) causes a restart. AAUTo The waveform is output only when a trigger event occurs. After the trigger event the waveform is output continuously. Waveform output is stopped with command SOUR:BB:ARB:TRIG:ARM:EXEC and started again when a trigger event occurs. ARETrigger The waveform is output only when a trigger event occurs. The device automatically toggles to RETRIG mode. Every subsequent trigger event causes a restart. Waveform output is stopped with command SOUR:BB:ARB:TRIG:ARM:EXEC and started again when a trigger event occurs. SINGle The waveform is output only when a trigger event occurs. After the trigger event the waveform is output once to the set sequence length (SOUR:BB:ARB:TRIG:SLEN) . Every subsequent trigger event causes a restart.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ARBitrary:TRIGger:SEQuence?')
		return Conversions.str_to_scalar_enum(response, enums.DmTrigMode)

	def set_sequence(self, sequence: enums.DmTrigMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:[TRIGger]:SEQuence \n
		Snippet: driver.source.bb.arbitrary.trigger.set_sequence(sequence = enums.DmTrigMode.AAUTo) \n
		The command selects the trigger mode. \n
			:param sequence: AUTO| RETRigger| AAUTo| ARETrigger| SINGle AUTO The waveform is output continuously. RETRigger The waveform is output continuously. A trigger event (internal or external) causes a restart. AAUTo The waveform is output only when a trigger event occurs. After the trigger event the waveform is output continuously. Waveform output is stopped with command SOUR:BB:ARB:TRIG:ARM:EXEC and started again when a trigger event occurs. ARETrigger The waveform is output only when a trigger event occurs. The device automatically toggles to RETRIG mode. Every subsequent trigger event causes a restart. Waveform output is stopped with command SOUR:BB:ARB:TRIG:ARM:EXEC and started again when a trigger event occurs. SINGle The waveform is output only when a trigger event occurs. After the trigger event the waveform is output once to the set sequence length (SOUR:BB:ARB:TRIG:SLEN) . Every subsequent trigger event causes a restart.
		"""
		param = Conversions.enum_scalar_to_str(sequence, enums.DmTrigMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:ARBitrary:TRIGger:SEQuence {param}')

	def clone(self) -> 'Trigger':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Trigger(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
