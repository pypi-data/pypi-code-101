from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Data:
	"""Data commands group definition. 4 total commands, 0 Sub-groups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("data", core, parent)

	def get_catalog(self) -> List[str]:
		"""SCPI: [SOURce<HW>]:IQ:DOHerty:SHAPing:NORMalized:DATA:CATalog \n
		Snippet: value: List[str] = driver.source.iq.doherty.shaping.normalized.data.get_catalog() \n
		No command help available \n
			:return: catalog: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:IQ:DOHerty:SHAPing:NORMalized:DATA:CATalog?')
		return Conversions.str_to_str_list(response)

	def load(self, filename: str) -> None:
		"""SCPI: [SOURce<HW>]:IQ:DOHerty:SHAPing:NORMalized:DATA:LOAD \n
		Snippet: driver.source.iq.doherty.shaping.normalized.data.load(filename = '1') \n
		No command help available \n
			:param filename: No help available
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SOURce<HwInstance>:IQ:DOHerty:SHAPing:NORMalized:DATA:LOAD {param}')

	def set_store(self, filename: str) -> None:
		"""SCPI: [SOURce<HW>]:IQ:DOHerty:SHAPing:NORMalized:DATA:STORe \n
		Snippet: driver.source.iq.doherty.shaping.normalized.data.set_store(filename = '1') \n
		No command help available \n
			:param filename: No help available
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SOURce<HwInstance>:IQ:DOHerty:SHAPing:NORMalized:DATA:STORe {param}')

	def get_value(self) -> bytes:
		"""SCPI: [SOURce<HW>]:IQ:DOHerty:SHAPing:NORMalized:DATA \n
		Snippet: value: bytes = driver.source.iq.doherty.shaping.normalized.data.get_value() \n
		No command help available \n
			:return: data: No help available
		"""
		response = self._core.io.query_bin_block('SOURce<HwInstance>:IQ:DOHerty:SHAPing:NORMalized:DATA?')
		return response

	def set_value(self, data: bytes) -> None:
		"""SCPI: [SOURce<HW>]:IQ:DOHerty:SHAPing:NORMalized:DATA \n
		Snippet: driver.source.iq.doherty.shaping.normalized.data.set_value(data = b'ABCDEFGH') \n
		No command help available \n
			:param data: No help available
		"""
		self._core.io.write_bin_block('SOURce<HwInstance>:IQ:DOHerty:SHAPing:NORMalized:DATA ', data)
