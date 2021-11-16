from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Phase:
	"""Phase commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("phase", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:CORRection:FRESponse:IQ:USER:FLISt:PHASe:[STATe] \n
		Snippet: value: bool = driver.source.correction.fresponse.iq.user.flist.phase.get_state() \n
		No command help available \n
			:return: freq_corr_pha_stat: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:CORRection:FRESponse:IQ:USER:FLISt:PHASe:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, freq_corr_pha_stat: bool) -> None:
		"""SCPI: [SOURce<HW>]:CORRection:FRESponse:IQ:USER:FLISt:PHASe:[STATe] \n
		Snippet: driver.source.correction.fresponse.iq.user.flist.phase.set_state(freq_corr_pha_stat = False) \n
		No command help available \n
			:param freq_corr_pha_stat: No help available
		"""
		param = Conversions.bool_to_str(freq_corr_pha_stat)
		self._core.io.write(f'SOURce<HwInstance>:CORRection:FRESponse:IQ:USER:FLISt:PHASe:STATe {param}')
