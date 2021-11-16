from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class All:
	"""All commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("all", core, parent)

	# noinspection PyTypeChecker
	def fetch(self) -> List[enums.ResourceState]:
		"""SCPI: FETCh:GPRF:MEASurement<Instance>:IQRecorder:STATe:ALL \n
		Snippet: value: List[enums.ResourceState] = driver.gprf.measurement.iqRecorder.state.all.fetch() \n
		Queries the main measurement state and the measurement substates. Both measurement substates are relevant for running
		measurements only. Use FETCh:...:STATe? to query the main measurement state only. Use INITiate..., STOP..., ABORt...
		to change the measurement state. \n
			:return: meas_state: No help available"""
		response = self._core.io.query_str(f'FETCh:GPRF:MEASurement<Instance>:IQRecorder:STATe:ALL?')
		return Conversions.str_to_list_enum(response, enums.ResourceState)
