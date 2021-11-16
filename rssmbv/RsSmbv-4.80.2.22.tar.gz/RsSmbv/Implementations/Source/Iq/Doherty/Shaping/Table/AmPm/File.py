from typing import List

from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class File:
	"""File commands group definition. 4 total commands, 0 Sub-groups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("file", core, parent)

	def get_catalog(self) -> List[str]:
		"""SCPI: [SOURce<HW>]:IQ:DOHerty:SHAPing:TABLe:AMPM:FILE:CATalog \n
		Snippet: value: List[str] = driver.source.iq.doherty.shaping.table.amPm.file.get_catalog() \n
		No command help available \n
			:return: catalog: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:DOHerty:SHAPing:TABLe:AMPM:FILE:CATalog?')
		return Conversions.str_to_str_list(response)

	def get_data(self) -> List[float]:
		"""SCPI: [SOURce<HW>]:IQ:DOHerty:SHAPing:TABLe:AMPM:FILE:DATA \n
		Snippet: value: List[float] = driver.source.iq.doherty.shaping.table.amPm.file.get_data() \n
		No command help available \n
			:return: dpd_pm_table_data: No help available
		"""
		response = self._core.io.query_bin_or_ascii_float_list('SOURce<HwInstance>:IQ:DOHerty:SHAPing:TABLe:AMPM:FILE:DATA?')
		return response

	def set_data(self, dpd_pm_table_data: List[float]) -> None:
		"""SCPI: [SOURce<HW>]:IQ:DOHerty:SHAPing:TABLe:AMPM:FILE:DATA \n
		Snippet: driver.source.iq.doherty.shaping.table.amPm.file.set_data(dpd_pm_table_data = [1.1, 2.2, 3.3]) \n
		No command help available \n
			:param dpd_pm_table_data: No help available
		"""
		param = Conversions.list_to_csv_str(dpd_pm_table_data)
		self._core.io.write(f'SOURce<HwInstance>:IQ:DOHerty:SHAPing:TABLe:AMPM:FILE:DATA {param}')

	def set_new(self, ipartd_pi_db_dpd_pm_table_data_new_file: List[float]) -> None:
		"""SCPI: [SOURce<HW>]:IQ:DOHerty:SHAPing:TABLe:AMPM:FILE:NEW \n
		Snippet: driver.source.iq.doherty.shaping.table.amPm.file.set_new(ipartd_pi_db_dpd_pm_table_data_new_file = [1.1, 2.2, 3.3]) \n
		No command help available \n
			:param ipartd_pi_db_dpd_pm_table_data_new_file: No help available
		"""
		param = Conversions.list_to_csv_str(ipartd_pi_db_dpd_pm_table_data_new_file)
		self._core.io.write(f'SOURce<HwInstance>:IQ:DOHerty:SHAPing:TABLe:AMPM:FILE:NEW {param}')

	def get_select(self) -> str:
		"""SCPI: [SOURce<HW>]:IQ:DOHerty:SHAPing:TABLe:AMPM:FILE:[SELect] \n
		Snippet: value: str = driver.source.iq.doherty.shaping.table.amPm.file.get_select() \n
		No command help available \n
			:return: filename: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:DOHerty:SHAPing:TABLe:AMPM:FILE:SELect?')
		return trim_str_response(response)

	def set_select(self, filename: str) -> None:
		"""SCPI: [SOURce<HW>]:IQ:DOHerty:SHAPing:TABLe:AMPM:FILE:[SELect] \n
		Snippet: driver.source.iq.doherty.shaping.table.amPm.file.set_select(filename = '1') \n
		No command help available \n
			:param filename: No help available
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SOURce<HwInstance>:IQ:DOHerty:SHAPing:TABLe:AMPM:FILE:SELect {param}')
