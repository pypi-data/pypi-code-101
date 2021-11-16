from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pulm:
	"""Pulm commands group definition. 13 total commands, 2 Sub-groups, 7 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pulm", core, parent)

	@property
	def double(self):
		"""double commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_double'):
			from .Double import Double
			self._double = Double(self._core, self._cmd_group)
		return self._double

	@property
	def trigger(self):
		"""trigger commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_trigger'):
			from .Trigger import Trigger
			self._trigger = Trigger(self._core, self._cmd_group)
		return self._trigger

	def get_delay(self) -> float:
		"""SCPI: [SOURce<HW>]:PULM:DELay \n
		Snippet: value: float = driver.source.pulm.get_delay() \n
		Sets the pulse delay. \n
			:return: delay: float Range: 0 to 100 s
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:PULM:DELay?')
		return Conversions.str_to_float(response)

	def set_delay(self, delay: float) -> None:
		"""SCPI: [SOURce<HW>]:PULM:DELay \n
		Snippet: driver.source.pulm.set_delay(delay = 1.0) \n
		Sets the pulse delay. \n
			:param delay: float Range: 0 to 100 s
		"""
		param = Conversions.decimal_value_to_str(delay)
		self._core.io.write(f'SOURce<HwInstance>:PULM:DELay {param}')

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.PulsMode:
		"""SCPI: [SOURce<HW>]:PULM:MODE \n
		Snippet: value: enums.PulsMode = driver.source.pulm.get_mode() \n
		Sets the mode of the pulse generator. \n
			:return: mode: SINGle| DOUBle SINGle Enables single pulse generation. DOUBle Enables double pulse generation. The two pulses are generated in one pulse period.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:PULM:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.PulsMode)

	def set_mode(self, mode: enums.PulsMode) -> None:
		"""SCPI: [SOURce<HW>]:PULM:MODE \n
		Snippet: driver.source.pulm.set_mode(mode = enums.PulsMode.DOUBle) \n
		Sets the mode of the pulse generator. \n
			:param mode: SINGle| DOUBle SINGle Enables single pulse generation. DOUBle Enables double pulse generation. The two pulses are generated in one pulse period.
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.PulsMode)
		self._core.io.write(f'SOURce<HwInstance>:PULM:MODE {param}')

	def get_period(self) -> float:
		"""SCPI: [SOURce<HW>]:PULM:PERiod \n
		Snippet: value: float = driver.source.pulm.get_period() \n
		Sets the period of the generated pulse. The period determines the repetition frequency of the internal signal. \n
			:return: period: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:PULM:PERiod?')
		return Conversions.str_to_float(response)

	def set_period(self, period: float) -> None:
		"""SCPI: [SOURce<HW>]:PULM:PERiod \n
		Snippet: driver.source.pulm.set_period(period = 1.0) \n
		Sets the period of the generated pulse. The period determines the repetition frequency of the internal signal. \n
			:param period: No help available
		"""
		param = Conversions.decimal_value_to_str(period)
		self._core.io.write(f'SOURce<HwInstance>:PULM:PERiod {param}')

	# noinspection PyTypeChecker
	def get_polarity(self) -> enums.NormalInverted:
		"""SCPI: [SOURce<HW>]:PULM:POLarity \n
		Snippet: value: enums.NormalInverted = driver.source.pulm.get_polarity() \n
		No command help available \n
			:return: polarity: NORMal| INVerted NORMal The RF signal is suppressed during the pulse pause. INVerted The RF signal is suppressed during the pulse.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:PULM:POLarity?')
		return Conversions.str_to_scalar_enum(response, enums.NormalInverted)

	def set_polarity(self, polarity: enums.NormalInverted) -> None:
		"""SCPI: [SOURce<HW>]:PULM:POLarity \n
		Snippet: driver.source.pulm.set_polarity(polarity = enums.NormalInverted.INVerted) \n
		No command help available \n
			:param polarity: NORMal| INVerted NORMal The RF signal is suppressed during the pulse pause. INVerted The RF signal is suppressed during the pulse.
		"""
		param = Conversions.enum_scalar_to_str(polarity, enums.NormalInverted)
		self._core.io.write(f'SOURce<HwInstance>:PULM:POLarity {param}')

	# noinspection PyTypeChecker
	def get_source(self) -> enums.SourceInt:
		"""SCPI: [SOURce<HW>]:PULM:SOURce \n
		Snippet: value: enums.SourceInt = driver.source.pulm.get_source() \n
		Selects the source for pulse modulation. \n
			:return: source: INTernal| EXTernal INTernal The internal pulse generator is used for the pulse modulation. EXTernal The signal applied externally via the trigger connector is used for the pulse modulation.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:PULM:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.SourceInt)

	def set_source(self, source: enums.SourceInt) -> None:
		"""SCPI: [SOURce<HW>]:PULM:SOURce \n
		Snippet: driver.source.pulm.set_source(source = enums.SourceInt.EXTernal) \n
		Selects the source for pulse modulation. \n
			:param source: INTernal| EXTernal INTernal The internal pulse generator is used for the pulse modulation. EXTernal The signal applied externally via the trigger connector is used for the pulse modulation.
		"""
		param = Conversions.enum_scalar_to_str(source, enums.SourceInt)
		self._core.io.write(f'SOURce<HwInstance>:PULM:SOURce {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:PULM:STATe \n
		Snippet: value: bool = driver.source.pulm.get_state() \n
		Activates the pulse modulation. \n
			:return: state: 0| 1| OFF| ON
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:PULM:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:PULM:STATe \n
		Snippet: driver.source.pulm.set_state(state = False) \n
		Activates the pulse modulation. \n
			:param state: 0| 1| OFF| ON
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:PULM:STATe {param}')

	def get_width(self) -> float:
		"""SCPI: [SOURce<HW>]:PULM:WIDTh \n
		Snippet: value: float = driver.source.pulm.get_width() \n
		Sets the width of the generated pulse. The width determines the pulse length. The pulse width must be at least 20ns less
		than the set pulse period. \n
			:return: width: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:PULM:WIDTh?')
		return Conversions.str_to_float(response)

	def set_width(self, width: float) -> None:
		"""SCPI: [SOURce<HW>]:PULM:WIDTh \n
		Snippet: driver.source.pulm.set_width(width = 1.0) \n
		Sets the width of the generated pulse. The width determines the pulse length. The pulse width must be at least 20ns less
		than the set pulse period. \n
			:param width: No help available
		"""
		param = Conversions.decimal_value_to_str(width)
		self._core.io.write(f'SOURce<HwInstance>:PULM:WIDTh {param}')

	def clone(self) -> 'Pulm':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pulm(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
