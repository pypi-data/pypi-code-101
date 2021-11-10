from ..Internal import Instrument
from time import sleep
from ..enums import MovementDirection


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class In:
	"""Methods for the inner axis control"""

	def __init__(self, io: Instrument):
		self._io = io

	@property
	def step_movement(self):
		"""Commands for inner step movement"""
		if not hasattr(self, '_stepMovement'):
			from .In_.StepMovement import StepMovement
			self._stepMovement = StepMovement(self._io)
		return self._stepMovement

	@property
	def trigger_output(self):
		"""Commands for inner trigger output control"""
		if not hasattr(self, '_triggerOutput'):
			from .In_.TriggerOutput import TriggerOutput
			self._triggerOutput = TriggerOutput(self._io)
		return self._triggerOutput

	def set_target_value(self, target: float) -> None:
		"""CONT:IN:POS:TARG \n
		Sets the target position in degrees for the next movement of the inner axis (turntable).
		Range: -45 to +45"""
		cmd = f'CONT:IN:POS:TARG {format(target, ".2f")}'
		self._io.write(cmd)

	def set_speed(self, speed: int) -> None:
		"""CONT:IN:SPE \n
		Sets the speed in degrees per second (°/s). Values below 0 or above the maximum limit are merged automatically to the minimum or maximum limit, respectively. We recommend a maximum inner speed of 20°/s2.
		Range: 0.1 to 15"""
		cmd = f'CONT:IN:SPE {speed}'
		self._io.write(cmd)

	def set_acceleration(self, acc: int) -> None:
		"""CONT:IN:ACC \n
		Sets or queries the acceleration of the inner axis. Sets the acceleration in degrees per second squared (°/s2).
		Values below 0 or above the maximum limit are merged automatically to the minimum or maximum limit, respectively. We recommend a maximum inner acceleration of 400°/s2.
		Range: 1 to 15000"""
		cmd = f'CONT:IN:ACC {acc}'
		self._io.write(cmd)

	def set_offset(self, offset: float) -> None:
		"""CONT:IN:OFFS \n
		Configures the offset for the inner axis.
		Range: -46 to +46"""
		cmd = f'CONT:IN:OFFS {format(offset, ".2f")}'
		self._io.write(cmd)

	def get_current_position(self) -> float:
		"""SENS:IN:POS? \n
		Queries the current inner position."""
		return self._io.query_float('SENS:IN:POS?')

	def get_current_activity(self) -> bool:
		"""SENS:IN:BUSY? \n
		Queries the current inner activity and returns True, if the axis is moving."""
		return self._io.query_bool('SENS:IN:BUSY?')

	def start_movement(self) -> None:
		"""CONT:IN:STAR \n
		Starts the inner movement and stops when it reaches the desired position.
		The method does not wait for the inner to reach the desired position. For that purpose, you can use the method start_and_wait()"""
		self._io.write('CONT:IN:STAR')

	def stop_movement(self) -> None:
		"""CONT:IN:STOP \n
		Stops the inner movement."""
		self._io.write('CONT:IN:STOP')

	def wait_for_movement_finish(self) -> None:
		"""SENS:IN:BUSY? \n
		Waits until the inner movement activity stops."""
		while self.get_current_activity():
			sleep(0.010)

	def start_cont_movement(self, direction: MovementDirection) -> None:
		"""CONT:IN:VELO:STAR POS|NEG \n
		Starts the movement of the inner axis in the desired direction and stop on the limit."""
		assert isinstance(direction, MovementDirection), f'input variable "direction", value {direction} is not of enums.MovementDirection type'
		cmd = 'CONT:IN:VELO:STAR '
		if direction == MovementDirection.POSitive:
			cmd += 'POS'
		elif direction == MovementDirection.NEGative:
			cmd += 'NEG'
		self._io.write(cmd)

	def start_referencing(self) -> None:
		"""CONT:IN:REF:STAR \n
		Starts a 0-position referencing of the inner axis."""
		self._io.write('CONT:IN:REF:STAR')

	def wait_for_referencing_finish(self) -> None:
		"""SYST:ERR? \n
		Waits until the 0-position referencing of the inner axis finishes."""
		while True:
			code = self._io.query_int('SYST:ERR?')
			if code != -995:
				break
			sleep(0.025)



