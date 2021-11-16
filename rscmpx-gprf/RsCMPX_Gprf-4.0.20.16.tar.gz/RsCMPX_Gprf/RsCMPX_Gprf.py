from typing import List

from .Internal.Core import Core
from .Internal.InstrumentErrors import RsInstrException
from .Internal.CommandsGroup import CommandsGroup
from .Internal.VisaSession import VisaSession
from . import repcap
from .Internal.RepeatedCapability import RepeatedCapability


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RsCMPX_Gprf:
	"""709 total commands, 17 Sub-groups, 0 group commands"""
	_driver_options = "SupportedInstrModels = CMX500/CMP/CMW, SupportedIdnPatterns = CMX/CMP/CMW, SimulationIdnString = 'Rohde&Schwarz,CMX,100001,4.0.20.0016'"

	def __init__(self, resource_name: str, id_query: bool = True, reset: bool = False, options: str = None, direct_session: object = None):
		"""Initializes new RsCMPX_Gprf session. \n
		Parameter options tokens examples:
			- ``Simulate=True`` - starts the session in simulation mode. Default: ``False``
			- ``SelectVisa=socket`` - uses no VISA implementation for socket connections - you do not need any VISA-C installation
			- ``SelectVisa=rs`` - forces usage of RohdeSchwarz Visa
			- ``SelectVisa=ivi`` - forces usage of National Instruments Visa
			- ``QueryInstrumentStatus = False`` - same as ``driver.utilities.instrument_status_checking = False``. Default: ``True``
			- ``WriteDelay = 20, ReadDelay = 5`` - Introduces delay of 20ms before each write and 5ms before each read. Default: ``0ms`` for both
			- ``OpcWaitMode = OpcQuery`` - mode for all the opc-synchronised write/reads. Other modes: StbPolling, StbPollingSlow, StbPollingSuperSlow. Default: ``StbPolling``
			- ``AddTermCharToWriteBinBLock = True`` - Adds one additional LF to the end of the binary data (some instruments require that). Default: ``False``
			- ``AssureWriteWithTermChar = True`` - Makes sure each command/query is terminated with termination character. Default: Interface dependent
			- ``TerminationCharacter = "\\r"`` - Sets the termination character for reading. Default: ``\\n`` (LineFeed or LF)
			- ``DataChunkSize = 10E3`` - Maximum size of one write/read segment. If transferred data is bigger, it is split to more segments. Default: ``1E6`` bytes
			- ``OpcTimeout = 10000`` - same as driver.utilities.opc_timeout = 10000. Default: ``30000ms``
			- ``VisaTimeout = 5000`` - same as driver.utilities.visa_timeout = 5000. Default: ``10000ms``
			- ``ViClearExeMode = Disabled`` - viClear() execution mode. Default: ``execute_on_all``
			- ``OpcQueryAfterWrite = True`` - same as driver.utilities.opc_query_after_write = True. Default: ``False``
			- ``StbInErrorCheck = False`` - if true, the driver checks errors with *STB? If false, it uses SYST:ERR?. Default: ``True``
			- ``LoggingMode = LoggingMode.On`` - Sets the logging status right from the start. Default: ``Off``
			- ``LoggingName = 'MyDevice'`` - Sets the name to represent the session in the log entries. Default: ``'resource_name'``
		:param resource_name: VISA resource name, e.g. 'TCPIP::192.168.2.1::INSTR'
		:param id_query: if True: the instrument's model name is verified against the models supported by the driver and eventually throws an exception.
		:param reset: Resets the instrument (sends *RST command) and clears its status sybsystem
		:param options: string tokens alternating the driver settings.
		:param direct_session: Another driver object or pyVisa object to reuse the session instead of opening a new session."""
		self._core = Core(resource_name, id_query, reset, RsCMPX_Gprf._driver_options, options, direct_session)
		self._core.driver_version = '4.0.20.0016'
		self._options = options
		self._add_all_global_repcaps()
		self._custom_properties_init()
		self.utilities.default_instrument_setup()
		# noinspection PyTypeChecker
		self._cmd_group = CommandsGroup("ROOT", self._core, None)

	@classmethod
	def from_existing_session(cls, session: object, options: str = None) -> 'RsCMPX_Gprf':
		"""Creates a new RsCMPX_Gprf object with the entered 'session' reused. \n
		:param session: can be an another driver or a direct pyvisa session.
		:param options: string tokens alternating the driver settings."""
		# noinspection PyTypeChecker
		return cls(None, False, False, options, session)

	def __str__(self) -> str:
		if self._core.io:
			return f"RsCMPX_Gprf session '{self._core.io.resource_name}'"
		else:
			return f"RsCMPX_Gprf with session closed"

	@staticmethod
	def assert_minimum_version(min_version: str) -> None:
		"""Asserts that the driver version fulfills the minimum required version you have entered.
		This way you make sure your installed driver is of the entered version or newer."""
		min_version_list = min_version.split('.')
		curr_version_list = '4.0.20.0016'.split('.')
		count_min = len(min_version_list)
		count_curr = len(curr_version_list)
		count = count_min if count_min < count_curr else count_curr
		for i in range(count):
			minimum = int(min_version_list[i])
			curr = int(curr_version_list[i])
			if curr > minimum:
				break
			if curr < minimum:
				raise RsInstrException(f"Assertion for minimum RsCMPX_Gprf version failed. Current version: '4.0.20.0016', minimum required version: '{min_version}'")
				
	@staticmethod
	def list_resources(expression: str = '?*::INSTR', visa_select: str = None) -> List[str]:
		"""Finds all the resources defined by the expression
			- '?*' - matches all the available instruments
			- 'USB::?*' - matches all the USB instruments
			- "TCPIP::192?*' - matches all the LAN instruments with the IP address starting with 192
		:param expression: see the examples in the function
		:param visa_select: optional parameter selecting a specific VISA. Examples: '@ivi', '@rs'
		"""
		rm = VisaSession.get_resource_manager(visa_select)
		resources = rm.list_resources(expression)
		rm.close()
		# noinspection PyTypeChecker
		return resources

	def close(self) -> None:
		"""Closes the active RsCMPX_Gprf session."""
		self._core.io.close()

	def get_session_handle(self) -> object:
		"""Returns the underlying session handle."""
		return self._core.get_session_handle()

	def _add_all_global_repcaps(self) -> None:
		"""Adds all the repcaps defined as global to the instrument's global repcaps dictionary."""
		self._core.io.add_global_repcap('<Instance>', RepeatedCapability("ROOT", 'repcap_instance_get', 'repcap_instance_set', repcap.Instance.Inst1))

	def repcap_instance_get(self) -> repcap.Instance:
		"""Returns Global Repeated capability Instance"""
		return self._core.io.get_global_repcap_value('<Instance>')

	def repcap_instance_set(self, value: repcap.Instance) -> None:
		"""Sets Global Repeated capability Instance
		Default value after init: Instance.Inst1"""
		self._core.io.set_global_repcap_value('<Instance>', value)

	def _custom_properties_init(self):
		"""Adds all the interfaces that are custom for the driver."""
		from .CustomFiles.utilities import Utilities
		self.utilities = Utilities(self._core)
		from .CustomFiles.events import Events
		self.events = Events(self._core)
		from .CustomFiles.reliability import Reliability
		self.reliability = Reliability(self._core)

	@property
	def source(self):
		"""source commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_source'):
			from .Implementations.Source import Source
			self._source = Source(self._core, self._cmd_group)
		return self._source

	@property
	def configure(self):
		"""configure commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_configure'):
			from .Implementations.Configure import Configure
			self._configure = Configure(self._core, self._cmd_group)
		return self._configure

	@property
	def route(self):
		"""route commands group. 9 Sub-classes, 0 commands."""
		if not hasattr(self, '_route'):
			from .Implementations.Route import Route
			self._route = Route(self._core, self._cmd_group)
		return self._route

	@property
	def trigger(self):
		"""trigger commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_trigger'):
			from .Implementations.Trigger import Trigger
			self._trigger = Trigger(self._core, self._cmd_group)
		return self._trigger

	@property
	def diagnostic(self):
		"""diagnostic commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_diagnostic'):
			from .Implementations.Diagnostic import Diagnostic
			self._diagnostic = Diagnostic(self._core, self._cmd_group)
		return self._diagnostic

	@property
	def gprf(self):
		"""gprf commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_gprf'):
			from .Implementations.Gprf import Gprf
			self._gprf = Gprf(self._core, self._cmd_group)
		return self._gprf

	@property
	def results(self):
		"""results commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_results'):
			from .Implementations.Results import Results
			self._results = Results(self._core, self._cmd_group)
		return self._results

	@property
	def calibration(self):
		"""calibration commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_calibration'):
			from .Implementations.Calibration import Calibration
			self._calibration = Calibration(self._core, self._cmd_group)
		return self._calibration

	@property
	def initiate(self):
		"""initiate commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_initiate'):
			from .Implementations.Initiate import Initiate
			self._initiate = Initiate(self._core, self._cmd_group)
		return self._initiate

	@property
	def sense(self):
		"""sense commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_sense'):
			from .Implementations.Sense import Sense
			self._sense = Sense(self._core, self._cmd_group)
		return self._sense

	@property
	def catalog(self):
		"""catalog commands group. 11 Sub-classes, 0 commands."""
		if not hasattr(self, '_catalog'):
			from .Implementations.Catalog import Catalog
			self._catalog = Catalog(self._core, self._cmd_group)
		return self._catalog

	@property
	def create(self):
		"""create commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_create'):
			from .Implementations.Create import Create
			self._create = Create(self._core, self._cmd_group)
		return self._create

	@property
	def tenvironment(self):
		"""tenvironment commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_tenvironment'):
			from .Implementations.Tenvironment import Tenvironment
			self._tenvironment = Tenvironment(self._core, self._cmd_group)
		return self._tenvironment

	@property
	def add(self):
		"""add commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_add'):
			from .Implementations.Add import Add
			self._add = Add(self._core, self._cmd_group)
		return self._add

	@property
	def remove(self):
		"""remove commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_remove'):
			from .Implementations.Remove import Remove
			self._remove = Remove(self._core, self._cmd_group)
		return self._remove

	@property
	def modify(self):
		"""modify commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_modify'):
			from .Implementations.Modify import Modify
			self._modify = Modify(self._core, self._cmd_group)
		return self._modify

	@property
	def system(self):
		"""system commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_system'):
			from .Implementations.System import System
			self._system = System(self._core, self._cmd_group)
		return self._system

	def clone(self) -> 'RsCMPX_Gprf':
		"""Creates a deep copy of the RsCMPX_Gprf object. Also copies:
			- All the existing Global repeated capability values
			- All the default group repeated capabilities setting \n
		Does not check the *IDN? response, and does not perform Reset.
		After cloning, you can set all the repeated capabilities settings independentely from the original group.
		Calling close() on the new object does not close the original VISA session"""
		cloned = RsCMPX_Gprf.from_existing_session(self.get_session_handle(), self._options)
		self._cmd_group.synchronize_repcaps(cloned)
		cloned.repcap_instance_set(self.repcap_instance_get())
		return cloned

	def restore_all_repcaps_to_default(self) -> None:
		"""Sets all the Group and Global repcaps to their initial values"""
		self._cmd_group.restore_repcaps()
		self.repcap_instance_set(repcap.Instance.Inst1)
