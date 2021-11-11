from typing import List

from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Log:
	"""Log commands group definition. 11 total commands, 7 Sub-groups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("log", core, parent)

	@property
	def channel(self):
		"""channel commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_channel'):
			from .Channel import Channel
			self._channel = Channel(self._core, self._cmd_group)
		return self._channel

	@property
	def mode(self):
		"""mode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mode'):
			from .Mode import Mode
			self._mode = Mode(self._core, self._cmd_group)
		return self._mode

	@property
	def count(self):
		"""count commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_count'):
			from .Count import Count
			self._count = Count(self._core, self._cmd_group)
		return self._count

	@property
	def duration(self):
		"""duration commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_duration'):
			from .Duration import Duration
			self._duration = Duration(self._core, self._cmd_group)
		return self._duration

	@property
	def interval(self):
		"""interval commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_interval'):
			from .Interval import Interval
			self._interval = Interval(self._core, self._cmd_group)
		return self._interval

	@property
	def fname(self):
		"""fname commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fname'):
			from .Fname import Fname
			self._fname = Fname(self._core, self._cmd_group)
		return self._fname

	@property
	def stime(self):
		"""stime commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_stime'):
			from .Stime import Stime
			self._stime = Stime(self._core, self._cmd_group)
		return self._stime

	# noinspection PyTypeChecker
	def get_location(self) -> enums.Filename:
		"""SCPI: LOG:LOCation \n
		Snippet: value: enums.Filename = driver.log.get_location() \n
		Sets or queries the logging location. \n
			:return: file_location: No help available
		"""
		response = self._core.io.query_str('LOG:LOCation?')
		return Conversions.str_to_scalar_enum(response, enums.Filename)

	def set_location(self, file_location: enums.Filename) -> None:
		"""SCPI: LOG:LOCation \n
		Snippet: driver.log.set_location(file_location = enums.Filename.DEF) \n
		Sets or queries the logging location. \n
			:param file_location: No help available
		"""
		param = Conversions.enum_scalar_to_str(file_location, enums.Filename)
		self._core.io.write(f'LOG:LOCation {param}')

	def get_data(self) -> List[float]:
		"""SCPI: LOG:DATA \n
		Snippet: value: List[float] = driver.log.get_data() \n
		Returns 12 sets of latest logging data with minimum logging interval (8 ms) . Depending on the models, the data is
		returned in the following format for a 2-channel models: <Ch1_voltage>, <Ch1_current>,<Ch1_power>,<Ch2_voltage>,
		<Ch2_current>,<Ch2_power>, <Ch1_voltage>, <Ch1_current>,<Ch1_power>, <Ch2_voltage>, <Ch2_current>,<Ch2_power>... \n
			:return: result: No help available
		"""
		response = self._core.io.query_bin_or_ascii_float_list('LOG:DATA?')
		return response

	def get_triggered(self) -> int or bool:
		"""SCPI: LOG:TRIGgered \n
		Snippet: value: int or bool = driver.log.get_triggered() \n
		Sets or queries the state for manual trigger logging function. \n
			:return: arg_0: (integer or boolean) No help available
		"""
		response = self._core.io.query_str('LOG:TRIGgered?')
		return Conversions.str_to_int_or_bool(response)

	def set_triggered(self, arg_0: int or bool) -> None:
		"""SCPI: LOG:TRIGgered \n
		Snippet: driver.log.set_triggered(arg_0 = 1) \n
		Sets or queries the state for manual trigger logging function. \n
			:param arg_0: (integer or boolean) 0 Manual trigger function is disabled. 1 Manual trigger function is enabled.
		"""
		param = Conversions.decimal_or_bool_value_to_str(arg_0)
		self._core.io.write(f'LOG:TRIGgered {param}')

	def get_state(self) -> bool:
		"""SCPI: LOG[:STATe] \n
		Snippet: value: bool = driver.log.get_state() \n
		Sets or queries the data logging state. \n
			:return: arg_0: No help available
		"""
		response = self._core.io.query_str('LOG:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, arg_0: bool) -> None:
		"""SCPI: LOG[:STATe] \n
		Snippet: driver.log.set_state(arg_0 = False) \n
		Sets or queries the data logging state. \n
			:param arg_0:
				- 1: Data logging function is enabled.
				- 0: Data logging function is disabled."""
		param = Conversions.bool_to_str(arg_0)
		self._core.io.write(f'LOG:STATe {param}')
