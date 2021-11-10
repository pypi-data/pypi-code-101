from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class File:
	"""File commands group definition. 4 total commands, 0 Sub-groups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("file", core, parent)

	def get_date(self) -> str:
		"""SCPI: SOURce:XRT:GENerator<Instance>:ARB:FILE:DATE \n
		Snippet: value: str = driver.source.xrt.generator.arb.file.get_date() \n
		No command help available \n
			:return: date: No help available
		"""
		response = self._core.io.query_str('SOURce:XRT:GENerator<Instance>:ARB:FILE:DATE?')
		return trim_str_response(response)

	def get_option(self) -> str:
		"""SCPI: SOURce:XRT:GENerator<Instance>:ARB:FILE:OPTion \n
		Snippet: value: str = driver.source.xrt.generator.arb.file.get_option() \n
		No command help available \n
			:return: options: No help available
		"""
		response = self._core.io.query_str('SOURce:XRT:GENerator<Instance>:ARB:FILE:OPTion?')
		return trim_str_response(response)

	def get_version(self) -> str:
		"""SCPI: SOURce:XRT:GENerator<Instance>:ARB:FILE:VERSion \n
		Snippet: value: str = driver.source.xrt.generator.arb.file.get_version() \n
		No command help available \n
			:return: version: No help available
		"""
		response = self._core.io.query_str('SOURce:XRT:GENerator<Instance>:ARB:FILE:VERSion?')
		return trim_str_response(response)

	def get_value(self) -> str:
		"""SCPI: SOURce:XRT:GENerator<Instance>:ARB:FILE \n
		Snippet: value: str = driver.source.xrt.generator.arb.file.get_value() \n
		No command help available \n
			:return: arb_file: No help available
		"""
		response = self._core.io.query_str('SOURce:XRT:GENerator<Instance>:ARB:FILE?')
		return trim_str_response(response)

	def set_value(self, arb_file: str) -> None:
		"""SCPI: SOURce:XRT:GENerator<Instance>:ARB:FILE \n
		Snippet: driver.source.xrt.generator.arb.file.set_value(arb_file = '1') \n
		No command help available \n
			:param arb_file: No help available
		"""
		param = Conversions.value_to_quoted_str(arb_file)
		self._core.io.write(f'SOURce:XRT:GENerator<Instance>:ARB:FILE {param}')
