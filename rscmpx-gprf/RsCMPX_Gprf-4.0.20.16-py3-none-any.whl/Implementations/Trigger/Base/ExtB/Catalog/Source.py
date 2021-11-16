from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Source:
	"""Source commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("source", core, parent)

	def get(self, triggerInstance=repcap.TriggerInstance.Default) -> List[str]:
		"""SCPI: TRIGger:BASE:EXTB<Instance>:CATalog:SOURce \n
		Snippet: value: List[str] = driver.trigger.base.extB.catalog.source.get(triggerInstance = repcap.TriggerInstance.Default) \n
		No command help available \n
			:param triggerInstance: optional repeated capability selector. Default value: Nr1 (settable in the interface 'ExtB')
			:return: trigger: No help available"""
		triggerInstance_cmd_val = self._cmd_group.get_repcap_cmd_value(triggerInstance, repcap.TriggerInstance)
		response = self._core.io.query_str(f'TRIGger:BASE:EXTB{triggerInstance_cmd_val}:CATalog:SOURce?')
		return Conversions.str_to_str_list(response)
