from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Slist:
	"""Slist commands group definition. 7 total commands, 1 Sub-groups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("slist", core, parent)

	@property
	def ports(self):
		"""ports commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_ports'):
			from .Ports import Ports
			self._ports = Ports(self._core, self._cmd_group)
		return self._ports

	def get_catalog(self) -> str:
		"""SCPI: [SOURce<HW>]:CORRection:FRESponse:RF:USER:SLISt:CATalog \n
		Snippet: value: str = driver.source.correction.fresponse.rf.user.slist.get_catalog() \n
		Queries the S-parameter files included in the current S-paramters list. \n
			:return: catalog: filename1,filename2,...filename10 Returns a string of filenames separated by commas.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:CORRection:FRESponse:RF:USER:SLISt:CATalog?')
		return trim_str_response(response)

	def clear(self) -> None:
		"""SCPI: [SOURce<HW>]:CORRection:FRESponse:RF:USER:SLISt:CLEar \n
		Snippet: driver.source.correction.fresponse.rf.user.slist.clear() \n
		Deletes all entries in the lists. \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:CORRection:FRESponse:RF:USER:SLISt:CLEar')

	def clear_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce<HW>]:CORRection:FRESponse:RF:USER:SLISt:CLEar \n
		Snippet: driver.source.correction.fresponse.rf.user.slist.clear_with_opc() \n
		Deletes all entries in the lists. \n
		Same as clear, but waits for the operation to complete before continuing further. Use the RsSmbv.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:CORRection:FRESponse:RF:USER:SLISt:CLEar', opc_timeout_ms)

	def get_select(self) -> str:
		"""SCPI: [SOURce<HW>]:CORRection:FRESponse:RF:USER:SLISt:SELect \n
		Snippet: value: str = driver.source.correction.fresponse.rf.user.slist.get_select() \n
		Selects an existing S-parameter file (*.s<n>p) from the default directory or from the specific directory.
		Refer to 'Accessing Files in the Default or Specified Directory' for general information on file handling in the default
		and in a specific directory. \n
			:return: freq_resp_rf_slsel: string Filename incl. file extension or complete file path Use 'none' to unload a file.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:CORRection:FRESponse:RF:USER:SLISt:SELect?')
		return trim_str_response(response)

	def set_select(self, freq_resp_rf_slsel: str) -> None:
		"""SCPI: [SOURce<HW>]:CORRection:FRESponse:RF:USER:SLISt:SELect \n
		Snippet: driver.source.correction.fresponse.rf.user.slist.set_select(freq_resp_rf_slsel = '1') \n
		Selects an existing S-parameter file (*.s<n>p) from the default directory or from the specific directory.
		Refer to 'Accessing Files in the Default or Specified Directory' for general information on file handling in the default
		and in a specific directory. \n
			:param freq_resp_rf_slsel: string Filename incl. file extension or complete file path Use 'none' to unload a file.
		"""
		param = Conversions.value_to_quoted_str(freq_resp_rf_slsel)
		self._core.io.write(f'SOURce<HwInstance>:CORRection:FRESponse:RF:USER:SLISt:SELect {param}')

	def get_size(self) -> int:
		"""SCPI: [SOURce<HW>]:CORRection:FRESponse:RF:USER:SLISt:SIZE \n
		Snippet: value: int = driver.source.correction.fresponse.rf.user.slist.get_size() \n
		Queries the number of files in the list. \n
			:return: freq_resp_rf_sli_si: integer Range: 0 to 10
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:CORRection:FRESponse:RF:USER:SLISt:SIZE?')
		return Conversions.str_to_int(response)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:CORRection:FRESponse:RF:USER:SLISt:[STATe] \n
		Snippet: value: bool = driver.source.correction.fresponse.rf.user.slist.get_state() \n
		Enables that the selected file is used for frequency response compensation. To trigger calculation of the correction
		values, send the command CORRection:FRESponse:RF:USER:APPLy. Otherwise changes are not considered. \n
			:return: freq_resp_sli_stat: 0| 1| OFF| ON
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:CORRection:FRESponse:RF:USER:SLISt:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, freq_resp_sli_stat: bool) -> None:
		"""SCPI: [SOURce<HW>]:CORRection:FRESponse:RF:USER:SLISt:[STATe] \n
		Snippet: driver.source.correction.fresponse.rf.user.slist.set_state(freq_resp_sli_stat = False) \n
		Enables that the selected file is used for frequency response compensation. To trigger calculation of the correction
		values, send the command CORRection:FRESponse:RF:USER:APPLy. Otherwise changes are not considered. \n
			:param freq_resp_sli_stat: 0| 1| OFF| ON
		"""
		param = Conversions.bool_to_str(freq_resp_sli_stat)
		self._core.io.write(f'SOURce<HwInstance>:CORRection:FRESponse:RF:USER:SLISt:STATe {param}')

	def clone(self) -> 'Slist':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Slist(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
