from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Edetector:
	"""Edetector commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("edetector", core, parent)

	def get_factor(self) -> float:
		"""SCPI: [SOURce<HW>]:POWer:ALC:EDETector:FACTor \n
		Snippet: value: float = driver.source.power.alc.edetector.get_factor() \n
		No command help available \n
			:return: detector_fact: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:POWer:ALC:EDETector:FACTor?')
		return Conversions.str_to_float(response)

	def get_level(self) -> float:
		"""SCPI: [SOURce<HW>]:POWer:ALC:EDETector:LEVel \n
		Snippet: value: float = driver.source.power.alc.edetector.get_level() \n
		No command help available \n
			:return: req_gen_lev: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:POWer:ALC:EDETector:LEVel?')
		return Conversions.str_to_float(response)
