from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IsMeas:
	"""IsMeas commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("isMeas", core, parent)

	def get_catalog(self) -> List[str]:
		"""SCPI: TRIGger:GPRF:GENerator<Instance>:SEQuencer:ISMeas:CATalog \n
		Snippet: value: List[str] = driver.trigger.gprf.generator.sequencer.isMeas.get_catalog() \n
		Queries all available measurement source strings. \n
			:return: source_list: Comma-separated list of strings. Each string represents a supported source.
		"""
		response = self._core.io.query_str('TRIGger:GPRF:GENerator<Instance>:SEQuencer:ISMeas:CATalog?')
		return Conversions.str_to_str_list(response)

	def get_source(self) -> str:
		"""SCPI: TRIGger:GPRF:GENerator<Instance>:SEQuencer:ISMeas:SOURce \n
		Snippet: value: str = driver.trigger.gprf.generator.sequencer.isMeas.get_source() \n
		Selects a measurement for triggering sequencer list incrementations. A complete list of all supported strings can be
		queried using method RsCMPX_Gprf.Trigger.Gprf.Generator.Sequencer.IsMeas.catalog. \n
			:return: source: No help available
		"""
		response = self._core.io.query_str('TRIGger:GPRF:GENerator<Instance>:SEQuencer:ISMeas:SOURce?')
		return trim_str_response(response)

	def set_source(self, source: str) -> None:
		"""SCPI: TRIGger:GPRF:GENerator<Instance>:SEQuencer:ISMeas:SOURce \n
		Snippet: driver.trigger.gprf.generator.sequencer.isMeas.set_source(source = '1') \n
		Selects a measurement for triggering sequencer list incrementations. A complete list of all supported strings can be
		queried using method RsCMPX_Gprf.Trigger.Gprf.Generator.Sequencer.IsMeas.catalog. \n
			:param source: No help available
		"""
		param = Conversions.value_to_quoted_str(source)
		self._core.io.write(f'TRIGger:GPRF:GENerator<Instance>:SEQuencer:ISMeas:SOURce {param}')
