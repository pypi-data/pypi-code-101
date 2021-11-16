from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Source:
	"""Source commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("source", core, parent)

	def set(self, trigger: List[str], triggerInstance=repcap.TriggerInstance.Default) -> None:
		"""SCPI: TRIGger:BASE:EXTA<Instance>:SOURce \n
		Snippet: driver.trigger.base.extA.source.set(trigger = ['1', '2', '3'], triggerInstance = repcap.TriggerInstance.Default) \n
		No command help available \n
			:param trigger: No help available
			:param triggerInstance: optional repeated capability selector. Default value: Nr1 (settable in the interface 'ExtA')
		"""
		param = Conversions.list_to_csv_quoted_str(trigger)
		triggerInstance_cmd_val = self._cmd_group.get_repcap_cmd_value(triggerInstance, repcap.TriggerInstance)
		self._core.io.write(f'TRIGger:BASE:EXTA{triggerInstance_cmd_val}:SOURce {param}')

	def get(self, triggerInstance=repcap.TriggerInstance.Default) -> List[str]:
		"""SCPI: TRIGger:BASE:EXTA<Instance>:SOURce \n
		Snippet: value: List[str] = driver.trigger.base.extA.source.get(triggerInstance = repcap.TriggerInstance.Default) \n
		No command help available \n
			:param triggerInstance: optional repeated capability selector. Default value: Nr1 (settable in the interface 'ExtA')
			:return: trigger: No help available"""
		triggerInstance_cmd_val = self._cmd_group.get_repcap_cmd_value(triggerInstance, repcap.TriggerInstance)
		response = self._core.io.query_str(f'TRIGger:BASE:EXTA{triggerInstance_cmd_val}:SOURce?')
		return Conversions.str_to_str_list(response)
