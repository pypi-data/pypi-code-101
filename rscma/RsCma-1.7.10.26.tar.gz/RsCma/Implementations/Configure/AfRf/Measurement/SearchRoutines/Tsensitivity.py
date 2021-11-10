from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tsensitivity:
	"""Tsensitivity commands group definition. 5 total commands, 0 Sub-groups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tsensitivity", core, parent)

	def get_trelative(self) -> float:
		"""SCPI: CONFigure:AFRF:MEASurement<Instance>:SROutines:TSENsitivity:TRELative \n
		Snippet: value: float = driver.configure.afRf.measurement.searchRoutines.tsensitivity.get_trelative() \n
		No command help available \n
			:return: target_relative: No help available
		"""
		response = self._core.io.query_str('CONFigure:AFRF:MEASurement<Instance>:SROutines:TSENsitivity:TRELative?')
		return Conversions.str_to_float(response)

	def set_trelative(self, target_relative: float) -> None:
		"""SCPI: CONFigure:AFRF:MEASurement<Instance>:SROutines:TSENsitivity:TRELative \n
		Snippet: driver.configure.afRf.measurement.searchRoutines.tsensitivity.set_trelative(target_relative = 1.0) \n
		No command help available \n
			:param target_relative: No help available
		"""
		param = Conversions.decimal_value_to_str(target_relative)
		self._core.io.write(f'CONFigure:AFRF:MEASurement<Instance>:SROutines:TSENsitivity:TRELative {param}')

	def get_tf_deviation(self) -> float:
		"""SCPI: CONFigure:AFRF:MEASurement<Instance>:SROutines:TSENsitivity:TFDeviation \n
		Snippet: value: float = driver.configure.afRf.measurement.searchRoutines.tsensitivity.get_tf_deviation() \n
		No command help available \n
			:return: target_freq_dev: No help available
		"""
		response = self._core.io.query_str('CONFigure:AFRF:MEASurement<Instance>:SROutines:TSENsitivity:TFDeviation?')
		return Conversions.str_to_float(response)

	def set_tf_deviation(self, target_freq_dev: float) -> None:
		"""SCPI: CONFigure:AFRF:MEASurement<Instance>:SROutines:TSENsitivity:TFDeviation \n
		Snippet: driver.configure.afRf.measurement.searchRoutines.tsensitivity.set_tf_deviation(target_freq_dev = 1.0) \n
		No command help available \n
			:param target_freq_dev: No help available
		"""
		param = Conversions.decimal_value_to_str(target_freq_dev)
		self._core.io.write(f'CONFigure:AFRF:MEASurement<Instance>:SROutines:TSENsitivity:TFDeviation {param}')

	def get_tp_deviation(self) -> float:
		"""SCPI: CONFigure:AFRF:MEASurement<Instance>:SROutines:TSENsitivity:TPDeviation \n
		Snippet: value: float = driver.configure.afRf.measurement.searchRoutines.tsensitivity.get_tp_deviation() \n
		No command help available \n
			:return: target_phase_dev: No help available
		"""
		response = self._core.io.query_str('CONFigure:AFRF:MEASurement<Instance>:SROutines:TSENsitivity:TPDeviation?')
		return Conversions.str_to_float(response)

	def set_tp_deviation(self, target_phase_dev: float) -> None:
		"""SCPI: CONFigure:AFRF:MEASurement<Instance>:SROutines:TSENsitivity:TPDeviation \n
		Snippet: driver.configure.afRf.measurement.searchRoutines.tsensitivity.set_tp_deviation(target_phase_dev = 1.0) \n
		No command help available \n
			:param target_phase_dev: No help available
		"""
		param = Conversions.decimal_value_to_str(target_phase_dev)
		self._core.io.write(f'CONFigure:AFRF:MEASurement<Instance>:SROutines:TSENsitivity:TPDeviation {param}')

	def get_tm_depth(self) -> float:
		"""SCPI: CONFigure:AFRF:MEASurement<Instance>:SROutines:TSENsitivity:TMDepth \n
		Snippet: value: float = driver.configure.afRf.measurement.searchRoutines.tsensitivity.get_tm_depth() \n
		No command help available \n
			:return: target_mod_depth: No help available
		"""
		response = self._core.io.query_str('CONFigure:AFRF:MEASurement<Instance>:SROutines:TSENsitivity:TMDepth?')
		return Conversions.str_to_float(response)

	def set_tm_depth(self, target_mod_depth: float) -> None:
		"""SCPI: CONFigure:AFRF:MEASurement<Instance>:SROutines:TSENsitivity:TMDepth \n
		Snippet: driver.configure.afRf.measurement.searchRoutines.tsensitivity.set_tm_depth(target_mod_depth = 1.0) \n
		No command help available \n
			:param target_mod_depth: No help available
		"""
		param = Conversions.decimal_value_to_str(target_mod_depth)
		self._core.io.write(f'CONFigure:AFRF:MEASurement<Instance>:SROutines:TSENsitivity:TMDepth {param}')

	def get_ttolerance(self) -> float:
		"""SCPI: CONFigure:AFRF:MEASurement<Instance>:SROutines:TSENsitivity:TTOLerance \n
		Snippet: value: float = driver.configure.afRf.measurement.searchRoutines.tsensitivity.get_ttolerance() \n
		No command help available \n
			:return: tolerance: No help available
		"""
		response = self._core.io.query_str('CONFigure:AFRF:MEASurement<Instance>:SROutines:TSENsitivity:TTOLerance?')
		return Conversions.str_to_float(response)

	def set_ttolerance(self, tolerance: float) -> None:
		"""SCPI: CONFigure:AFRF:MEASurement<Instance>:SROutines:TSENsitivity:TTOLerance \n
		Snippet: driver.configure.afRf.measurement.searchRoutines.tsensitivity.set_ttolerance(tolerance = 1.0) \n
		No command help available \n
			:param tolerance: No help available
		"""
		param = Conversions.decimal_value_to_str(tolerance)
		self._core.io.write(f'CONFigure:AFRF:MEASurement<Instance>:SROutines:TSENsitivity:TTOLerance {param}')
