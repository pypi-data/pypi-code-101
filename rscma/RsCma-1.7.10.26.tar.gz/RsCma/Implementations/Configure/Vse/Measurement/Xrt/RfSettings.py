from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RfSettings:
	"""RfSettings commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rfSettings", core, parent)

	# noinspection PyTypeChecker
	def get_connector(self) -> enums.XrtInputConnector:
		"""SCPI: CONFigure:VSE:MEASurement<Instance>:XRT:RFSettings:CONNector \n
		Snippet: value: enums.XrtInputConnector = driver.configure.vse.measurement.xrt.rfSettings.get_connector() \n
		No command help available \n
			:return: input_connector: No help available
		"""
		response = self._core.io.query_str('CONFigure:VSE:MEASurement<Instance>:XRT:RFSettings:CONNector?')
		return Conversions.str_to_scalar_enum(response, enums.XrtInputConnector)

	def set_connector(self, input_connector: enums.XrtInputConnector) -> None:
		"""SCPI: CONFigure:VSE:MEASurement<Instance>:XRT:RFSettings:CONNector \n
		Snippet: driver.configure.vse.measurement.xrt.rfSettings.set_connector(input_connector = enums.XrtInputConnector.RF1) \n
		No command help available \n
			:param input_connector: No help available
		"""
		param = Conversions.enum_scalar_to_str(input_connector, enums.XrtInputConnector)
		self._core.io.write(f'CONFigure:VSE:MEASurement<Instance>:XRT:RFSettings:CONNector {param}')

	def get_frequency(self) -> float:
		"""SCPI: CONFigure:VSE:MEASurement<Instance>:XRT:RFSettings:FREQuency \n
		Snippet: value: float = driver.configure.vse.measurement.xrt.rfSettings.get_frequency() \n
		No command help available \n
			:return: frequency: No help available
		"""
		response = self._core.io.query_str('CONFigure:VSE:MEASurement<Instance>:XRT:RFSettings:FREQuency?')
		return Conversions.str_to_float(response)

	def set_frequency(self, frequency: float) -> None:
		"""SCPI: CONFigure:VSE:MEASurement<Instance>:XRT:RFSettings:FREQuency \n
		Snippet: driver.configure.vse.measurement.xrt.rfSettings.set_frequency(frequency = 1.0) \n
		No command help available \n
			:param frequency: No help available
		"""
		param = Conversions.decimal_value_to_str(frequency)
		self._core.io.write(f'CONFigure:VSE:MEASurement<Instance>:XRT:RFSettings:FREQuency {param}')

	def get_envelope_power(self) -> float:
		"""SCPI: CONFigure:VSE:MEASurement<Instance>:XRT:RFSettings:ENPower \n
		Snippet: value: float = driver.configure.vse.measurement.xrt.rfSettings.get_envelope_power() \n
		No command help available \n
			:return: exp_nominal_power: No help available
		"""
		response = self._core.io.query_str('CONFigure:VSE:MEASurement<Instance>:XRT:RFSettings:ENPower?')
		return Conversions.str_to_float(response)

	def set_envelope_power(self, exp_nominal_power: float) -> None:
		"""SCPI: CONFigure:VSE:MEASurement<Instance>:XRT:RFSettings:ENPower \n
		Snippet: driver.configure.vse.measurement.xrt.rfSettings.set_envelope_power(exp_nominal_power = 1.0) \n
		No command help available \n
			:param exp_nominal_power: No help available
		"""
		param = Conversions.decimal_value_to_str(exp_nominal_power)
		self._core.io.write(f'CONFigure:VSE:MEASurement<Instance>:XRT:RFSettings:ENPower {param}')
