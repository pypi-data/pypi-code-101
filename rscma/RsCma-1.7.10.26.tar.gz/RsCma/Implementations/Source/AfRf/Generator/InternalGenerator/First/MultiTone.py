from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MultiTone:
	"""MultiTone commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("multiTone", core, parent)

	def get_tlevel(self) -> List[float]:
		"""SCPI: SOURce:AFRF:GENerator<Instance>:IGENerator:FIRSt:MTONe:TLEVel \n
		Snippet: value: List[float] = driver.source.afRf.generator.internalGenerator.first.multiTone.get_tlevel() \n
		No command help available \n
			:return: tlevel: No help available
		"""
		response = self._core.io.query_bin_or_ascii_float_list('SOURce:AFRF:GENerator<Instance>:IGENerator:FIRSt:MTONe:TLEVel?')
		return response

	def set_tlevel(self, tlevel: List[float]) -> None:
		"""SCPI: SOURce:AFRF:GENerator<Instance>:IGENerator:FIRSt:MTONe:TLEVel \n
		Snippet: driver.source.afRf.generator.internalGenerator.first.multiTone.set_tlevel(tlevel = [1.1, 2.2, 3.3]) \n
		No command help available \n
			:param tlevel: No help available
		"""
		param = Conversions.list_to_csv_str(tlevel)
		self._core.io.write(f'SOURce:AFRF:GENerator<Instance>:IGENerator:FIRSt:MTONe:TLEVel {param}')
