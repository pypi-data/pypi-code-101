from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Clipping:
	"""Clipping commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("clipping", core, parent)

	def get_cfactor(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:MCARrier:CLIPping:CFACtor \n
		Snippet: value: float = driver.source.bb.arbitrary.mcarrier.clipping.get_cfactor() \n
		Sets the value of the desired crest factor, if baseband clipping is enabled (BB:ARB:MCAR:CLIP:STAT ON) . A Target Crest
		Factor above the crest factor of the unclipped multicarrier signal has no effect. \n
			:return: cfactor: float Range: -50 to 50, Unit: dB
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ARBitrary:MCARrier:CLIPping:CFACtor?')
		return Conversions.str_to_float(response)

	def set_cfactor(self, cfactor: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:MCARrier:CLIPping:CFACtor \n
		Snippet: driver.source.bb.arbitrary.mcarrier.clipping.set_cfactor(cfactor = 1.0) \n
		Sets the value of the desired crest factor, if baseband clipping is enabled (BB:ARB:MCAR:CLIP:STAT ON) . A Target Crest
		Factor above the crest factor of the unclipped multicarrier signal has no effect. \n
			:param cfactor: float Range: -50 to 50, Unit: dB
		"""
		param = Conversions.decimal_value_to_str(cfactor)
		self._core.io.write(f'SOURce<HwInstance>:BB:ARBitrary:MCARrier:CLIPping:CFACtor {param}')

	def get_cutoff(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:MCARrier:CLIPping:CUToff \n
		Snippet: value: float = driver.source.bb.arbitrary.mcarrier.clipping.get_cutoff() \n
		Sets the cut off frequency of the final lowpass filter, if baseband clipping is enabled (BB:ARB:MCAR:CLIP:STAT ON) . When
		the cut off frequency is set as half of the output sample rate, a final lowpass filter improves the spectrum of the
		clipped multicarrier signal, but may also increase the resulting crest factor. \n
			:return: cutoff: float Range: 0 to 120E6, Unit: MHz
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ARBitrary:MCARrier:CLIPping:CUToff?')
		return Conversions.str_to_float(response)

	def set_cutoff(self, cutoff: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:MCARrier:CLIPping:CUToff \n
		Snippet: driver.source.bb.arbitrary.mcarrier.clipping.set_cutoff(cutoff = 1.0) \n
		Sets the cut off frequency of the final lowpass filter, if baseband clipping is enabled (BB:ARB:MCAR:CLIP:STAT ON) . When
		the cut off frequency is set as half of the output sample rate, a final lowpass filter improves the spectrum of the
		clipped multicarrier signal, but may also increase the resulting crest factor. \n
			:param cutoff: float Range: 0 to 120E6, Unit: MHz
		"""
		param = Conversions.decimal_value_to_str(cutoff)
		self._core.io.write(f'SOURce<HwInstance>:BB:ARBitrary:MCARrier:CLIPping:CUToff {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:MCARrier:CLIPping:[STATe] \n
		Snippet: value: bool = driver.source.bb.arbitrary.mcarrier.clipping.get_state() \n
		Switches baseband clipping on and off. Clipping reduces the peak power of the resulting multi carrier signal according to
		the value set with the command BB:ARB:MCAR:CLIP:CFAC. The resulting clipped peak power is defined by sum of the the RMS
		level of the unclipped multi carrier signal and the input parameter Target Crest Factor. Note that clipping reduces also
		the RMS level. Hence the resulting crest factor of the clipped signal is slightly above the Target Crest Factor. In order
		to get the unclipped parts of the clipped multicarrier signal matched with the unclipped multicarrier signal, the RF
		output power should be reduced by the difference between resulting crest factor and Target Crest Factor. \n
			:return: state: 0| 1| OFF| ON
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:ARBitrary:MCARrier:CLIPping:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:ARBitrary:MCARrier:CLIPping:[STATe] \n
		Snippet: driver.source.bb.arbitrary.mcarrier.clipping.set_state(state = False) \n
		Switches baseband clipping on and off. Clipping reduces the peak power of the resulting multi carrier signal according to
		the value set with the command BB:ARB:MCAR:CLIP:CFAC. The resulting clipped peak power is defined by sum of the the RMS
		level of the unclipped multi carrier signal and the input parameter Target Crest Factor. Note that clipping reduces also
		the RMS level. Hence the resulting crest factor of the clipped signal is slightly above the Target Crest Factor. In order
		to get the unclipped parts of the clipped multicarrier signal matched with the unclipped multicarrier signal, the RF
		output power should be reduced by the difference between resulting crest factor and Target Crest Factor. \n
			:param state: 0| 1| OFF| ON
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SOURce<HwInstance>:BB:ARBitrary:MCARrier:CLIPping:STATe {param}')
