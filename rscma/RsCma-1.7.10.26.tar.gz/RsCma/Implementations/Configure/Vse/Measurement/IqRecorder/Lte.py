from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Lte:
	"""Lte commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lte", core, parent)

	# noinspection PyTypeChecker
	def get_cbwidth(self) -> enums.LteChannelBandwidth:
		"""SCPI: CONFigure:VSE:MEASurement<Instance>:IQRecorder:LTE:CBWidth \n
		Snippet: value: enums.LteChannelBandwidth = driver.configure.vse.measurement.iqRecorder.lte.get_cbwidth() \n
		No command help available \n
			:return: channel_bandwidth: No help available
		"""
		response = self._core.io.query_str('CONFigure:VSE:MEASurement<Instance>:IQRecorder:LTE:CBWidth?')
		return Conversions.str_to_scalar_enum(response, enums.LteChannelBandwidth)

	def set_cbwidth(self, channel_bandwidth: enums.LteChannelBandwidth) -> None:
		"""SCPI: CONFigure:VSE:MEASurement<Instance>:IQRecorder:LTE:CBWidth \n
		Snippet: driver.configure.vse.measurement.iqRecorder.lte.set_cbwidth(channel_bandwidth = enums.LteChannelBandwidth.F10M) \n
		No command help available \n
			:param channel_bandwidth: No help available
		"""
		param = Conversions.enum_scalar_to_str(channel_bandwidth, enums.LteChannelBandwidth)
		self._core.io.write(f'CONFigure:VSE:MEASurement<Instance>:IQRecorder:LTE:CBWidth {param}')
