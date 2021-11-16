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
		"""SCPI: [SOURce<HW>]:CORRection:FRESponse:RF:USER:SLISt:PORTs:FROM \n
		Snippet: value: int = driver.source.correction.fresponse.rf.user.slist.ports.get_from_py() \n
		Sets the port number from that the signal is coming and the port to that it is going. Available ports depend on the file
		content and file extenssion, see 'S-Parameters (Touchstone) Files'. \n
			:return: freq_resp_sli_stfr: integer Range: 1 to 8 (dynamic)
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:CORRection:FRESponse:RF:USER:SLISt:PORTs:FROM?')
		return Conversions.str_to_int(response)

	def set_from_py(self, freq_resp_sli_stfr: int) -> None:
		"""SCPI: [SOURce<HW>]:CORRection:FRESponse:RF:USER:SLISt:PORTs:FROM \n
		Snippet: driver.source.correction.fresponse.rf.user.slist.ports.set_from_py(freq_resp_sli_stfr = 1) \n
		Sets the port number from that the signal is coming and the port to that it is going. Available ports depend on the file
		content and file extenssion, see 'S-Parameters (Touchstone) Files'. \n
			:param freq_resp_sli_stfr: integer Range: 1 to 8 (dynamic)
		"""
		param = Conversions.decimal_value_to_str(freq_resp_sli_stfr)
		self._core.io.write(f'SOURce<HwInstance>:CORRection:FRESponse:RF:USER:SLISt:PORTs:FROM {param}')

	def get_to(self) -> int:
		"""SCPI: [SOURce<HW>]:CORRection:FRESponse:RF:USER:SLISt:PORTs:TO \n
		Snippet: value: int = driver.source.correction.fresponse.rf.user.slist.ports.get_to() \n
		Sets the port number from that the signal is coming and the port to that it is going. Available ports depend on the file
		content and file extenssion, see 'S-Parameters (Touchstone) Files'. \n
			:return: freq_resp_sli_stfr: integer Range: 1 to 8 (dynamic)
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:CORRection:FRESponse:RF:USER:SLISt:PORTs:TO?')
		return Conversions.str_to_int(response)

	def set_to(self, freq_resp_sli_stfr: int) -> None:
		"""SCPI: [SOURce<HW>]:CORRection:FRESponse:RF:USER:SLISt:PORTs:TO \n
		Snippet: driver.source.correction.fresponse.rf.user.slist.ports.set_to(freq_resp_sli_stfr = 1) \n
		Sets the port number from that the signal is coming and the port to that it is going. Available ports depend on the file
		content and file extenssion, see 'S-Parameters (Touchstone) Files'. \n
			:param freq_resp_sli_stfr: integer Range: 1 to 8 (dynamic)
		"""
		param = Conversions.decimal_value_to_str(freq_resp_sli_stfr)
		self._core.io.write(f'SOURce<HwInstance>:CORRection:FRESponse:RF:USER:SLISt:PORTs:TO {param}')
