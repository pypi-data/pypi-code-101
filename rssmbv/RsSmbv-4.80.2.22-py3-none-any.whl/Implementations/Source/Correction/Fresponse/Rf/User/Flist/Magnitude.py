from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Magnitude:
	"""Magnitude commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("magnitude", core, parent)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:CORRection:FRESponse:RF:USER:FLISt:MAGNitude:[STATe] \n
		Snippet: value: bool = driver.source.correction.fresponse.rf.user.flist.magnitude.get_state() \n
		Enables that the magnitude and/or phase values from the selected file are used for frequency response compensation.
		To trigger calculation of the correction values, send the command CORRection:FRESponse:RF:USER:APPLy. Otherwise changes
		are not considered. \n
			:return: freq_corr_rf_mag_st: 0| 1| OFF| ON
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:CORRection:FRESponse:RF:USER:FLISt:MAGNitude:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, freq_corr_rf_mag_st: bool) -> None:
		"""SCPI: [SOURce<HW>]:CORRection:FRESponse:RF:USER:FLISt:MAGNitude:[STATe] \n
		Snippet: driver.source.correction.fresponse.rf.user.flist.magnitude.set_state(freq_corr_rf_mag_st = False) \n
		Enables that the magnitude and/or phase values from the selected file are used for frequency response compensation.
		To trigger calculation of the correction values, send the command CORRection:FRESponse:RF:USER:APPLy. Otherwise changes
		are not considered. \n
			:param freq_corr_rf_mag_st: 0| 1| OFF| ON
		"""
		param = Conversions.bool_to_str(freq_corr_rf_mag_st)
		self._core.io.write(f'SOURce<HwInstance>:CORRection:FRESponse:RF:USER:FLISt:MAGNitude:STATe {param}')
