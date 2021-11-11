from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Model:
	"""Model commands group definition. 11 total commands, 3 Sub-groups, 6 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("model", core, parent)

	@property
	def fname(self):
		"""fname commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fname'):
			from .Fname import Fname
			self._fname = Fname(self._core, self._cmd_group)
		return self._fname

	@property
	def data(self):
		"""data commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_data'):
			from .Data import Data
			self._data = Data(self._core, self._cmd_group)
		return self._data

	@property
	def current(self):
		"""current commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_current'):
			from .Current import Current
			self._current = Current(self._core, self._cmd_group)
		return self._current

	def save(self) -> None:
		"""SCPI: BATTery:MODel:SAVE \n
		Snippet: driver.battery.model.save() \n
		Saves the current battery model to a file \n
		"""
		self._core.io.write(f'BATTery:MODel:SAVE')

	def save_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: BATTery:MODel:SAVE \n
		Snippet: driver.battery.model.save_with_opc() \n
		Saves the current battery model to a file \n
		Same as save, but waits for the operation to complete before continuing further. Use the RsNgx.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'BATTery:MODel:SAVE', opc_timeout_ms)

	def load(self) -> None:
		"""SCPI: BATTery:MODel:LOAD \n
		Snippet: driver.battery.model.load() \n
		Loads a battery model for editing. \n
		"""
		self._core.io.write(f'BATTery:MODel:LOAD')

	def load_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: BATTery:MODel:LOAD \n
		Snippet: driver.battery.model.load_with_opc() \n
		Loads a battery model for editing. \n
		Same as load, but waits for the operation to complete before continuing further. Use the RsNgx.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'BATTery:MODel:LOAD', opc_timeout_ms)

	def set_transfer(self, arg_0: int) -> None:
		"""SCPI: BATTery:MODel:TRANsfer \n
		Snippet: driver.battery.model.set_transfer(arg_0 = 1) \n
		Transfers the loaded battery model into the channel. \n
			:param arg_0: 1 | 2
		"""
		param = Conversions.decimal_value_to_str(arg_0)
		self._core.io.write(f'BATTery:MODel:TRANsfer {param}')

	def get_capacity(self) -> float:
		"""SCPI: BATTery:MODel:CAPacity \n
		Snippet: value: float = driver.battery.model.get_capacity() \n
		Sets or queries the battery model capacity. \n
			:return: arg_0: Sets the battery model capacity.
		"""
		response = self._core.io.query_str('BATTery:MODel:CAPacity?')
		return Conversions.str_to_float(response)

	def set_capacity(self, arg_0: float) -> None:
		"""SCPI: BATTery:MODel:CAPacity \n
		Snippet: driver.battery.model.set_capacity(arg_0 = 1.0) \n
		Sets or queries the battery model capacity. \n
			:param arg_0: Sets the battery model capacity.
		"""
		param = Conversions.decimal_value_to_str(arg_0)
		self._core.io.write(f'BATTery:MODel:CAPacity {param}')

	def get_isoc(self) -> float:
		"""SCPI: BATTery:MODel:ISOC \n
		Snippet: value: float = driver.battery.model.get_isoc() \n
		Sets or queries the initial state of charge (SoC) of the battery model. \n
			:return: arg_0: No help available
		"""
		response = self._core.io.query_str('BATTery:MODel:ISOC?')
		return Conversions.str_to_float(response)

	def set_isoc(self, arg_0: float) -> None:
		"""SCPI: BATTery:MODel:ISOC \n
		Snippet: driver.battery.model.set_isoc(arg_0 = 1.0) \n
		Sets or queries the initial state of charge (SoC) of the battery model. \n
			:param arg_0: Initial state of charge (SoC) for the battery model.
		"""
		param = Conversions.decimal_value_to_str(arg_0)
		self._core.io.write(f'BATTery:MODel:ISOC {param}')

	def clear(self) -> None:
		"""SCPI: BATTery:MODel:CLEar \n
		Snippet: driver.battery.model.clear() \n
		Clears the current battery model. \n
		"""
		self._core.io.write(f'BATTery:MODel:CLEar')

	def clear_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: BATTery:MODel:CLEar \n
		Snippet: driver.battery.model.clear_with_opc() \n
		Clears the current battery model. \n
		Same as clear, but waits for the operation to complete before continuing further. Use the RsNgx.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'BATTery:MODel:CLEar', opc_timeout_ms)
