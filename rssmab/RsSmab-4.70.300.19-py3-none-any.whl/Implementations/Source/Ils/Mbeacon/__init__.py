from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mbeacon:
	"""Mbeacon commands group definition. 17 total commands, 3 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mbeacon", core, parent)

	@property
	def comid(self):
		"""comid commands group. 1 Sub-classes, 9 commands."""
		if not hasattr(self, '_comid'):
			from .Comid import Comid
			self._comid = Comid(self._core, self._cmd_group)
		return self._comid

	@property
	def frequency(self):
		"""frequency commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import Frequency
			self._frequency = Frequency(self._core, self._cmd_group)
		return self._frequency

	@property
	def marker(self):
		"""marker commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_marker'):
			from .Marker import Marker
			self._marker = Marker(self._core, self._cmd_group)
		return self._marker

	def preset(self) -> None:
		"""SCPI: [SOURce<HW>]:[ILS]:MBEacon:PRESet \n
		Snippet: driver.source.ils.mbeacon.preset() \n
		Sets the parameters of the ILS marker beacons component to their default values (*RST values specified for the commands) .
		For other ILS preset commands, see ILS:PRESet. \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:ILS:MBEacon:PRESet')

	def preset_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SOURce<HW>]:[ILS]:MBEacon:PRESet \n
		Snippet: driver.source.ils.mbeacon.preset_with_opc() \n
		Sets the parameters of the ILS marker beacons component to their default values (*RST values specified for the commands) .
		For other ILS preset commands, see ILS:PRESet. \n
		Same as preset, but waits for the operation to complete before continuing further. Use the RsSmab.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:ILS:MBEacon:PRESet', opc_timeout_ms)

	def clone(self) -> 'Mbeacon':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Mbeacon(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
