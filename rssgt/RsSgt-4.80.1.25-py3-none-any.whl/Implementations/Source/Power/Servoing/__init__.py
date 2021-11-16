from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Servoing:
	"""Servoing commands group definition. 8 total commands, 1 Sub-groups, 6 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("servoing", core, parent)

	@property
	def sensor(self):
		"""sensor commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_sensor'):
			from .Sensor import Sensor
			self._sensor = Sensor(self._core, self._cmd_group)
		return self._sensor

	# noinspection PyTypeChecker
	class SetStruct(StructBase):  # From ReadStructDefinition CmdPropertyTemplate.xml
		"""Structure for reading output parameters. Fields: \n
			- Target: float: float Sets the target output power level at the DUT.
			- Start: enums.Test: 0| 1| RUNning| STOPped Queries the current status of the powerservoing procedure."""
		__meta_args_list = [
			ArgStruct.scalar_float('Target'),
			ArgStruct.scalar_enum('Start', enums.Test)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Target: float = None
			self.Start: enums.Test = None

	def get_set(self) -> SetStruct:
		"""SCPI: [SOURce<HW>]:POWer:SERVoing:SET \n
		Snippet: value: SetStruct = driver.source.power.servoing.get_set() \n
		Sets the target output power level and queries power servoing procedure status. \n
			:return: structure: for return value, see the help for SetStruct structure arguments.
		"""
		return self._core.io.query_struct('SOURce<HwInstance>:POWer:SERVoing:SET?', self.__class__.SetStruct())

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:POWer:SERVoing:STATe \n
		Snippet: value: bool = driver.source.power.servoing.get_state() \n
		Activates/deactivates power servoing. \n
			:return: state: 0| 1| OFF| ON
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:POWer:SERVoing:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:POWer:SERVoing:STATe \n
		Snippet: driver.source.power.servoing.set_state(state = False) \n
		Activates/deactivates power servoing. \n
			:param state: 0| 1| OFF| ON
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:POWer:SERVoing:STATe {param}')

	def get_target(self) -> float:
		"""SCPI: [SOURce<HW>]:POWer:SERVoing:TARGet \n
		Snippet: value: float = driver.source.power.servoing.get_target() \n
		Sets the target output power level required at the DUT. \n
			:return: target_level: float Range: -120 to 25
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:POWer:SERVoing:TARGet?')
		return Conversions.str_to_float(response)

	def set_target(self, target_level: float) -> None:
		"""SCPI: [SOURce<HW>]:POWer:SERVoing:TARGet \n
		Snippet: driver.source.power.servoing.set_target(target_level = 1.0) \n
		Sets the target output power level required at the DUT. \n
			:param target_level: float Range: -120 to 25
		"""
		param = Conversions.decimal_value_to_str(target_level)
		self._core.io.write(f'SOURce<HwInstance>:POWer:SERVoing:TARGet {param}')

	# noinspection PyTypeChecker
	def get_test(self) -> enums.Test:
		"""SCPI: [SOURce<HW>]:POWer:SERVoing:TEST \n
		Snippet: value: enums.Test = driver.source.power.servoing.get_test() \n
		Queries the state of the power servoing procedure. \n
			:return: start: 0| 1| RUNning| STOPped
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:POWer:SERVoing:TEST?')
		return Conversions.str_to_scalar_enum(response, enums.Test)

	def get_tolerance(self) -> float:
		"""SCPI: [SOURce<HW>]:POWer:SERVoing:TOLerance \n
		Snippet: value: float = driver.source.power.servoing.get_tolerance() \n
		Sets the tolerance level interval, in which the 'Target' output power level of the DUT lies.
		A large tolerance accelerates the power servoing procedure but also reduces the accuracy of the target output power level. \n
			:return: tolerance: float Range: 0.01 to 3
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:POWer:SERVoing:TOLerance?')
		return Conversions.str_to_float(response)

	def set_tolerance(self, tolerance: float) -> None:
		"""SCPI: [SOURce<HW>]:POWer:SERVoing:TOLerance \n
		Snippet: driver.source.power.servoing.set_tolerance(tolerance = 1.0) \n
		Sets the tolerance level interval, in which the 'Target' output power level of the DUT lies.
		A large tolerance accelerates the power servoing procedure but also reduces the accuracy of the target output power level. \n
			:param tolerance: float Range: 0.01 to 3
		"""
		param = Conversions.decimal_value_to_str(tolerance)
		self._core.io.write(f'SOURce<HwInstance>:POWer:SERVoing:TOLerance {param}')

	def get_tracking(self) -> bool:
		"""SCPI: [SOURce<HW>]:POWer:SERVoing:TRACking \n
		Snippet: value: bool = driver.source.power.servoing.get_tracking() \n
		Activates/deactivates level tracking. Activation increases measurement accuracy but also measurement time. \n
			:return: state: 0| 1| OFF| ON
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:POWer:SERVoing:TRACking?')
		return Conversions.str_to_bool(response)

	def set_tracking(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:POWer:SERVoing:TRACking \n
		Snippet: driver.source.power.servoing.set_tracking(state = False) \n
		Activates/deactivates level tracking. Activation increases measurement accuracy but also measurement time. \n
			:param state: 0| 1| OFF| ON
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:POWer:SERVoing:TRACking {param}')

	def clone(self) -> 'Servoing':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Servoing(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
