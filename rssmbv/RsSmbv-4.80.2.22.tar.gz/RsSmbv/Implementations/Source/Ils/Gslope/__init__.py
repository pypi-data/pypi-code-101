from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Gslope:
	"""Gslope commands group definition. 3 total commands, 1 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("gslope", core, parent)

	@property
	def ddm(self):
		"""ddm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ddm'):
			from .Ddm import Ddm
			self._ddm = Ddm(self._core, self._cmd_group)
		return self._ddm

	def preset(self) -> None:
		"""SCPI: [SOURce<HW>]:ILS:GSLope:PRESet \n
		Snippet: driver.source.ils.gslope.preset() \n
		No command help available \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:ILS:GSLope:PRESet')

	def preset_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce<HW>]:ILS:GSLope:PRESet \n
		Snippet: driver.source.ils.gslope.preset_with_opc() \n
		No command help available \n
		Same as preset, but waits for the operation to complete before continuing further. Use the RsSmbv.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:ILS:GSLope:PRESet', opc_timeout_ms)

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:ILS:GSLope:STATe \n
		Snippet: value: bool = driver.source.ils.gslope.get_state() \n
		No command help available \n
			:return: state: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:ILS:GSLope:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:ILS:GSLope:STATe \n
		Snippet: driver.source.ils.gslope.set_state(state = False) \n
		No command help available \n
			:param state: No help available
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:ILS:GSLope:STATe {param}')

	def clone(self) -> 'Gslope':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Gslope(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
