from .Internal import Instrument


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RsAts1500c:

	def __init__(self, resource_name: str, preset: bool = False):
		"""Initializes new RsAts1500c session. \n
		:param resource_name: VISA resource name, e.g. 'TCPIP::192.168.2.1::200::SOCKET'
		:param preset: Presets the instrument - sends SYST:PRES command"""
		self._io = Instrument.Instrument(resource_name)
		self.driver_version = '1.0.0.2'
		if preset is True:
			self._io.write("SYST:PRES")

	def __str__(self):
		if self._io:
			return f"RsAts1500c session '{self._io.resource_name}'"
		else:
			return f"RsAts1500c with session closed"

	def close(self):
		"""Closes the active RsAts1500c session."""
		self._io.close()

	@property
	def outer(self):
		"""Group of outer axis-related commands"""
		if not hasattr(self, '_outer'):
			from .Implementations.Out import Out
			self._outer = Out(self._io)
		return self._outer

	@property
	def inner(self):
		"""Group of inner axis-related commands"""
		if not hasattr(self, '_inner'):
			from .Implementations.In import In
			self._inner = In(self._io)
		return self._inner

	@property
	def utilities(self):
		"""Utilities - direct write and read methods"""
		if not hasattr(self, '_utilities'):
			from .Implementations.Utilities import Utilities
			self._utilities = Utilities(self._io, self.driver_version)
		return self._utilities
