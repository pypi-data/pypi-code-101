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

	def set(self, tx_connector: enums.TxConnector, rf_converter: enums.TxConverter) -> None:
		"""SCPI: ROUTe:GPRF:GENerator<Instance>:SCENario:SALone \n
		Snippet: driver.route.gprf.generator.scenario.salone.set(tx_connector = enums.TxConnector.I12O, rf_converter = enums.TxConverter.ITX1) \n
		Selects the signal path for the generated signal, for signal output via an R&S CMW500. Send the command to the R&S
		CMW500/R&S CMWC.
			INTRO_CMD_HELP: Value combinations: \n
			- RF 1 COM, RF 2 COM, RF 1 OUT are compatible with TX 1 and TX 3.
			- RF 3 COM, RF 4 COM, RF 3 OUT are compatible with TX 2 and TX 4.
		Note: This command is an interim solution. It is planned to replace this command in a later software version. \n
			:param tx_connector: RF connector for the output path Single R&S CMW500: RFnC for RF n COM RFnO for RF n OUT CMWflexx: RabC for CMW a, connector RF b COM RabO for CMW a, connector RF b OUT
			:param rf_converter: TX module for the output path Single R&S CMW500: TX1 to TX4 CMWflexx: TXab for CMW a, TX b
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('tx_connector', tx_connector, DataType.Enum, enums.TxConnector), ArgSingle('rf_converter', rf_converter, DataType.Enum, enums.TxConverter))
		self._core.io.write(f'ROUTe:GPRF:GENerator<Instance>:SCENario:SALone {param}'.rstrip())

	# noinspection PyTypeChecker
	class SaloneStruct(StructBase):
		"""Response structure. Fields: \n
			- Tx_Connector: enums.TxConnector: RF connector for the output path Single R&S CMW500: RFnC for RF n COM RFnO for RF n OUT CMWflexx: RabC for CMW a, connector RF b COM RabO for CMW a, connector RF b OUT
			- Rf_Converter: enums.TxConverter: TX module for the output path Single R&S CMW500: TX1 to TX4 CMWflexx: TXab for CMW a, TX b"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Tx_Connector', enums.TxConnector),
			ArgStruct.scalar_enum('Rf_Converter', enums.TxConverter)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Tx_Connector: enums.TxConnector = None
			self.Rf_Converter: enums.TxConverter = None

	def get(self) -> SaloneStruct:
		"""SCPI: ROUTe:GPRF:GENerator<Instance>:SCENario:SALone \n
		Snippet: value: SaloneStruct = driver.route.gprf.generator.scenario.salone.get() \n
		Selects the signal path for the generated signal, for signal output via an R&S CMW500. Send the command to the R&S
		CMW500/R&S CMWC.
			INTRO_CMD_HELP: Value combinations: \n
			- RF 1 COM, RF 2 COM, RF 1 OUT are compatible with TX 1 and TX 3.
			- RF 3 COM, RF 4 COM, RF 3 OUT are compatible with TX 2 and TX 4.
		Note: This command is an interim solution. It is planned to replace this command in a later software version. \n
			:return: structure: for return value, see the help for SaloneStruct structure arguments."""
		return self._core.io.query_struct(f'ROUTe:GPRF:GENerator<Instance>:SCENario:SALone?', self.__class__.SaloneStruct())
