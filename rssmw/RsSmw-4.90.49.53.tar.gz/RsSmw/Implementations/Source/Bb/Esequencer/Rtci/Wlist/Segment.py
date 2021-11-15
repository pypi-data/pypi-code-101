from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Segment:
	"""Segment commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("segment", core, parent)

	def get_catalog(self) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:ESEQuencer:RTCI:WLISt:SEGMent:CATalog \n
		Snippet: value: List[str] = driver.source.bb.esequencer.rtci.wlist.segment.get_catalog() \n
		Queries the waveform sequence of the currently selected waveform list. \n
			:return: catalog: string Returns the waveform files separated by commas
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ESEQuencer:RTCI:WLISt:SEGMent:CATalog?')
		return Conversions.str_to_str_list(response)
