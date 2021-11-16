from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Spath:
	"""Spath commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("spath", core, parent)

	def get_usage(self) -> List[bool]:
		"""SCPI: CONFigure:GPRF:GENerator<Instance>:SPATh:USAGe \n
		Snippet: value: List[bool] = driver.configure.gprf.generator.spath.get_usage() \n
		No command help available \n
			:return: enable: No help available
		"""
		response = self._core.io.query_str('CONFigure:GPRF:GENerator<Instance>:SPATh:USAGe?')
		return Conversions.str_to_bool_list(response)

	def set_usage(self, enable: List[bool]) -> None:
		"""SCPI: CONFigure:GPRF:GENerator<Instance>:SPATh:USAGe \n
		Snippet: driver.configure.gprf.generator.spath.set_usage(enable = [True, False, True]) \n
		No command help available \n
			:param enable: No help available
		"""
		param = Conversions.list_to_csv_str(enable)
		self._core.io.write(f'CONFigure:GPRF:GENerator<Instance>:SPATh:USAGe {param}')
