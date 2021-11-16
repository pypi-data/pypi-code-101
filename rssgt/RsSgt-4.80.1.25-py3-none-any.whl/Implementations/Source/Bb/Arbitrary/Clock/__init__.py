from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Clock:
	"""Clock commands group definition. 6 total commands, 1 Sub-groups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("clock", core, parent)

	@property
	def synchronization(self):
		"""synchronization commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_synchronization'):
			from .Synchronization import Synchronization
			self._synchronization = Synchronization(self._core, self._cmd_group)
		return self._synchronization

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.ArbClockMode:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:CLOCk:MODE \n
		Snippet: value: enums.ArbClockMode = driver.source.bb.arbitrary.clock.get_mode() \n
		The command enters the type of externally supplied clock (BB:ARB:CLOCk:SOURce EXTernal) . When MSAMple is used,
		a multiple of the sample clock is supplied via the CLOCK connector and the sample clock is derived internally from this.
		The multiplier is entered with the command BB:ARB:CLOCk:MULTiplier. \n
			:return: mode: SAMPle| MSAMple
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ARBitrary:CLOCk:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.ArbClockMode)

	def set_mode(self, mode: enums.ArbClockMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:CLOCk:MODE \n
		Snippet: driver.source.bb.arbitrary.clock.set_mode(mode = enums.ArbClockMode.MSAMple) \n
		The command enters the type of externally supplied clock (BB:ARB:CLOCk:SOURce EXTernal) . When MSAMple is used,
		a multiple of the sample clock is supplied via the CLOCK connector and the sample clock is derived internally from this.
		The multiplier is entered with the command BB:ARB:CLOCk:MULTiplier. \n
			:param mode: SAMPle| MSAMple
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.ArbClockMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:ARBitrary:CLOCk:MODE {param}')

	def get_multiplier(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:CLOCk:MULTiplier \n
		Snippet: value: int = driver.source.bb.arbitrary.clock.get_multiplier() \n
		The command specifies the multiplier for clock type 'Multiple Samples' (BB:ARB:CLOCk:MODE MSAM) in the case of an
		external clock source. \n
			:return: multiplier: integer Range: 1 to 64
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ARBitrary:CLOCk:MULTiplier?')
		return Conversions.str_to_int(response)

	def set_multiplier(self, multiplier: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:CLOCk:MULTiplier \n
		Snippet: driver.source.bb.arbitrary.clock.set_multiplier(multiplier = 1) \n
		The command specifies the multiplier for clock type 'Multiple Samples' (BB:ARB:CLOCk:MODE MSAM) in the case of an
		external clock source. \n
			:param multiplier: integer Range: 1 to 64
		"""
		param = Conversions.decimal_value_to_str(multiplier)
		self._core.io.write(f'SOURce<HwInstance>:BB:ARBitrary:CLOCk:MULTiplier {param}')

	# noinspection PyTypeChecker
	def get_source(self) -> enums.ClocSourBb:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:CLOCk:SOURce \n
		Snippet: value: enums.ClocSourBb = driver.source.bb.arbitrary.clock.get_source() \n
		Sets the source for the digital modulation clock. \n
			:return: source: INTernal| EXTernal INTernal The internal clock reference is used. EXTernal The external clock reference is supplied to the connector.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ARBitrary:CLOCk:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.ClocSourBb)

	def set_source(self, source: enums.ClocSourBb) -> None:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:CLOCk:SOURce \n
		Snippet: driver.source.bb.arbitrary.clock.set_source(source = enums.ClocSourBb.AINTernal) \n
		Sets the source for the digital modulation clock. \n
			:param source: INTernal| EXTernal INTernal The internal clock reference is used. EXTernal The external clock reference is supplied to the connector.
		"""
		param = Conversions.enum_scalar_to_str(source, enums.ClocSourBb)
		self._core.io.write(f'SOURce<HwInstance>:BB:ARBitrary:CLOCk:SOURce {param}')

	def get_value(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:CLOCk \n
		Snippet: value: float = driver.source.bb.arbitrary.clock.get_value() \n
		The command sets the clock rate in samples. Loading a waveform waveform (ARB:WAV:SEL <name>) sets the clock rate that is
		defined in the waveform tag 'clock'. The command subsequently changes the clock rate; see data sheet for value range. In
		the case of an external clock source (selection ARB:CLOCk:SOURce EXTernal) the clock for the external source must be
		entered with this command. \n
			:return: clock: float
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ARBitrary:CLOCk?')
		return Conversions.str_to_float(response)

	def set_value(self, clock: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:CLOCk \n
		Snippet: driver.source.bb.arbitrary.clock.set_value(clock = 1.0) \n
		The command sets the clock rate in samples. Loading a waveform waveform (ARB:WAV:SEL <name>) sets the clock rate that is
		defined in the waveform tag 'clock'. The command subsequently changes the clock rate; see data sheet for value range. In
		the case of an external clock source (selection ARB:CLOCk:SOURce EXTernal) the clock for the external source must be
		entered with this command. \n
			:param clock: float
		"""
		param = Conversions.decimal_value_to_str(clock)
		self._core.io.write(f'SOURce<HwInstance>:BB:ARBitrary:CLOCk {param}')

	def clone(self) -> 'Clock':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Clock(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
