from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Salone:
	"""Salone commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("salone", core, parent)

	def set(self, rx_connector: enums.RfConnector, rf_converter: enums.RxConverter) -> None:
		"""SCPI: ROUTe:GPRF:MEASurement<Instance>:SCENario:SALone \n
		Snippet: driver.route.gprf.measurement.scenario.salone.set(rx_connector = enums.RfConnector.I11I, rf_converter = enums.RxConverter.IRX1) \n
		Selects the signal path for the measured signal, for signal input via an R&S CMW500 and Device Mode = CMW.
		Send the command to the R&S CMW500/R&S CMWC.
			INTRO_CMD_HELP: Value combinations: \n
			- RF 1 COM and RF 2 COM are compatible with TX 1 and TX 3.
			- RF 3 COM and RF 4 COM are compatible with TX 2 and TX 4.
		Note: This command is an interim solution. It is planned to replace this command in a later software version. \n
			:param rx_connector: RF connector for the input path Single R&S CMW500: RFnC for RF n COM CMWflexx: RabC for CMW a, connector RF b COM
			:param rf_converter: RX module for the input path Single R&S CMW500: TX1 to TX4 CMWflexx: TXab for CMW a, TX b
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('rx_connector', rx_connector, DataType.Enum, enums.RfConnector), ArgSingle('rf_converter', rf_converter, DataType.Enum, enums.RxConverter))
		self._core.io.write(f'ROUTe:GPRF:MEASurement<Instance>:SCENario:SALone {param}'.rstrip())

	# noinspection PyTypeChecker
	class SaloneStruct(StructBase):
		"""Response structure. Fields: \n
			- Rx_Connector: enums.RfConnector: RF connector for the input path Single R&S CMW500: RFnC for RF n COM CMWflexx: RabC for CMW a, connector RF b COM
			- Rf_Converter: enums.RxConverter: RX module for the input path Single R&S CMW500: TX1 to TX4 CMWflexx: TXab for CMW a, TX b"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Rx_Connector', enums.RfConnector),
			ArgStruct.scalar_enum('Rf_Converter', enums.RxConverter)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rx_Connector: enums.RfConnector = None
			self.Rf_Converter: enums.RxConverter = None

	def get(self) -> SaloneStruct:
		"""SCPI: ROUTe:GPRF:MEASurement<Instance>:SCENario:SALone \n
		Snippet: value: SaloneStruct = driver.route.gprf.measurement.scenario.salone.get() \n
		Selects the signal path for the measured signal, for signal input via an R&S CMW500 and Device Mode = CMW.
		Send the command to the R&S CMW500/R&S CMWC.
			INTRO_CMD_HELP: Value combinations: \n
			- RF 1 COM and RF 2 COM are compatible with TX 1 and TX 3.
			- RF 3 COM and RF 4 COM are compatible with TX 2 and TX 4.
		Note: This command is an interim solution. It is planned to replace this command in a later software version. \n
			:return: structure: for return value, see the help for SaloneStruct structure arguments."""
		return self._core.io.query_struct(f'ROUTe:GPRF:MEASurement<Instance>:SCENario:SALone?', self.__class__.SaloneStruct())
