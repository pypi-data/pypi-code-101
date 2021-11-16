from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Measurement:
	"""Measurement commands group definition. 10 total commands, 3 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("measurement", core, parent)

	@property
	def scenario(self):
		"""scenario commands group. 4 Sub-classes, 2 commands."""
		if not hasattr(self, '_scenario'):
			from .Scenario import Scenario
			self._scenario = Scenario(self._core, self._cmd_group)
		return self._scenario

	@property
	def rfSettings(self):
		"""rfSettings commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rfSettings'):
			from .RfSettings import RfSettings
			self._rfSettings = RfSettings(self._core, self._cmd_group)
		return self._rfSettings

	@property
	def spath(self):
		"""spath commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_spath'):
			from .Spath import Spath
			self._spath = Spath(self._core, self._cmd_group)
		return self._spath

	# noinspection PyTypeChecker
	class ValueStruct(StructBase):  # From ReadStructDefinition CmdPropertyTemplate.xml
		"""Structure for reading output parameters. Fields: \n
			- Scenario: enums.MeasScenario: No parameter help available
			- Master: str: No parameter help available
			- Rf_Connector: enums.RfConnector: No parameter help available
			- Rf_Converter: enums.RxConverter: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Scenario', enums.MeasScenario),
			ArgStruct.scalar_str('Master'),
			ArgStruct.scalar_enum('Rf_Connector', enums.RfConnector),
			ArgStruct.scalar_enum('Rf_Converter', enums.RxConverter)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Scenario: enums.MeasScenario = None
			self.Master: str = None
			self.Rf_Connector: enums.RfConnector = None
			self.Rf_Converter: enums.RxConverter = None

	def get_value(self) -> ValueStruct:
		"""SCPI: ROUTe:GPRF:MEASurement<Instance> \n
		Snippet: value: ValueStruct = driver.route.gprf.measurement.get_value() \n
		No command help available \n
			:return: structure: for return value, see the help for ValueStruct structure arguments.
		"""
		return self._core.io.query_struct('ROUTe:GPRF:MEASurement<Instance>?', self.__class__.ValueStruct())

	def clone(self) -> 'Measurement':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Measurement(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
