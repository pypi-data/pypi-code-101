from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Statistic:
	"""Statistic commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("statistic", core, parent)

	def reset(self) -> None:
		"""SCPI: MEASure[:SCALar]:STATistic:RESet \n
		Snippet: driver.measure.scalar.statistic.reset() \n
		Resets the minimum, maximum and average statistic values for voltage, current, and power. Additionally this command
		resets the measured energy. \n
		"""
		self._core.io.write(f'MEASure:SCALar:STATistic:RESet')

	def reset_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: MEASure[:SCALar]:STATistic:RESet \n
		Snippet: driver.measure.scalar.statistic.reset_with_opc() \n
		Resets the minimum, maximum and average statistic values for voltage, current, and power. Additionally this command
		resets the measured energy. \n
		Same as reset, but waits for the operation to complete before continuing further. Use the RsNgx.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'MEASure:SCALar:STATistic:RESet', opc_timeout_ms)

	def get_count(self) -> int:
		"""SCPI: MEASure[:SCALar]:STATistic:COUNt \n
		Snippet: value: int = driver.measure.scalar.statistic.get_count() \n
		Returns the number of samples measured in the statistics for voltage/current/power \n
			:return: result: No help available
		"""
		response = self._core.io.query_str('MEASure:SCALar:STATistic:COUNt?')
		return Conversions.str_to_int(response)
