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
		"""SCPI: [SOURce<HW>]:CORRection:FRESponse:IQ:USER:FLISt:CATalog \n
		Snippet: value: str = driver.source.correction.fresponse.iq.user.flist.get_catalog() \n
		No command help available \n
			:return: catalog: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:CORRection:FRESponse:IQ:USER:FLISt:CATalog?')
		return trim_str_response(response)

	def clear(self) -> None:
		"""SCPI: [SOURce<HW>]:CORRection:FRESponse:IQ:USER:FLISt:CLEar \n
		Snippet: driver.source.correction.fresponse.iq.user.flist.clear() \n
		No command help available \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:CORRection:FRESponse:IQ:USER:FLISt:CLEar')

	def clear_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce<HW>]:CORRection:FRESponse:IQ:USER:FLISt:CLEar \n
		Snippet: driver.source.correction.fresponse.iq.user.flist.clear_with_opc() \n
		No command help available \n
		Same as clear, but waits for the operation to complete before continuing further. Use the RsSmbv.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:CORRection:FRESponse:IQ:USER:FLISt:CLEar', opc_timeout_ms)

	def get_select(self) -> str:
		"""SCPI: [SOURce<HW>]:CORRection:FRESponse:IQ:USER:FLISt:SELect \n
		Snippet: value: str = driver.source.correction.fresponse.iq.user.flist.get_select() \n
		No command help available \n
			:return: freq_corr_iq_flsel: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:CORRection:FRESponse:IQ:USER:FLISt:SELect?')
		return trim_str_response(response)

	def set_select(self, freq_corr_iq_flsel: str) -> None:
		"""SCPI: [SOURce<HW>]:CORRection:FRESponse:IQ:USER:FLISt:SELect \n
		Snippet: driver.source.correction.fresponse.iq.user.flist.set_select(freq_corr_iq_flsel = '1') \n
		No command help available \n
			:param freq_corr_iq_flsel: No help available
		"""
		param = Conversions.value_to_quoted_str(freq_corr_iq_flsel)
		self._core.io.write(f'SOURce<HwInstance>:CORRection:FRESponse:IQ:USER:FLISt:SELect {param}')

	def get_size(self) -> int:
		"""SCPI: [SOURce<HW>]:CORRection:FRESponse:IQ:USER:FLISt:SIZE \n
		Snippet: value: int = driver.source.correction.fresponse.iq.user.flist.get_size() \n
		No command help available \n
			:return: freq_resp_iq_fl_isi: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:CORRection:FRESponse:IQ:USER:FLISt:SIZE?')
		return Conversions.str_to_int(response)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:CORRection:FRESponse:IQ:USER:FLISt:[STATe] \n
		Snippet: value: bool = driver.source.correction.fresponse.iq.user.flist.get_state() \n
		No command help available \n
			:return: freq_corr_fl_stat: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:CORRection:FRESponse:IQ:USER:FLISt:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, freq_corr_fl_stat: bool) -> None:
		"""SCPI: [SOURce<HW>]:CORRection:FRESponse:IQ:USER:FLISt:[STATe] \n
		Snippet: driver.source.correction.fresponse.iq.user.flist.set_state(freq_corr_fl_stat = False) \n
		No command help available \n
			:param freq_corr_fl_stat: No help available
		"""
		param = Conversions.bool_to_str(freq_corr_fl_stat)
		self._core.io.write(f'SOURce<HwInstance>:CORRection:FRESponse:IQ:USER:FLISt:STATe {param}')

	def clone(self) -> 'Flist':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Flist(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
