from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Utilities import trim_str_response
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bbin:
	"""Bbin commands group definition. 23 total commands, 7 Sub-groups, 10 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bbin", core, parent)

	@property
	def alevel(self):
		"""alevel commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_alevel'):
			from .Alevel import Alevel
			self._alevel = Alevel(self._core, self._cmd_group)
		return self._alevel

	@property
	def digital(self):
		"""digital commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_digital'):
			from .Digital import Digital
			self._digital = Digital(self._core, self._cmd_group)
		return self._digital

	@property
	def iqswap(self):
		"""iqswap commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_iqswap'):
			from .Iqswap import Iqswap
			self._iqswap = Iqswap(self._core, self._cmd_group)
		return self._iqswap

	@property
	def offset(self):
		"""offset commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_offset'):
			from .Offset import Offset
			self._offset = Offset(self._core, self._cmd_group)
		return self._offset

	@property
	def oload(self):
		"""oload commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_oload'):
			from .Oload import Oload
			self._oload = Oload(self._core, self._cmd_group)
		return self._oload

	@property
	def power(self):
		"""power commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_power'):
			from .Power import Power
			self._power = Power(self._core, self._cmd_group)
		return self._power

	@property
	def symbolRate(self):
		"""symbolRate commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_symbolRate'):
			from .SymbolRate import SymbolRate
			self._symbolRate = SymbolRate(self._core, self._cmd_group)
		return self._symbolRate

	def get_cdevice(self) -> str:
		"""SCPI: [SOURce<HW>]:BBIN:CDEVice \n
		Snippet: value: str = driver.source.bbin.get_cdevice() \n
		Digital Input only. Indicates the ID of an externally connected R&S Instrument or R&S Device. \n
			:return: cdevice: string
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BBIN:CDEVice?')
		return trim_str_response(response)

	def get_cfactor(self) -> float:
		"""SCPI: [SOURce<HW>]:BBIN:CFACtor \n
		Snippet: value: float = driver.source.bbin.get_cfactor() \n
		This command enters the crest factor of the external baseband signal. \n
			:return: cfactor: float Range: 0 to 30, Unit: dB
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BBIN:CFACtor?')
		return Conversions.str_to_float(response)

	def set_cfactor(self, cfactor: float) -> None:
		"""SCPI: [SOURce<HW>]:BBIN:CFACtor \n
		Snippet: driver.source.bbin.set_cfactor(cfactor = 1.0) \n
		This command enters the crest factor of the external baseband signal. \n
			:param cfactor: float Range: 0 to 30, Unit: dB
		"""
		param = Conversions.decimal_value_to_str(cfactor)
		self._core.io.write(f'SOURce<HwInstance>:BBIN:CFACtor {param}')

	def get_foffset(self) -> float:
		"""SCPI: [SOURce<HW>]:BBIN:FOFFset \n
		Snippet: value: float = driver.source.bbin.get_foffset() \n
		Enters the frequency offset for the external baseband signal. The complex I/Q bandwidth of the shifted useful signal must
		not exceed the total available baseband bandwidth (see data sheet) . \n
			:return: foffset: float Range: -40E6 to 40E6, Unit: Hz
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BBIN:FOFFset?')
		return Conversions.str_to_float(response)

	def set_foffset(self, foffset: float) -> None:
		"""SCPI: [SOURce<HW>]:BBIN:FOFFset \n
		Snippet: driver.source.bbin.set_foffset(foffset = 1.0) \n
		Enters the frequency offset for the external baseband signal. The complex I/Q bandwidth of the shifted useful signal must
		not exceed the total available baseband bandwidth (see data sheet) . \n
			:param foffset: float Range: -40E6 to 40E6, Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(foffset)
		self._core.io.write(f'SOURce<HwInstance>:BBIN:FOFFset {param}')

	def get_gimbalance(self) -> float:
		"""SCPI: [SOURce<HW>]:BBIN:GIMBalance \n
		Snippet: value: float = driver.source.bbin.get_gimbalance() \n
		This command enters a gain to the Q component of the external baseband signal. \n
			:return: gimbalance: float Range: -3 to 3, Unit: dB
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BBIN:GIMBalance?')
		return Conversions.str_to_float(response)

	def set_gimbalance(self, gimbalance: float) -> None:
		"""SCPI: [SOURce<HW>]:BBIN:GIMBalance \n
		Snippet: driver.source.bbin.set_gimbalance(gimbalance = 1.0) \n
		This command enters a gain to the Q component of the external baseband signal. \n
			:param gimbalance: float Range: -3 to 3, Unit: dB
		"""
		param = Conversions.decimal_value_to_str(gimbalance)
		self._core.io.write(f'SOURce<HwInstance>:BBIN:GIMBalance {param}')

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.AnalogDigitalMode:
		"""SCPI: [SOURce<HW>]:BBIN:MODE \n
		Snippet: value: enums.AnalogDigitalMode = driver.source.bbin.get_mode() \n
		This command selects the external input signal mode for the 'Baseband In' block. \n
			:return: mode: ANALog| DIGital ANALog The external analog baseband signal is supplied via the inputs I and Q. DIGItal The external digital baseband signal is fed into the signal path via the 'Digital Input' connector. The internal signal processing is based on a sample rate of 100 MHz. Input signals with a sample rate less than 100 MHz are upsampled. The sample rate can be estimated or defined by the user in the appropriate entry fields.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BBIN:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.AnalogDigitalMode)

	def set_mode(self, mode: enums.AnalogDigitalMode) -> None:
		"""SCPI: [SOURce<HW>]:BBIN:MODE \n
		Snippet: driver.source.bbin.set_mode(mode = enums.AnalogDigitalMode.ANALog) \n
		This command selects the external input signal mode for the 'Baseband In' block. \n
			:param mode: ANALog| DIGital ANALog The external analog baseband signal is supplied via the inputs I and Q. DIGItal The external digital baseband signal is fed into the signal path via the 'Digital Input' connector. The internal signal processing is based on a sample rate of 100 MHz. Input signals with a sample rate less than 100 MHz are upsampled. The sample rate can be estimated or defined by the user in the appropriate entry fields.
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.AnalogDigitalMode)
		self._core.io.write(f'SOURce<HwInstance>:BBIN:MODE {param}')

	def get_mperiod(self) -> int:
		"""SCPI: [SOURce<HW>]:BBIN:MPERiod \n
		Snippet: value: int = driver.source.bbin.get_mperiod() \n
		Sets the recording duration for measuring the baseband input signal by Auto Level Set. \n
			:return: mperiod: integer Range: 1 to 32, Unit: s
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BBIN:MPERiod?')
		return Conversions.str_to_int(response)

	def set_mperiod(self, mperiod: int) -> None:
		"""SCPI: [SOURce<HW>]:BBIN:MPERiod \n
		Snippet: driver.source.bbin.set_mperiod(mperiod = 1) \n
		Sets the recording duration for measuring the baseband input signal by Auto Level Set. \n
			:param mperiod: integer Range: 1 to 32, Unit: s
		"""
		param = Conversions.decimal_value_to_str(mperiod)
		self._core.io.write(f'SOURce<HwInstance>:BBIN:MPERiod {param}')

	def get_odelay(self) -> float:
		"""SCPI: [SOURce<HW>]:BBIN:ODELay \n
		Snippet: value: float = driver.source.bbin.get_odelay() \n
		Seds the output delay of the external baseband signal. \n
			:return: delay: float Range: 0 to 1
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BBIN:ODELay?')
		return Conversions.str_to_float(response)

	def set_odelay(self, delay: float) -> None:
		"""SCPI: [SOURce<HW>]:BBIN:ODELay \n
		Snippet: driver.source.bbin.set_odelay(delay = 1.0) \n
		Seds the output delay of the external baseband signal. \n
			:param delay: float Range: 0 to 1
		"""
		param = Conversions.decimal_value_to_str(delay)
		self._core.io.write(f'SOURce<HwInstance>:BBIN:ODELay {param}')

	def get_pgain(self) -> float:
		"""SCPI: [SOURce<HW>]:BBIN:PGAin \n
		Snippet: value: float = driver.source.bbin.get_pgain() \n
		This command enters the relative gain for the external baseband signal compared with the signals of the other baseband
		sources. The actual gain of the different baseband signals depends not only on the path gain setting but also on the
		signal characteristics such as the crest factor and on the number of used sources. used and on the total RF output power.
		The gain affects the signal on the 'Baseband' In block output. \n
			:return: pgain: float Range: -50 to 50, Unit: dB
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BBIN:PGAin?')
		return Conversions.str_to_float(response)

	def set_pgain(self, pgain: float) -> None:
		"""SCPI: [SOURce<HW>]:BBIN:PGAin \n
		Snippet: driver.source.bbin.set_pgain(pgain = 1.0) \n
		This command enters the relative gain for the external baseband signal compared with the signals of the other baseband
		sources. The actual gain of the different baseband signals depends not only on the path gain setting but also on the
		signal characteristics such as the crest factor and on the number of used sources. used and on the total RF output power.
		The gain affects the signal on the 'Baseband' In block output. \n
			:param pgain: float Range: -50 to 50, Unit: dB
		"""
		param = Conversions.decimal_value_to_str(pgain)
		self._core.io.write(f'SOURce<HwInstance>:BBIN:PGAin {param}')

	def get_skew(self) -> float:
		"""SCPI: [SOURce<HW>]:BBIN:SKEW \n
		Snippet: value: float = driver.source.bbin.get_skew() \n
		This command determines the delay between Q and I channel. Positive values represent a delay for Q versus I. \n
			:return: skew: float Range: -1E-9 to 1E-9, Unit: s
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BBIN:SKEW?')
		return Conversions.str_to_float(response)

	def set_skew(self, skew: float) -> None:
		"""SCPI: [SOURce<HW>]:BBIN:SKEW \n
		Snippet: driver.source.bbin.set_skew(skew = 1.0) \n
		This command determines the delay between Q and I channel. Positive values represent a delay for Q versus I. \n
			:param skew: float Range: -1E-9 to 1E-9, Unit: s
		"""
		param = Conversions.decimal_value_to_str(skew)
		self._core.io.write(f'SOURce<HwInstance>:BBIN:SKEW {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BBIN:STATe \n
		Snippet: value: bool = driver.source.bbin.get_state() \n
		This command switches the feeding of an external analog signal into the signal path on/off. \n
			:return: state: 0| 1| OFF| ON
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BBIN:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BBIN:STATe \n
		Snippet: driver.source.bbin.set_state(state = False) \n
		This command switches the feeding of an external analog signal into the signal path on/off. \n
			:param state: 0| 1| OFF| ON
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BBIN:STATe {param}')

	def clone(self) -> 'Bbin':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Bbin(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
