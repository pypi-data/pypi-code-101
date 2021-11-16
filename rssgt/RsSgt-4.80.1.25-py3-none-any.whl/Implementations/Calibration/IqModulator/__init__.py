from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IqModulator:
	"""IqModulator commands group definition. 5 total commands, 2 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("iqModulator", core, parent)

	@property
	def bband(self):
		"""bband commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bband'):
			from .Bband import Bband
			self._bband = Bband(self._core, self._cmd_group)
		return self._bband

	@property
	def iqModulator(self):
		"""iqModulator commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_iqModulator'):
			from .IqModulator import IqModulator
			self._iqModulator = IqModulator(self._core, self._cmd_group)
		return self._iqModulator

	def get_full(self) -> bool:
		"""SCPI: CALibration:IQModulator:FULL \n
		Snippet: value: bool = driver.calibration.iqModulator.get_full() \n
		Starts the adjustment of the I/Q modulator for the entire frequency range. The I/Q modulator is adjusted with respect to
		carrier leakage, I/Q imbalance and quadrature. \n
			:return: modulator: 0| 1| OFF| ON
		"""
		response = self._core.io.query_str('CALibration:IQModulator:FULL?')
		return Conversions.str_to_bool(response)

	def get_local(self) -> bool:
		"""SCPI: CALibration:IQModulator:LOCal \n
		Snippet: value: bool = driver.calibration.iqModulator.get_local() \n
		Starts the adjustment of the I/Q modulator for the current frequency. The I/Q modulator is adjusted with respect to
		carrier leakage, I/Q imbalance and quadrature. This adjustment is only possible when OUTPut[:STATe] ON and
		[:SOURce]:IQ:STATe ON. \n
			:return: cal_modulator_loc_error: No help available
		"""
		response = self._core.io.query_str('CALibration:IQModulator:LOCal?')
		return Conversions.str_to_bool(response)

	def get_temperature(self) -> str:
		"""SCPI: CALibration:IQModulator:TEMPerature \n
		Snippet: value: str = driver.calibration.iqModulator.get_temperature() \n
		Queries the delta temperature since the last performed adjustment. \n
			:return: temperature: string
		"""
		response = self._core.io.query_str('CALibration:IQModulator:TEMPerature?')
		return trim_str_response(response)

	def clone(self) -> 'IqModulator':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = IqModulator(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
