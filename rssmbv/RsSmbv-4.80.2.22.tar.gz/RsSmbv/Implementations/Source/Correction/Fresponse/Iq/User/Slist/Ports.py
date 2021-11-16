from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ports:
	"""Ports commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ports", core, parent)

	def get_from_py(self) -> int:
		"""SCPI: [SOURce<HW>]:CORRection:FRESponse:IQ:USER:SLISt:PORTs:FROM \n
		Snippet: value: int = driver.source.correction.fresponse.iq.user.slist.ports.get_from_py() \n
		No command help available \n
			:return: freq_corr_iq_po_fro: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:CORRection:FRESponse:IQ:USER:SLISt:PORTs:FROM?')
		return Conversions.str_to_int(response)

	def set_from_py(self, freq_corr_iq_po_fro: int) -> None:
		"""SCPI: [SOURce<HW>]:CORRection:FRESponse:IQ:USER:SLISt:PORTs:FROM \n
		Snippet: driver.source.correction.fresponse.iq.user.slist.ports.set_from_py(freq_corr_iq_po_fro = 1) \n
		No command help available \n
			:param freq_corr_iq_po_fro: No help available
		"""
		param = Conversions.decimal_value_to_str(freq_corr_iq_po_fro)
		self._core.io.write(f'SOURce<HwInstance>:CORRection:FRESponse:IQ:USER:SLISt:PORTs:FROM {param}')

	def get_to(self) -> int:
		"""SCPI: [SOURce<HW>]:CORRection:FRESponse:IQ:USER:SLISt:PORTs:TO \n
		Snippet: value: int = driver.source.correction.fresponse.iq.user.slist.ports.get_to() \n
		No command help available \n
			:return: freq_corr_iq_po_to: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:CORRection:FRESponse:IQ:USER:SLISt:PORTs:TO?')
		return Conversions.str_to_int(response)

	def set_to(self, freq_corr_iq_po_to: int) -> None:
		"""SCPI: [SOURce<HW>]:CORRection:FRESponse:IQ:USER:SLISt:PORTs:TO \n
		Snippet: driver.source.correction.fresponse.iq.user.slist.ports.set_to(freq_corr_iq_po_to = 1) \n
		No command help available \n
			:param freq_corr_iq_po_to: No help available
		"""
		param = Conversions.decimal_value_to_str(freq_corr_iq_po_to)
		self._core.io.write(f'SOURce<HwInstance>:CORRection:FRESponse:IQ:USER:SLISt:PORTs:TO {param}')
