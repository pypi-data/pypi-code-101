from ...enums import MovementDirection
from ...Internal import Instrument


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StepMovement:
	"""Step movement of the outer axis"""
	def __init__(self, io: Instrument):
		self._io = io

	def set_size(self, step: float) -> None:
		"""CONT:OUT:POS:STEP \n
		Sets the single-step size. Range: 0.1 .. 360."""
		cmd = f'CONT:OUT:POS:STEP {format(step, ".2f")}'
		self._io.write(cmd)

	def set_direction(self, direction: MovementDirection) -> None:
		"""CONT:OUT:STEP:DIR POS|NEG \n
		Configures the single-step movement for the outer axis."""
		assert isinstance(direction, MovementDirection), f'input variable "direction", value {direction} is not of enums.MovementDirection type'
		cmd = 'CONT:OUT:STEP:DIR '
		if direction == MovementDirection.POSitive:
			cmd += 'POS'
		elif direction == MovementDirection.NEGative:
			cmd += 'NEG'
		self._io.write(cmd)

	def start(self) -> None:
		"""CONT:OUT:STEP:STAR \n
		Moves the outer axis by a single step."""
		self._io.write('CONT:OUT:STEP:STAR')
