from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UssIdx:
	"""UssIdx commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ussIdx", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:NR5G:QCKSet:FRMFormat:SSC:USSidx:STATe \n
		Snippet: value: bool = driver.source.bb.nr5G.qckset.frmFormat.ssc.ussIdx.get_state() \n
		No command help available \n
			:return: qck_set_use_slot: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:NR5G:QCKSet:FRMFormat:SSC:USSidx:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, qck_set_use_slot: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:NR5G:QCKSet:FRMFormat:SSC:USSidx:STATe \n
		Snippet: driver.source.bb.nr5G.qckset.frmFormat.ssc.ussIdx.set_state(qck_set_use_slot = False) \n
		No command help available \n
			:param qck_set_use_slot: No help available
		"""
		param = Conversions.bool_to_str(qck_set_use_slot)
		self._core.io.write(f'SOURce<HwInstance>:BB:NR5G:QCKSet:FRMFormat:SSC:USSidx:STATe {param}')
