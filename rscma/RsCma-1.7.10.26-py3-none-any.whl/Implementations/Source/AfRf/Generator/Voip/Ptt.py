from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ptt:
	"""Ptt commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ptt", core, parent)

	def get_state(self) -> bool:
		"""SCPI: SOURce:AFRF:GENerator<Instance>:VOIP:PTT:STATe \n
		Snippet: value: bool = driver.source.afRf.generator.voip.ptt.get_state() \n
		Sets the DUT's PTT state. Disable PTT at the DUT side, if you are finished with the TX testing. \n
			:return: ptt_state: OFF | ON
		"""
		response = self._core.io.query_str('SOURce:AFRF:GENerator<Instance>:VOIP:PTT:STATe?')
		return Conversions.str_to_bool(response)

	def get_value(self) -> bool:
		"""SCPI: SOURce:AFRF:GENerator<Instance>:VOIP:PTT \n
		Snippet: value: bool = driver.source.afRf.generator.voip.ptt.get_value() \n
		No command help available \n
			:return: ptt: No help available
		"""
		response = self._core.io.query_str('SOURce:AFRF:GENerator<Instance>:VOIP:PTT?')
		return Conversions.str_to_bool(response)

	def set_value(self, ptt: bool) -> None:
		"""SCPI: SOURce:AFRF:GENerator<Instance>:VOIP:PTT \n
		Snippet: driver.source.afRf.generator.voip.ptt.set_value(ptt = False) \n
		No command help available \n
			:param ptt: No help available
		"""
		param = Conversions.bool_to_str(ptt)
		self._core.io.write(f'SOURce:AFRF:GENerator<Instance>:VOIP:PTT {param}')
