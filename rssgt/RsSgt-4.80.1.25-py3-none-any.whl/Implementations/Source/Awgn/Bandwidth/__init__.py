from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bandwidth:
	"""Bandwidth commands group definition. 4 total commands, 1 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bandwidth", core, parent)

	@property
	def coupling(self):
		"""coupling commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_coupling'):
			from .Coupling import Coupling
			self._coupling = Coupling(self._core, self._cmd_group)
		return self._coupling

	def get_noise(self) -> float:
		"""SCPI: [SOURce<HW>]:AWGN:BWIDth:NOISe \n
		Snippet: value: float = driver.source.awgn.bandwidth.get_noise() \n
		This command is available for modes In Additive Noise and Noise Only (SOUR:AWGN:MODE ADD|ONLY) modes, queries the real
		noise bandwidth. \n
			:return: noise: float Range: 0 to 200E6
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:AWGN:BWIDth:NOISe?')
		return Conversions.str_to_float(response)

	def get_ratio(self) -> float:
		"""SCPI: [SOURce<HW>]:AWGN:BWIDth:RATio \n
		Snippet: value: float = driver.source.awgn.bandwidth.get_ratio() \n
		In Additive Noise and Noise Only (SOUR:AWGN:MODE ADD|ONLY) modes, sets the ratio of minimum real noise bandwidth to
		system bandwidth. The overall bandwidth is calculated as follows and may not exceed the total bandwidth specified in the
		data sheet: Overall Bandwidth = System BW x Min Noise/System BW Ratio \n
			:return: ratio: float Range: 1 to Max
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:AWGN:BWIDth:RATio?')
		return Conversions.str_to_float(response)

	def set_ratio(self, ratio: float) -> None:
		"""SCPI: [SOURce<HW>]:AWGN:BWIDth:RATio \n
		Snippet: driver.source.awgn.bandwidth.set_ratio(ratio = 1.0) \n
		In Additive Noise and Noise Only (SOUR:AWGN:MODE ADD|ONLY) modes, sets the ratio of minimum real noise bandwidth to
		system bandwidth. The overall bandwidth is calculated as follows and may not exceed the total bandwidth specified in the
		data sheet: Overall Bandwidth = System BW x Min Noise/System BW Ratio \n
			:param ratio: float Range: 1 to Max
		"""
		param = Conversions.decimal_value_to_str(ratio)
		self._core.io.write(f'SOURce<HwInstance>:AWGN:BWIDth:RATio {param}')

	def get_value(self) -> float:
		"""SCPI: [SOURce<HW>]:AWGN:BWIDth \n
		Snippet: value: float = driver.source.awgn.bandwidth.get_value() \n
		Sets the system bandwidth. The noise signal at the level which corresponds to the specified carrier/noise ratio is
		generated in the bandwidth specified here. This command is available for modes Additive Noise and Noise Only
		(SOUR:AWGN:MODE ADD|ONLY) . \n
			:return: bwidth: float Range: 1000 to depends on the installed options
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:AWGN:BWIDth?')
		return Conversions.str_to_float(response)

	def set_value(self, bwidth: float) -> None:
		"""SCPI: [SOURce<HW>]:AWGN:BWIDth \n
		Snippet: driver.source.awgn.bandwidth.set_value(bwidth = 1.0) \n
		Sets the system bandwidth. The noise signal at the level which corresponds to the specified carrier/noise ratio is
		generated in the bandwidth specified here. This command is available for modes Additive Noise and Noise Only
		(SOUR:AWGN:MODE ADD|ONLY) . \n
			:param bwidth: float Range: 1000 to depends on the installed options
		"""
		param = Conversions.decimal_value_to_str(bwidth)
		self._core.io.write(f'SOURce<HwInstance>:AWGN:BWIDth {param}')

	def clone(self) -> 'Bandwidth':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Bandwidth(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
