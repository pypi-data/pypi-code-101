from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ...Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ntp:
	"""Ntp commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ntp", core, parent)

	def get_hostname(self) -> str:
		"""SCPI: SYSTem:NTP:HOSTname \n
		Snippet: value: str = driver.system.ntp.get_hostname() \n
		No command help available \n
			:return: ntp_name: No help available
		"""
		response = self._core.io.query_str('SYSTem:NTP:HOSTname?')
		return trim_str_response(response)

	def set_hostname(self, ntp_name: str) -> None:
		"""SCPI: SYSTem:NTP:HOSTname \n
		Snippet: driver.system.ntp.set_hostname(ntp_name = '1') \n
		No command help available \n
			:param ntp_name: No help available
		"""
		param = Conversions.value_to_quoted_str(ntp_name)
		self._core.io.write(f'SYSTem:NTP:HOSTname {param}')

	def get_state(self) -> bool:
		"""SCPI: SYSTem:NTP:STATe \n
		Snippet: value: bool = driver.system.ntp.get_state() \n
		No command help available \n
			:return: use_ntp_state: No help available
		"""
		response = self._core.io.query_str('SYSTem:NTP:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, use_ntp_state: bool) -> None:
		"""SCPI: SYSTem:NTP:STATe \n
		Snippet: driver.system.ntp.set_state(use_ntp_state = False) \n
		No command help available \n
			:param use_ntp_state: No help available
		"""
		param = Conversions.bool_to_str(use_ntp_state)
		self._core.io.write(f'SYSTem:NTP:STATe {param}')
