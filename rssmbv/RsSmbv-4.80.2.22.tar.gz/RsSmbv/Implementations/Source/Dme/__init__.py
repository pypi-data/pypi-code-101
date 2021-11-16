from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dme:
	"""Dme commands group definition. 12 total commands, 1 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dme", core, parent)

	@property
	def analysis(self):
		"""analysis commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_analysis'):
			from .Analysis import Analysis
			self._analysis = Analysis(self._core, self._cmd_group)
		return self._analysis

	def get_low_emission(self) -> bool:
		"""SCPI: [SOURce<HW>]:DME:LOWemission \n
		Snippet: value: bool = driver.source.dme.get_low_emission() \n
		No command help available \n
			:return: state: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:DME:LOWemission?')
		return Conversions.str_to_bool(response)

	def set_low_emission(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:DME:LOWemission \n
		Snippet: driver.source.dme.set_low_emission(state = False) \n
		No command help available \n
			:param state: No help available
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:DME:LOWemission {param}')

	def preset(self) -> None:
		"""SCPI: [SOURce<HW>]:DME:PRESet \n
		Snippet: driver.source.dme.preset() \n
		No command help available \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:DME:PRESet')

	def preset_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce<HW>]:DME:PRESet \n
		Snippet: driver.source.dme.preset_with_opc() \n
		No command help available \n
		Same as preset, but waits for the operation to complete before continuing further. Use the RsSmbv.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:DME:PRESet', opc_timeout_ms)

	# noinspection PyTypeChecker
	def get_trigger(self) -> enums.VimDmeTrigMode:
		"""SCPI: [SOURce<HW>]:DME:TRIGger \n
		Snippet: value: enums.VimDmeTrigMode = driver.source.dme.get_trigger() \n
		No command help available \n
			:return: trigger_mode: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:DME:TRIGger?')
		return Conversions.str_to_scalar_enum(response, enums.VimDmeTrigMode)

	def set_trigger(self, trigger_mode: enums.VimDmeTrigMode) -> None:
		"""SCPI: [SOURce<HW>]:DME:TRIGger \n
		Snippet: driver.source.dme.set_trigger(trigger_mode = enums.VimDmeTrigMode.AUTO) \n
		No command help available \n
			:param trigger_mode: No help available
		"""
		param = Conversions.enum_scalar_to_str(trigger_mode, enums.VimDmeTrigMode)
		self._core.io.write(f'SOURce<HwInstance>:DME:TRIGger {param}')

	def clone(self) -> 'Dme':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Dme(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
