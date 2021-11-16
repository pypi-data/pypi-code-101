from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Level:
	"""Level commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("level", core, parent)

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.ArbWaveSegmPowMode:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:WSEGment:CONFigure:LEVel:[MODE] \n
		Snippet: value: enums.ArbWaveSegmPowMode = driver.source.bb.arbitrary.wsegment.configure.level.get_mode() \n
		This command selects the level mode for the multi segment waveform. \n
			:return: mode: UNCHanged| ERMS UNCHanged The segments are output exactly as defined in the files. ERMS The segments are output so that all segments have the same rms value.
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ARBitrary:WSEGment:CONFigure:LEVel:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.ArbWaveSegmPowMode)

	def set_mode(self, mode: enums.ArbWaveSegmPowMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:WSEGment:CONFigure:LEVel:[MODE] \n
		Snippet: driver.source.bb.arbitrary.wsegment.configure.level.set_mode(mode = enums.ArbWaveSegmPowMode.ERMS) \n
		This command selects the level mode for the multi segment waveform. \n
			:param mode: UNCHanged| ERMS UNCHanged The segments are output exactly as defined in the files. ERMS The segments are output so that all segments have the same rms value.
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.ArbWaveSegmPowMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:ARBitrary:WSEGment:CONFigure:LEVel:MODE {param}')
