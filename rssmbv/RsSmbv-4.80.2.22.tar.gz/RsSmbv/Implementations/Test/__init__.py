from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ...Internal.Utilities import trim_str_response
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Test:
	"""Test commands group definition. 38 total commands, 10 Sub-groups, 6 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("test", core, parent)

	@property
	def all(self):
		"""all commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_all'):
			from .All import All
			self._all = All(self._core, self._cmd_group)
		return self._all

	@property
	def baseband(self):
		"""baseband commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_baseband'):
			from .Baseband import Baseband
			self._baseband = Baseband(self._core, self._cmd_group)
		return self._baseband

	@property
	def bb(self):
		"""bb commands group. 3 Sub-classes, 1 commands."""
		if not hasattr(self, '_bb'):
			from .Bb import Bb
			self._bb = Bb(self._core, self._cmd_group)
		return self._bb

	@property
	def device(self):
		"""device commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_device'):
			from .Device import Device
			self._device = Device(self._core, self._cmd_group)
		return self._device

	@property
	def hs(self):
		"""hs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hs'):
			from .Hs import Hs
			self._hs = Hs(self._core, self._cmd_group)
		return self._hs

	@property
	def remote(self):
		"""remote commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_remote'):
			from .Remote import Remote
			self._remote = Remote(self._core, self._cmd_group)
		return self._remote

	@property
	def res(self):
		"""res commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_res'):
			from .Res import Res
			self._res = Res(self._core, self._cmd_group)
		return self._res

	@property
	def serror(self):
		"""serror commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_serror'):
			from .Serror import Serror
			self._serror = Serror(self._core, self._cmd_group)
		return self._serror

	@property
	def sw(self):
		"""sw commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_sw'):
			from .Sw import Sw
			self._sw = Sw(self._core, self._cmd_group)
		return self._sw

	@property
	def write(self):
		"""write commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_write'):
			from .Write import Write
			self._write = Write(self._core, self._cmd_group)
		return self._write

	def get_bbin(self) -> bool:
		"""SCPI: TEST:BBIN \n
		Snippet: value: bool = driver.test.get_bbin() \n
		No command help available \n
			:return: bbin: No help available
		"""
		response = self._core.io.query_str('TEST:BBIN?')
		return Conversions.str_to_bool(response)

	# noinspection PyTypeChecker
	def get_eiq_mode(self) -> enums.TestExtIqMode:
		"""SCPI: TEST:EIQMode \n
		Snippet: value: enums.TestExtIqMode = driver.test.get_eiq_mode() \n
		No command help available \n
			:return: eiq_mode: No help available
		"""
		response = self._core.io.query_str('TEST:EIQMode?')
		return Conversions.str_to_scalar_enum(response, enums.TestExtIqMode)

	def set_eiq_mode(self, eiq_mode: enums.TestExtIqMode) -> None:
		"""SCPI: TEST:EIQMode \n
		Snippet: driver.test.set_eiq_mode(eiq_mode = enums.TestExtIqMode.IQIN) \n
		No command help available \n
			:param eiq_mode: No help available
		"""
		param = Conversions.enum_scalar_to_str(eiq_mode, enums.TestExtIqMode)
		self._core.io.write(f'TEST:EIQMode {param}')

	def get_frc(self) -> str:
		"""SCPI: TEST:FRC \n
		Snippet: value: str = driver.test.get_frc() \n
		No command help available \n
			:return: test_freq_resp_cor: No help available
		"""
		response = self._core.io.query_str('TEST:FRC?')
		return trim_str_response(response)

	def set_frc(self, test_freq_resp_cor: str) -> None:
		"""SCPI: TEST:FRC \n
		Snippet: driver.test.set_frc(test_freq_resp_cor = '1') \n
		No command help available \n
			:param test_freq_resp_cor: No help available
		"""
		param = Conversions.value_to_quoted_str(test_freq_resp_cor)
		self._core.io.write(f'TEST:FRC {param}')

	# noinspection PyTypeChecker
	def get_level(self) -> enums.SelftLev:
		"""SCPI: TEST:LEVel \n
		Snippet: value: enums.SelftLev = driver.test.get_level() \n
		No command help available \n
			:return: level: No help available
		"""
		response = self._core.io.query_str('TEST:LEVel?')
		return Conversions.str_to_scalar_enum(response, enums.SelftLev)

	def set_level(self, level: enums.SelftLev) -> None:
		"""SCPI: TEST:LEVel \n
		Snippet: driver.test.set_level(level = enums.SelftLev.CUSTomer) \n
		No command help available \n
			:param level: No help available
		"""
		param = Conversions.enum_scalar_to_str(level, enums.SelftLev)
		self._core.io.write(f'TEST:LEVel {param}')

	def set_nrp_trigger(self, nrp_trigger: bool) -> None:
		"""SCPI: TEST:NRPTrigger \n
		Snippet: driver.test.set_nrp_trigger(nrp_trigger = False) \n
		No command help available \n
			:param nrp_trigger: No help available
		"""
		param = Conversions.bool_to_str(nrp_trigger)
		self._core.io.write(f'TEST:NRPTrigger {param}')

	def preset(self) -> None:
		"""SCPI: TEST:PRESet \n
		Snippet: driver.test.preset() \n
		No command help available \n
		"""
		self._core.io.write(f'TEST:PRESet')

	def preset_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: TEST:PRESet \n
		Snippet: driver.test.preset_with_opc() \n
		No command help available \n
		Same as preset, but waits for the operation to complete before continuing further. Use the RsSmbv.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'TEST:PRESet', opc_timeout_ms)

	def clone(self) -> 'Test':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Test(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
