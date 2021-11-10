from ..Internal import Instrument
from time import sleep
from ..enums import MovementDirection


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Out:
	"""Methods for the outer axis control"""
	def __init__(self, io: Instrument):
		self._io = io

	@property
	def step_movement(self):
		"""Commands for outer step movement"""
		if not hasattr(self, '_stepMovement'):
			
			from .Out_.StepMovement import StepMovement
			self._stepMovement = StepMovement(self._io)
		return self._stepMovement

	@property
	def trigger_output(self):
		"""Commands for outer trigger output control"""
		if not hasattr(self, '_triggerOutput'):
			from .Out_.TriggerOutput import TriggerOutput
			self._triggerOutput = TriggerOutput(self._io)
		return self._triggerOutput

	def set_target_value(self, target: float) -> None:
		"""CONT:OUT:POS:TARG \n
		Sets the target position in degrees for the next movement of the outer axis (turntable).
		Range: -181 to 181"""
		cmd = f'CONT:OUT:POS:TARG {format(target, ".2f")}'
		self._io.write(cmd)

	def set_speed(self, speed: int) -> None:
		"""CONT:OUT:SPE \n
		Sets the speed in degrees per second (°/s).
		Values below 0 or above the maximum limit are merged automatically to the minimum or maximum limit, respectively.
		We recommend a maximum outer speed of 70°/s for stepped measurement and 50°/s for hardware triggered measurement, or lower speeds for heavy DUTs.
		Range: 1 to 120"""
		cmd = f'CONT:OUT:SPE {speed}'
		self._io.write(cmd)

	def set_acceleration(self, acc: int) -> None:
		"""CONT:OUT:ACC \n
		Sets the acceleration in degrees per second squared (°/s2).
		Values below 0 or above the maximum limit are merged automatically to the minimum or maximum limit, respectively. We recommend a maximum outer acceleration of 2000°/s2.
		Range: 1 to 2000"""
		cmd = f'CONT:OUT:ACC {acc}'
		self._io.write(cmd)

	def set_offset(self, offset: float) -> None:
		"""CONT:OUT:OFFS \n
		Configures the offset for the outer axis.
		Range: -184.8 to +184.8"""
		cmd = f'CONT:OUT:OFFS {format(offset, ".2f")}'
		self._io.write(cmd)

	def get_current_position(self) -> float:
		"""SENS:OUT:POS? \n
		Queries the current outer position."""
		return self._io.query_float('SENS:OUT:POS?')

	def get_current_activity(self) -> bool:
		"""SENS:OUT:BUSY? \n
		Queries the current outer activity and returns True, if the axis is moving."""
		return self._io.query_bool('SENS:OUT:BUSY?')

	def start_movement(self) -> None:
		"""CONT:OUT:STAR \n
		Starts the outer movement and stops when it reaches the desired position.
		The method does not wait for the outer to reach the desired position. For that purpose, you can use the method start_and_wait()"""
		self._io.write('CONT:OUT:STAR')

	def stop_movement(self) -> None:
		"""CONT:OUT:STOP \n
		Stops the outer movement."""
		self._io.write('CONT:OUT:STOP')

	def wait_for_movement_finish(self) -> None:
		"""SENS:OUT:BUSY? \n
		Waits until the outer movement activity stops."""
		while self.get_current_activity():
			sleep(0.010)

	def start_cont_movement(self, direction: MovementDirection) -> None:
		"""CONT:OUT:VELO:STAR POS|NEG \n
		Starts the movement of the outer in the desired direction and stop on the limit."""
		assert isinstance(direction, MovementDirection), f'input variable "direction", value {direction} is not of enums.MovementDirection type'
		cmd = 'CONT:OUT:VELO:STAR '
		if direction == MovementDirection.POSitive:
			cmd += 'POS'
		elif direction == MovementDirection.NEGative:
			cmd += 'NEG'
		self._io.write(cmd)
