from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ...Internal.StructBase import StructBase
from ...Internal.ArgStruct import ArgStruct
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Calibration:
	"""Calibration commands group definition. 26 total commands, 7 Sub-groups, 7 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("calibration", core, parent)

	@property
	def current(self):
		"""current commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_current'):
			from .Current import Current
			self._current = Current(self._core, self._cmd_group)
		return self._current

	@property
	def voltage(self):
		"""voltage commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_voltage'):
			from .Voltage import Voltage
			self._voltage = Voltage(self._core, self._cmd_group)
		return self._voltage

	@property
	def end(self):
		"""end commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_end'):
			from .End import End
			self._end = End(self._core, self._cmd_group)
		return self._end

	@property
	def cancel(self):
		"""cancel commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cancel'):
			from .Cancel import Cancel
			self._cancel = Cancel(self._core, self._cmd_group)
		return self._cancel

	@property
	def ainput(self):
		"""ainput commands group. 5 Sub-classes, 4 commands."""
		if not hasattr(self, '_ainput'):
			from .Ainput import Ainput
			self._ainput = Ainput(self._core, self._cmd_group)
		return self._ainput

	@property
	def point(self):
		"""point commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_point'):
			from .Point import Point
			self._point = Point(self._core, self._cmd_group)
		return self._point

	@property
	def self(self):
		"""self commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_self'):
			from .Self import Self
			self._self = Self(self._core, self._cmd_group)
		return self._self

	# noinspection PyTypeChecker
	class DateStruct(StructBase):  # From ReadStructDefinition CmdPropertyTemplate.xml
		"""Structure for reading output parameters. Fields: \n
			- Arg_0: float: No parameter help available
			- Arg_1: float: No parameter help available
			- Arg_2: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_float('Arg_0'),
			ArgStruct.scalar_float('Arg_1'),
			ArgStruct.scalar_float('Arg_2')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Arg_0: float = None
			self.Arg_1: float = None
			self.Arg_2: float = None

	def get_date(self) -> DateStruct:
		"""SCPI: CALibration:DATE \n
		Snippet: value: DateStruct = driver.calibration.get_date() \n
		Returns the channel adjustment date. \n
			:return: structure: for return value, see the help for DateStruct structure arguments.
		"""
		return self._core.io.query_struct('CALibration:DATE?', self.__class__.DateStruct())

	# noinspection PyTypeChecker
	def get_type_py(self) -> enums.CalibrationType:
		"""SCPI: CALibration:TYPE \n
		Snippet: value: enums.CalibrationType = driver.calibration.get_type_py() \n
		No command help available \n
			:return: arg_0: (enum or string) No help available
		"""
		response = self._core.io.query_str('CALibration:TYPE?')
		return Conversions.str_to_scalar_enum_ext(response, enums.CalibrationType)

	def set_type_py(self, arg_0: enums.CalibrationType) -> None:
		"""SCPI: CALibration:TYPE \n
		Snippet: driver.calibration.set_type_py(arg_0 = enums.CalibrationType.CURR) \n
		No command help available \n
			:param arg_0: (enum or string) No help available
		"""
		param = Conversions.enum_ext_scalar_to_str(arg_0, enums.CalibrationType)
		self._core.io.write(f'CALibration:TYPE {param}')

	def get_value(self) -> float:
		"""SCPI: CALibration:VALue \n
		Snippet: value: float = driver.calibration.get_value() \n
		No command help available \n
			:return: arg_0: No help available
		"""
		response = self._core.io.query_str('CALibration:VALue?')
		return Conversions.str_to_float(response)

	def set_value(self, arg_0: float) -> None:
		"""SCPI: CALibration:VALue \n
		Snippet: driver.calibration.set_value(arg_0 = 1.0) \n
		No command help available \n
			:param arg_0: No help available
		"""
		param = Conversions.decimal_value_to_str(arg_0)
		self._core.io.write(f'CALibration:VALue {param}')

	def get_user(self) -> bool:
		"""SCPI: CALibration:USER \n
		Snippet: value: bool = driver.calibration.get_user() \n
		Starts the channel adjustment process. \n
			:return: arg_0: No help available
		"""
		response = self._core.io.query_str('CALibration:USER?')
		return Conversions.str_to_bool(response)

	def set_user(self, arg_0: bool) -> None:
		"""SCPI: CALibration:USER \n
		Snippet: driver.calibration.set_user(arg_0 = False) \n
		Starts the channel adjustment process. \n
			:param arg_0: No help available
		"""
		param = Conversions.bool_to_str(arg_0)
		self._core.io.write(f'CALibration:USER {param}')

	def save(self) -> None:
		"""SCPI: CALibration:SAVE \n
		Snippet: driver.calibration.save() \n
		Saves the channel adjustment. \n
		"""
		self._core.io.write(f'CALibration:SAVE')

	def save_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: CALibration:SAVE \n
		Snippet: driver.calibration.save_with_opc() \n
		Saves the channel adjustment. \n
		Same as save, but waits for the operation to complete before continuing further. Use the RsNgx.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'CALibration:SAVE', opc_timeout_ms)

	def get_temperature(self) -> float:
		"""SCPI: CALibration:TEMPerature \n
		Snippet: value: float = driver.calibration.get_temperature() \n
		Returns the temperature of selected channel. \n
			:return: result: No help available
		"""
		response = self._core.io.query_str('CALibration:TEMPerature?')
		return Conversions.str_to_float(response)

	def get_count(self) -> float:
		"""SCPI: CALibration:COUNt \n
		Snippet: value: float = driver.calibration.get_count() \n
		Queries the number of counts channel adjustment performed successfully. \n
			:return: result: No help available
		"""
		response = self._core.io.query_str('CALibration:COUNt?')
		return Conversions.str_to_float(response)
