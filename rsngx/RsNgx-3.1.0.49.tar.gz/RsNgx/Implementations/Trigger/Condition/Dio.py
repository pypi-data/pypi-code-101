from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle
from ....Internal.RepeatedCapability import RepeatedCapability
from .... import enums
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dio:
	"""Dio commands group definition. 1 total commands, 0 Sub-groups, 1 group commands
	Repeated Capability: DigitalIo, default value after init: DigitalIo.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dio", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_digitalIo_get', 'repcap_digitalIo_set', repcap.DigitalIo.Nr1)

	def repcap_digitalIo_set(self, digitalIo: repcap.DigitalIo) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to DigitalIo.Default
		Default value after init: DigitalIo.Nr1"""
		self._cmd_group.set_repcap_enum_value(digitalIo)

	def repcap_digitalIo_get(self) -> repcap.DigitalIo:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def set(self, arg_0: enums.TriggerCondition, arg_1: float = None, digitalIo=repcap.DigitalIo.Default) -> None:
		"""SCPI: TRIGger:CONDition:DIO<IO> \n
		Snippet: driver.trigger.condition.dio.set(arg_0 = enums.TriggerCondition.ANINput, arg_1 = 1.0, digitalIo = repcap.DigitalIo.Default) \n
		Sets the trigger condition of the specified Digital I/O line. \n
			:param arg_0: No help available
			:param arg_1: No help available
			:param digitalIo: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Dio')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('arg_0', arg_0, DataType.Enum, enums.TriggerCondition), ArgSingle('arg_1', arg_1, DataType.Float, None, is_optional=True))
		digitalIo_cmd_val = self._cmd_group.get_repcap_cmd_value(digitalIo, repcap.DigitalIo)
		self._core.io.write(f'TRIGger:CONDition:DIO{digitalIo_cmd_val} {param}'.rstrip())

	# noinspection PyTypeChecker
	class DioStruct(StructBase):
		"""Response structure. Fields: \n
			- Arg_0: enums.TriggerCondition: No parameter help available
			- Arg_1: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Arg_0', enums.TriggerCondition),
			ArgStruct.scalar_float('Arg_1')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Arg_0: enums.TriggerCondition = None
			self.Arg_1: float = None

	def get(self, digitalIo=repcap.DigitalIo.Default) -> DioStruct:
		"""SCPI: TRIGger:CONDition:DIO<IO> \n
		Snippet: value: DioStruct = driver.trigger.condition.dio.get(digitalIo = repcap.DigitalIo.Default) \n
		Sets the trigger condition of the specified Digital I/O line. \n
			:param digitalIo: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Dio')
			:return: structure: for return value, see the help for DioStruct structure arguments."""
		digitalIo_cmd_val = self._cmd_group.get_repcap_cmd_value(digitalIo, repcap.DigitalIo)
		return self._core.io.query_struct(f'TRIGger:CONDition:DIO{digitalIo_cmd_val}?', self.__class__.DioStruct())
