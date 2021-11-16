from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tp:
	"""Tp commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tp", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:NR5G:QCKSet:GENeral:ES:TP:STATe \n
		Snippet: value: bool = driver.source.bb.nr5G.qckset.general.es.tp.get_state() \n
		No command help available \n
			:return: qck_set_tp: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:QCKSet:GENeral:ES:TP:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, qck_set_tp: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:QCKSet:GENeral:ES:TP:STATe \n
		Snippet: driver.source.bb.nr5G.qckset.general.es.tp.set_state(qck_set_tp = False) \n
		No command help available \n
			:param qck_set_tp: No help available
		"""
		param = Conversions.bool_to_str(qck_set_tp)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:QCKSet:GENeral:ES:TP:STATe {param}')
