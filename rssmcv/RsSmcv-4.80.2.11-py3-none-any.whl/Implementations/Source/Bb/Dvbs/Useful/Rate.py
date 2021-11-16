from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rate:
	"""Rate commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rate", core, parent)

	def get_max(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:DVBS:USEFul:[RATE]:MAX \n
		Snippet: value: float = driver.source.bb.dvbs.useful.rate.get_max() \n
		Displays the transport stream data rate that is derived from the current modulation parameter settings and is required by
		the modulator at the input. For 'Stuffing > On', the value indicates the maximum useful data rate (payload) that is
		allowed in the transport stream. \n
			:return: inp_sig_max_rate: float Range: 0 to 999999999
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBS:USEFul:RATE:MAX?')
		return Conversions.str_to_float(response)

	def get_value(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:DVBS:USEFul:[RATE] \n
		Snippet: value: float = driver.source.bb.dvbs.useful.rate.get_value() \n
		Displays the data rate of the useful data that is present in the transport stream at the transport stream input interface
		selected to supply the modulation data. This is a measured value. \n
			:return: inp_sig_usefull: float Range: 0 to 999999999
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:DVBS:USEFul:RATE?')
		return Conversions.str_to_float(response)
