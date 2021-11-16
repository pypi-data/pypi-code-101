from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Power:
	"""Power commands group definition. 7 total commands, 2 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("power", core, parent)

	@property
	def noise(self):
		"""noise commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_noise'):
			from .Noise import Noise
			self._noise = Noise(self._core, self._cmd_group)
		return self._noise

	@property
	def sum(self):
		"""sum commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_sum'):
			from .Sum import Sum
			self._sum = Sum(self._core, self._cmd_group)
		return self._sum

	def get_carrier(self) -> float:
		"""SCPI: [SOURce<HW>]:AWGN:POWer:CARRier \n
		Snippet: value: float = driver.source.awgn.power.get_carrier() \n
		available for Additive Noise and CW Interferer (SOUR:AWGN:MODE ADD|CW) modes
			INTRO_CMD_HELP: Sets/queries the carrier or signal power depending on the selected reference mode. \n
			- SOUR:AWGN:POW:RMOD CARR Sets the carrier power. The power of the noise signal is derived from the entered C/N value.
			- SOUR:AWGN:POW:RMOD NOIS queries the carrier power which is derived from the entered C/N value. The noise power is set with command SOUR:AWGN:POW:NOISe. \n
			:return: carrier: float Unit: dBm
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:AWGN:POWer:CARRier?')
		return Conversions.str_to_float(response)

	def set_carrier(self, carrier: float) -> None:
		"""SCPI: [SOURce<HW>]:AWGN:POWer:CARRier \n
		Snippet: driver.source.awgn.power.set_carrier(carrier = 1.0) \n
		available for Additive Noise and CW Interferer (SOUR:AWGN:MODE ADD|CW) modes
			INTRO_CMD_HELP: Sets/queries the carrier or signal power depending on the selected reference mode. \n
			- SOUR:AWGN:POW:RMOD CARR Sets the carrier power. The power of the noise signal is derived from the entered C/N value.
			- SOUR:AWGN:POW:RMOD NOIS queries the carrier power which is derived from the entered C/N value. The noise power is set with command SOUR:AWGN:POW:NOISe. \n
			:param carrier: float Unit: dBm
		"""
		param = Conversions.decimal_value_to_str(carrier)
		self._core.io.write(f'SOURce<HwInstance>:AWGN:POWer:CARRier {param}')

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.NoisAwgnPowMode:
		"""SCPI: [SOURce<HW>]:AWGN:POWer:MODE \n
		Snippet: value: enums.NoisAwgnPowMode = driver.source.awgn.power.get_mode() \n
		In Additive Noise (SOUR:AWGN:MODE ADD) mode, selects the mode for setting the noise power. \n
			:return: mode: CN| SN | EN CN|SN The noise power is set on the basis of the value entered for the carrier/noise or signal/noise ratio (SOURce:AWGN:CNRatio|SNRatio) . EN The noise power is set on the basis of the value entered for the ratio of bit energy to noise power density (AWGN:ENR) .
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:AWGN:POWer:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.NoisAwgnPowMode)

	def set_mode(self, mode: enums.NoisAwgnPowMode) -> None:
		"""SCPI: [SOURce<HW>]:AWGN:POWer:MODE \n
		Snippet: driver.source.awgn.power.set_mode(mode = enums.NoisAwgnPowMode.CN) \n
		In Additive Noise (SOUR:AWGN:MODE ADD) mode, selects the mode for setting the noise power. \n
			:param mode: CN| SN | EN CN|SN The noise power is set on the basis of the value entered for the carrier/noise or signal/noise ratio (SOURce:AWGN:CNRatio|SNRatio) . EN The noise power is set on the basis of the value entered for the ratio of bit energy to noise power density (AWGN:ENR) .
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.NoisAwgnPowMode)
		self._core.io.write(f'SOURce<HwInstance>:AWGN:POWer:MODE {param}')

	# noinspection PyTypeChecker
	def get_rmode(self) -> enums.NoisAwgnPowRefMode:
		"""SCPI: [SOURce<HW>]:AWGN:POWer:RMODe \n
		Snippet: value: enums.NoisAwgnPowRefMode = driver.source.awgn.power.get_rmode() \n
		In Additive Noise and CW Interferer (SOUR:AWGN:MODE ADD|CW) modes and Display Mode set to RF (AWGN:DISP:MODE RF) ,
		selects the mode for setting the interfering signal. \n
			:return: rmode: CARRier| NOISe CARRier The carrier power is kept constant when the C/N value or Eb/N0 value is changed. The noise power is adjusted. NOISe The noise power is kept constant when the C/N value or Eb/N0 value is changed. The carrier power is adjusted.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:AWGN:POWer:RMODe?')
		return Conversions.str_to_scalar_enum(response, enums.NoisAwgnPowRefMode)

	def set_rmode(self, rmode: enums.NoisAwgnPowRefMode) -> None:
		"""SCPI: [SOURce<HW>]:AWGN:POWer:RMODe \n
		Snippet: driver.source.awgn.power.set_rmode(rmode = enums.NoisAwgnPowRefMode.CARRier) \n
		In Additive Noise and CW Interferer (SOUR:AWGN:MODE ADD|CW) modes and Display Mode set to RF (AWGN:DISP:MODE RF) ,
		selects the mode for setting the interfering signal. \n
			:param rmode: CARRier| NOISe CARRier The carrier power is kept constant when the C/N value or Eb/N0 value is changed. The noise power is adjusted. NOISe The noise power is kept constant when the C/N value or Eb/N0 value is changed. The carrier power is adjusted.
		"""
		param = Conversions.enum_scalar_to_str(rmode, enums.NoisAwgnPowRefMode)
		self._core.io.write(f'SOURce<HwInstance>:AWGN:POWer:RMODe {param}')

	def clone(self) -> 'Power':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Power(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
