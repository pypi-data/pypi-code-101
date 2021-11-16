from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Antenna:
	"""Antenna commands group definition. 8 total commands, 1 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("antenna", core, parent)

	@property
	def tchain(self):
		"""tchain commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_tchain'):
			from .Tchain import Tchain
			self._tchain = Tchain(self._core, self._cmd_group)
		return self._tchain

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.WlannTxAnt:
		"""SCPI: [SOURce<HW>]:BB:WLNN:ANTenna:MODE \n
		Snippet: value: enums.WlannTxAnt = driver.source.bb.wlnn.antenna.get_mode() \n
		The command selects the number of transmit antennas to be used. \n
			:return: mode: A1| A2| A3| A4| A5| A6| A7| A8
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:WLNN:ANTenna:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.WlannTxAnt)

	def set_mode(self, mode: enums.WlannTxAnt) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLNN:ANTenna:MODE \n
		Snippet: driver.source.bb.wlnn.antenna.set_mode(mode = enums.WlannTxAnt.A1) \n
		The command selects the number of transmit antennas to be used. \n
			:param mode: A1| A2| A3| A4| A5| A6| A7| A8
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.WlannTxAnt)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLNN:ANTenna:MODE {param}')

	# noinspection PyTypeChecker
	def get_system(self) -> enums.CoordMapMode:
		"""SCPI: [SOURce<HW>]:BB:WLNN:ANTenna:SYSTem \n
		Snippet: value: enums.CoordMapMode = driver.source.bb.wlnn.antenna.get_system() \n
		Selects the coordinate system of the transmission chain matrix. \n
			:return: system: CARTesian| CYLindrical
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:WLNN:ANTenna:SYSTem?')
		return Conversions.str_to_scalar_enum(response, enums.CoordMapMode)

	def set_system(self, system: enums.CoordMapMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:WLNN:ANTenna:SYSTem \n
		Snippet: driver.source.bb.wlnn.antenna.set_system(system = enums.CoordMapMode.CARTesian) \n
		Selects the coordinate system of the transmission chain matrix. \n
			:param system: CARTesian| CYLindrical
		"""
		param = Conversions.enum_scalar_to_str(system, enums.CoordMapMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:WLNN:ANTenna:SYSTem {param}')

	def clone(self) -> 'Antenna':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Antenna(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
