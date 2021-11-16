from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Test:
	"""Test commands group definition. 17 total commands, 9 Sub-groups, 3 group commands"""

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
	def bb(self):
		"""bb commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bb'):
			from .Bb import Bb
			self._bb = Bb(self._core, self._cmd_group)
		return self._bb

	@property
	def bbin(self):
		"""bbin commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_bbin'):
			from .Bbin import Bbin
			self._bbin = Bbin(self._core, self._cmd_group)
		return self._bbin

	@property
	def connector(self):
		"""connector commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_connector'):
			from .Connector import Connector
			self._connector = Connector(self._core, self._cmd_group)
		return self._connector

	@property
	def keyboard(self):
		"""keyboard commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_keyboard'):
			from .Keyboard import Keyboard
			self._keyboard = Keyboard(self._core, self._cmd_group)
		return self._keyboard

	@property
	def remote(self):
		"""remote commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_remote'):
			from .Remote import Remote
			self._remote = Remote(self._core, self._cmd_group)
		return self._remote

	@property
	def res(self):
		"""res commands group. 0 Sub-classes, 2 commands."""
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

	# noinspection PyTypeChecker
	def get_eiq_mode(self) -> enums.TestExtIqMode:
		"""SCPI: TEST:EIQMode \n
		Snippet: value: enums.TestExtIqMode = driver.test.get_eiq_mode() \n
		Triggers a connection test for testing the active external IQ devices. \n
			:return: eiq_mode: IQIN| IQOut
		"""
		response = self._core.io.query_str('TEST:EIQMode?')
		return Conversions.str_to_scalar_enum(response, enums.TestExtIqMode)

	def set_eiq_mode(self, eiq_mode: enums.TestExtIqMode) -> None:
		"""SCPI: TEST:EIQMode \n
		Snippet: driver.test.set_eiq_mode(eiq_mode = enums.TestExtIqMode.IQIN) \n
		Triggers a connection test for testing the active external IQ devices. \n
			:param eiq_mode: IQIN| IQOut
		"""
		param = Conversions.enum_scalar_to_str(eiq_mode, enums.TestExtIqMode)
		self._core.io.write(f'TEST:EIQMode {param}')

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
		Same as preset, but waits for the operation to complete before continuing further. Use the RsSgt.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'TEST:PRESet', opc_timeout_ms)

	def clone(self) -> 'Test':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Test(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
