from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cqpsk:
	"""Cqpsk commands group definition. 5 total commands, 0 Sub-groups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cqpsk", core, parent)

	# noinspection PyTypeChecker
	def get_ilength(self) -> enums.ImpulseLength:
		"""SCPI: SOURce:AFRF:GENerator<Instance>:PTFive:CQPSk:ILENgth \n
		Snippet: value: enums.ImpulseLength = driver.source.afRf.generator.ptFive.cqpsk.get_ilength() \n
		Queries the impulse length of the filter used for pulse shaping for P25 with CQPSK modulation. \n
			:return: impulse_length: T2
		"""
		response = self._core.io.query_str('SOURce:AFRF:GENerator<Instance>:PTFive:CQPSk:ILENgth?')
		return Conversions.str_to_scalar_enum(response, enums.ImpulseLength)

	def get_standard_dev(self) -> List[float]:
		"""SCPI: SOURce:AFRF:GENerator<Instance>:PTFive:CQPSk:SDEViation \n
		Snippet: value: List[float] = driver.source.afRf.generator.ptFive.cqpsk.get_standard_dev() \n
		Queries the phase changes used for CQPSK modulation, for P25. \n
			:return: sdeviation: List of four phase changes, for the symbols 01, 00, 10, 11. Range: -180 deg to 180 deg, Unit: deg
		"""
		response = self._core.io.query_bin_or_ascii_float_list('SOURce:AFRF:GENerator<Instance>:PTFive:CQPSk:SDEViation?')
		return response

	def get_ro_factor(self) -> float:
		"""SCPI: SOURce:AFRF:GENerator<Instance>:PTFive:CQPSk:ROFactor \n
		Snippet: value: float = driver.source.afRf.generator.ptFive.cqpsk.get_ro_factor() \n
		Queries the roll-off factor of the filter used for pulse shaping for P25 with CQPSK modulation. \n
			:return: ro_factor: Range: 0.2 to 0.2
		"""
		response = self._core.io.query_str('SOURce:AFRF:GENerator<Instance>:PTFive:CQPSk:ROFactor?')
		return Conversions.str_to_float(response)

	# noinspection PyTypeChecker
	def get_filter_py(self) -> enums.PtFiveFilter:
		"""SCPI: SOURce:AFRF:GENerator<Instance>:PTFive:CQPSk:FILTer \n
		Snippet: value: enums.PtFiveFilter = driver.source.afRf.generator.ptFive.cqpsk.get_filter_py() \n
		Queries the filter type used for pulse shaping for P25 with CQPSK modulation. \n
			:return: filter_py: RRC
		"""
		response = self._core.io.query_str('SOURce:AFRF:GENerator<Instance>:PTFive:CQPSk:FILTer?')
		return Conversions.str_to_scalar_enum(response, enums.PtFiveFilter)

	def get_symbol_rate(self) -> float:
		"""SCPI: SOURce:AFRF:GENerator<Instance>:PTFive:CQPSk:SRATe \n
		Snippet: value: float = driver.source.afRf.generator.ptFive.cqpsk.get_symbol_rate() \n
		Queries the symbol rate for P25 with CQPSK modulation. \n
			:return: srate: Range: 4800 symbol/s to 4800 symbol/s , Unit: symbol/s
		"""
		response = self._core.io.query_str('SOURce:AFRF:GENerator<Instance>:PTFive:CQPSk:SRATe?')
		return Conversions.str_to_float(response)
