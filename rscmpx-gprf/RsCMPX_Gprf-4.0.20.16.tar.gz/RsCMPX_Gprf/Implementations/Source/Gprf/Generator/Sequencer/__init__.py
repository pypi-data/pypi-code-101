from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sequencer:
	"""Sequencer commands group definition. 94 total commands, 9 Sub-groups, 6 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sequencer", core, parent)

	@property
	def apool(self):
		"""apool commands group. 13 Sub-classes, 8 commands."""
		if not hasattr(self, '_apool'):
			from .Apool import Apool
			self._apool = Apool(self._core, self._cmd_group)
		return self._apool

	@property
	def reliability(self):
		"""reliability commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_reliability'):
			from .Reliability import Reliability
			self._reliability = Reliability(self._core, self._cmd_group)
		return self._reliability

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	@property
	def listPy(self):
		"""listPy commands group. 12 Sub-classes, 3 commands."""
		if not hasattr(self, '_listPy'):
			from .ListPy import ListPy
			self._listPy = ListPy(self._core, self._cmd_group)
		return self._listPy

	@property
	def marker(self):
		"""marker commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_marker'):
			from .Marker import Marker
			self._marker = Marker(self._core, self._cmd_group)
		return self._marker

	@property
	def wmarker(self):
		"""wmarker commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_wmarker'):
			from .Wmarker import Wmarker
			self._wmarker = Wmarker(self._core, self._cmd_group)
		return self._wmarker

	@property
	def rmarker(self):
		"""rmarker commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rmarker'):
			from .Rmarker import Rmarker
			self._rmarker = Rmarker(self._core, self._cmd_group)
		return self._rmarker

	@property
	def dtone(self):
		"""dtone commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_dtone'):
			from .Dtone import Dtone
			self._dtone = Dtone(self._core, self._cmd_group)
		return self._dtone

	@property
	def tdd(self):
		"""tdd commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tdd'):
			from .Tdd import Tdd
			self._tdd = Tdd(self._core, self._cmd_group)
		return self._tdd

	# noinspection PyTypeChecker
	def get_repetition(self) -> enums.RepeatMode:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:REPetition \n
		Snippet: value: enums.RepeatMode = driver.source.gprf.generator.sequencer.get_repetition() \n
		Defines how often the sequencer list is processed. \n
			:return: repetition: CONTinuous: Unlimited, cyclic processing SINGle: Single execution
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:SEQuencer:REPetition?')
		return Conversions.str_to_scalar_enum(response, enums.RepeatMode)

	def set_repetition(self, repetition: enums.RepeatMode) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:REPetition \n
		Snippet: driver.source.gprf.generator.sequencer.set_repetition(repetition = enums.RepeatMode.CONTinuous) \n
		Defines how often the sequencer list is processed. \n
			:param repetition: CONTinuous: Unlimited, cyclic processing SINGle: Single execution
		"""
		param = Conversions.enum_scalar_to_str(repetition, enums.RepeatMode)
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:SEQuencer:REPetition {param}')

	def get_nrepetition(self) -> int:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:NREPetition \n
		Snippet: value: int = driver.source.gprf.generator.sequencer.get_nrepetition() \n
		No command help available \n
			:return: num_of_rep: No help available
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:SEQuencer:NREPetition?')
		return Conversions.str_to_int(response)

	def set_nrepetition(self, num_of_rep: int) -> None:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:NREPetition \n
		Snippet: driver.source.gprf.generator.sequencer.set_nrepetition(num_of_rep = 1) \n
		No command help available \n
			:param num_of_rep: No help available
		"""
		param = Conversions.decimal_value_to_str(num_of_rep)
		self._core.io.write(f'SOURce:GPRF:GENerator<Instance>:SEQuencer:NREPetition {param}')

	def get_rcount(self) -> int:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:RCOunt \n
		Snippet: value: int = driver.source.gprf.generator.sequencer.get_rcount() \n
		No command help available \n
			:return: rep_count: No help available
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:SEQuencer:RCOunt?')
		return Conversions.str_to_int(response)

	def get_signal(self) -> bool:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:SIGNal \n
		Snippet: value: bool = driver.source.gprf.generator.sequencer.get_signal() \n
		Queries whether a signal is generated or not. \n
			:return: signal: No help available
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:SEQuencer:SIGNal?')
		return Conversions.str_to_bool(response)

	def get_centry(self) -> int:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:CENTry \n
		Snippet: value: int = driver.source.gprf.generator.sequencer.get_centry() \n
		Queries the index of the processed entry. The remote query takes between 2 ms and 3 ms, which introduces an uncertainty
		to the results. \n
			:return: current_entry: If the sequencer is not running, NAV is returned.
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:SEQuencer:CENTry?')
		return Conversions.str_to_int(response)

	def get_uoptions(self) -> str:
		"""SCPI: SOURce:GPRF:GENerator<Instance>:SEQuencer:UOPTions \n
		Snippet: value: str = driver.source.gprf.generator.sequencer.get_uoptions() \n
		Queries a list of the used software options. \n
			:return: used_options: The string contains a comma-separated list of options. If the sequencer is OFF, NAV is returned. If the sequencer is not OFF but no options are used by the sequencer list, 'None' is returned.
		"""
		response = self._core.io.query_str('SOURce:GPRF:GENerator<Instance>:SEQuencer:UOPTions?')
		return trim_str_response(response)

	def clone(self) -> 'Sequencer':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Sequencer(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
