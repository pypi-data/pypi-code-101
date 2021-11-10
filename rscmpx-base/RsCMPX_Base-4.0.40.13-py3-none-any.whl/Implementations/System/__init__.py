from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ...Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class System:
	"""System commands group definition. 100 total commands, 21 Sub-groups, 9 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("system", core, parent)

	@property
	def base(self):
		"""base commands group. 8 Sub-classes, 1 commands."""
		if not hasattr(self, '_base'):
			from .Base import Base
			self._base = Base(self._core, self._cmd_group)
		return self._base

	@property
	def connector(self):
		"""connector commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_connector'):
			from .Connector import Connector
			self._connector = Connector(self._core, self._cmd_group)
		return self._connector

	@property
	def routing(self):
		"""routing commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_routing'):
			from .Routing import Routing
			self._routing = Routing(self._core, self._cmd_group)
		return self._routing

	@property
	def help(self):
		"""help commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_help'):
			from .Help import Help
			self._help = Help(self._core, self._cmd_group)
		return self._help

	@property
	def record(self):
		"""record commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_record'):
			from .Record import Record
			self._record = Record(self._core, self._cmd_group)
		return self._record

	@property
	def startup(self):
		"""startup commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_startup'):
			from .Startup import Startup
			self._startup = Startup(self._core, self._cmd_group)
		return self._startup

	@property
	def cmw(self):
		"""cmw commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_cmw'):
			from .Cmw import Cmw
			self._cmw = Cmw(self._core, self._cmd_group)
		return self._cmw

	@property
	def update(self):
		"""update commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_update'):
			from .Update import Update
			self._update = Update(self._core, self._cmd_group)
		return self._update

	@property
	def communicate(self):
		"""communicate commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_communicate'):
			from .Communicate import Communicate
			self._communicate = Communicate(self._core, self._cmd_group)
		return self._communicate

	@property
	def singleCmw(self):
		"""singleCmw commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_singleCmw'):
			from .SingleCmw import SingleCmw
			self._singleCmw = SingleCmw(self._core, self._cmd_group)
		return self._singleCmw

	@property
	def password(self):
		"""password commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_password'):
			from .Password import Password
			self._password = Password(self._core, self._cmd_group)
		return self._password

	@property
	def display(self):
		"""display commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_display'):
			from .Display import Display
			self._display = Display(self._core, self._cmd_group)
		return self._display

	@property
	def deviceFootprint(self):
		"""deviceFootprint commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_deviceFootprint'):
			from .DeviceFootprint import DeviceFootprint
			self._deviceFootprint = DeviceFootprint(self._core, self._cmd_group)
		return self._deviceFootprint

	@property
	def generator(self):
		"""generator commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_generator'):
			from .Generator import Generator
			self._generator = Generator(self._core, self._cmd_group)
		return self._generator

	@property
	def measurement(self):
		"""measurement commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_measurement'):
			from .Measurement import Measurement
			self._measurement = Measurement(self._core, self._cmd_group)
		return self._measurement

	@property
	def signaling(self):
		"""signaling commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_signaling'):
			from .Signaling import Signaling
			self._signaling = Signaling(self._core, self._cmd_group)
		return self._signaling

	@property
	def time(self):
		"""time commands group. 4 Sub-classes, 1 commands."""
		if not hasattr(self, '_time'):
			from .Time import Time
			self._time = Time(self._core, self._cmd_group)
		return self._time

	@property
	def device(self):
		"""device commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_device'):
			from .Device import Device
			self._device = Device(self._core, self._cmd_group)
		return self._device

	@property
	def date(self):
		"""date commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_date'):
			from .Date import Date
			self._date = Date(self._core, self._cmd_group)
		return self._date

	@property
	def tzone(self):
		"""tzone commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tzone'):
			from .Tzone import Tzone
			self._tzone = Tzone(self._core, self._cmd_group)
		return self._tzone

	@property
	def error(self):
		"""error commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_error'):
			from .Error import Error
			self._error = Error(self._core, self._cmd_group)
		return self._error

	def get_did(self) -> str:
		"""SCPI: SYSTem:DID \n
		Snippet: value: str = driver.system.get_did() \n
		No command help available \n
			:return: device_id: No help available
		"""
		response = self._core.io.query_str('SYSTem:DID?')
		return trim_str_response(response)

	def get_klock(self) -> bool:
		"""SCPI: SYSTem:KLOCk \n
		Snippet: value: bool = driver.system.get_klock() \n
		No command help available \n
			:return: klock: No help available
		"""
		response = self._core.io.query_str('SYSTem:KLOCk?')
		return Conversions.str_to_bool(response)

	def set_klock(self, klock: bool) -> None:
		"""SCPI: SYSTem:KLOCk \n
		Snippet: driver.system.set_klock(klock = False) \n
		No command help available \n
			:param klock: No help available
		"""
		param = Conversions.bool_to_str(klock)
		self._core.io.write(f'SYSTem:KLOCk {param}')

	def preset(self, appl_name_and_li_number: str = None) -> None:
		"""SCPI: SYSTem:PRESet \n
		Snippet: driver.system.preset(appl_name_and_li_number = '1') \n
		No command help available \n
			:param appl_name_and_li_number: No help available
		"""
		param = ''
		if appl_name_and_li_number:
			param = Conversions.value_to_quoted_str(appl_name_and_li_number)
		self._core.io.write(f'SYSTem:PRESet {param}'.strip())

	def preset_all(self) -> None:
		"""SCPI: SYSTem:PRESet:ALL \n
		Snippet: driver.system.preset_all() \n
		No command help available \n
		"""
		self._core.io.write(f'SYSTem:PRESet:ALL')

	def preset_all_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: SYSTem:PRESet:ALL \n
		Snippet: driver.system.preset_all_with_opc() \n
		No command help available \n
		Same as preset_all, but waits for the operation to complete before continuing further. Use the RsCMPX_Base.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SYSTem:PRESet:ALL', opc_timeout_ms)

	def preset_base(self) -> None:
		"""SCPI: SYSTem:PRESet:BASE \n
		Snippet: driver.system.preset_base() \n
		No command help available \n
		"""
		self._core.io.write(f'SYSTem:PRESet:BASE')

	def preset_base_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: SYSTem:PRESet:BASE \n
		Snippet: driver.system.preset_base_with_opc() \n
		No command help available \n
		Same as preset_base, but waits for the operation to complete before continuing further. Use the RsCMPX_Base.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SYSTem:PRESet:BASE', opc_timeout_ms)

	def reset(self, appl_name_and_li_number: str = None) -> None:
		"""SCPI: SYSTem:RESet \n
		Snippet: driver.system.reset(appl_name_and_li_number = '1') \n
		No command help available \n
			:param appl_name_and_li_number: No help available
		"""
		param = ''
		if appl_name_and_li_number:
			param = Conversions.value_to_quoted_str(appl_name_and_li_number)
		self._core.io.write(f'SYSTem:RESet {param}'.strip())

	def reset_all(self) -> None:
		"""SCPI: SYSTem:RESet:ALL \n
		Snippet: driver.system.reset_all() \n
		No command help available \n
		"""
		self._core.io.write(f'SYSTem:RESet:ALL')

	def reset_all_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: SYSTem:RESet:ALL \n
		Snippet: driver.system.reset_all_with_opc() \n
		No command help available \n
		Same as reset_all, but waits for the operation to complete before continuing further. Use the RsCMPX_Base.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SYSTem:RESet:ALL', opc_timeout_ms)

	def reset_base(self) -> None:
		"""SCPI: SYSTem:RESet:BASE \n
		Snippet: driver.system.reset_base() \n
		No command help available \n
		"""
		self._core.io.write(f'SYSTem:RESet:BASE')

	def reset_base_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: SYSTem:RESet:BASE \n
		Snippet: driver.system.reset_base_with_opc() \n
		No command help available \n
		Same as reset_base, but waits for the operation to complete before continuing further. Use the RsCMPX_Base.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SYSTem:RESet:BASE', opc_timeout_ms)

	def get_version(self) -> float:
		"""SCPI: SYSTem:VERSion \n
		Snippet: value: float = driver.system.get_version() \n
		Queries the SCPI version number to which the instrument complies. \n
			:return: version: '1999.0' is the final SCPI version.
		"""
		response = self._core.io.query_str('SYSTem:VERSion?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'System':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = System(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
