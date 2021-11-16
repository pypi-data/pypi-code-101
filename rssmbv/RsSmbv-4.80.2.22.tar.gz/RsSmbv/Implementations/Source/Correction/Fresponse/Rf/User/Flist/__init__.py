from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Flist:
	"""Flist commands group definition. 7 total commands, 2 Sub-groups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("flist", core, parent)

	@property
	def magnitude(self):
		"""magnitude commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_magnitude'):
			from .Magnitude import Magnitude
			self._magnitude = Magnitude(self._core, self._cmd_group)
		return self._magnitude

	@property
	def phase(self):
		"""phase commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_phase'):
			from .Phase import Phase
			self._phase = Phase(self._core, self._cmd_group)
		return self._phase

	def get_catalog(self) -> str:
		"""SCPI: [SOURce<HW>]:CORRection:FRESponse:RF:USER:FLISt:CATalog \n
		Snippet: value: str = driver.source.correction.fresponse.rf.user.flist.get_catalog() \n
		Queries the frequency response FR list files included in the current FR list. \n
			:return: catalog: filename1,filename2,...filename5 Returns a string of filenames separated by commas.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:CORRection:FRESponse:RF:USER:FLISt:CATalog?')
		return trim_str_response(response)

	def clear(self) -> None:
		"""SCPI: [SOURce<HW>]:CORRection:FRESponse:RF:USER:FLISt:CLEar \n
		Snippet: driver.source.correction.fresponse.rf.user.flist.clear() \n
		Deletes all entries in the lists. \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:CORRection:FRESponse:RF:USER:FLISt:CLEar')

	def clear_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce<HW>]:CORRection:FRESponse:RF:USER:FLISt:CLEar \n
		Snippet: driver.source.correction.fresponse.rf.user.flist.clear_with_opc() \n
		Deletes all entries in the lists. \n
		Same as clear, but waits for the operation to complete before continuing further. Use the RsSmbv.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:CORRection:FRESponse:RF:USER:FLISt:CLEar', opc_timeout_ms)

	def get_select(self) -> str:
		"""SCPI: [SOURce<HW>]:CORRection:FRESponse:RF:USER:FLISt:SELect \n
		Snippet: value: str = driver.source.correction.fresponse.rf.user.flist.get_select() \n
		Selects an existing frequency response list file (*.uco or *.fres) from the default directory or from the specific
		directory. Refer to 'Accessing Files in the Default or Specified Directory' for general information on file handling in
		the default and in a specific directory. \n
			:return: freq_corr_rf_fl_sel: string Filename incl. file extension or complete file path Use 'none' to unload a file.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:CORRection:FRESponse:RF:USER:FLISt:SELect?')
		return trim_str_response(response)

	def set_select(self, freq_corr_rf_fl_sel: str) -> None:
		"""SCPI: [SOURce<HW>]:CORRection:FRESponse:RF:USER:FLISt:SELect \n
		Snippet: driver.source.correction.fresponse.rf.user.flist.set_select(freq_corr_rf_fl_sel = '1') \n
		Selects an existing frequency response list file (*.uco or *.fres) from the default directory or from the specific
		directory. Refer to 'Accessing Files in the Default or Specified Directory' for general information on file handling in
		the default and in a specific directory. \n
			:param freq_corr_rf_fl_sel: string Filename incl. file extension or complete file path Use 'none' to unload a file.
		"""
		param = Conversions.value_to_quoted_str(freq_corr_rf_fl_sel)
		self._core.io.write(f'SOURce<HwInstance>:CORRection:FRESponse:RF:USER:FLISt:SELect {param}')

	def get_size(self) -> int:
		"""SCPI: [SOURce<HW>]:CORRection:FRESponse:RF:USER:FLISt:SIZE \n
		Snippet: value: int = driver.source.correction.fresponse.rf.user.flist.get_size() \n
		Queries the number of files in the list. \n
			:return: freq_resp_rf_fli_si: integer Range: 0 to 5
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:CORRection:FRESponse:RF:USER:FLISt:SIZE?')
		return Conversions.str_to_int(response)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:CORRection:FRESponse:RF:USER:FLISt:[STATe] \n
		Snippet: value: bool = driver.source.correction.fresponse.rf.user.flist.get_state() \n
		Enables that user-defined corrections in form of FR lists are used. To use corrections of this kind, load the FR lists,
		activated them and apply the configuration with the corresponding commands, see 'Frequency Response (FR) List Commands'. \n
			:return: freq_corr_rf_fl_sta: 0| 1| OFF| ON
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:CORRection:FRESponse:RF:USER:FLISt:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, freq_corr_rf_fl_sta: bool) -> None:
		"""SCPI: [SOURce<HW>]:CORRection:FRESponse:RF:USER:FLISt:[STATe] \n
		Snippet: driver.source.correction.fresponse.rf.user.flist.set_state(freq_corr_rf_fl_sta = False) \n
		Enables that user-defined corrections in form of FR lists are used. To use corrections of this kind, load the FR lists,
		activated them and apply the configuration with the corresponding commands, see 'Frequency Response (FR) List Commands'. \n
			:param freq_corr_rf_fl_sta: 0| 1| OFF| ON
		"""
		param = Conversions.bool_to_str(freq_corr_rf_fl_sta)
		self._core.io.write(f'SOURce<HwInstance>:CORRection:FRESponse:RF:USER:FLISt:STATe {param}')

	def clone(self) -> 'Flist':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Flist(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
