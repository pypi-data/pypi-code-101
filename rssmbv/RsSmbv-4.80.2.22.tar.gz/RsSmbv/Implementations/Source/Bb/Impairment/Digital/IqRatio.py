from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IqRatio:
	"""IqRatio commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("iqRatio", core, parent)

	def get_magnitude(self) -> float:
		"""SCPI: [SOURce]:BB:IMPairment:DIGital:IQRatio:[MAGNitude] \n
		Snippet: value: float = driver.source.bb.impairment.digital.iqRatio.get_magnitude() \n
		Sets the ratio of I modulation to Q modulation (amplification imbalance) of the corresponding digital channel.
		Value range
			Table Header: Impairments / Min [dB] / Max [dB] / Resolution \n
			- Digital / 4 / 4 / 0.0001
			- Analog / 1 / 1 / 0.0001 \n
			:return: ipartq_ratio: No help available
		"""
		response = self._core.io.query_str('SOURce:BB:IMPairment:DIGital:IQRatio:MAGNitude?')
		return Conversions.str_to_float(response)

	def set_magnitude(self, ipartq_ratio: float) -> None:
		"""SCPI: [SOURce]:BB:IMPairment:DIGital:IQRatio:[MAGNitude] \n
		Snippet: driver.source.bb.impairment.digital.iqRatio.set_magnitude(ipartq_ratio = 1.0) \n
		Sets the ratio of I modulation to Q modulation (amplification imbalance) of the corresponding digital channel.
		Value range
			Table Header: Impairments / Min [dB] / Max [dB] / Resolution \n
			- Digital / 4 / 4 / 0.0001
			- Analog / 1 / 1 / 0.0001 \n
			:param ipartq_ratio: float The setting value can be either in dB or %. An input in percent is rounded to the closest valid value in dB. Range: -4 to 4, Unit: dB | PCT (setting command) / dB (result value)
		"""
		param = Conversions.decimal_value_to_str(ipartq_ratio)
		self._core.io.write(f'SOURce:BB:IMPairment:DIGital:IQRatio:MAGNitude {param}')
