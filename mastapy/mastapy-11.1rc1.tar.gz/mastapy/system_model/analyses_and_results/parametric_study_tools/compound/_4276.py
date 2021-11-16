'''_4276.py

TorqueConverterCompoundParametricStudyTool
'''


from typing import List

from mastapy.system_model.part_model.couplings import _2332
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4148
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4196
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound', 'TorqueConverterCompoundParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('TorqueConverterCompoundParametricStudyTool',)


class TorqueConverterCompoundParametricStudyTool(_4196.CouplingCompoundParametricStudyTool):
    '''TorqueConverterCompoundParametricStudyTool

    This is a mastapy class.
    '''

    TYPE = _TORQUE_CONVERTER_COMPOUND_PARAMETRIC_STUDY_TOOL

    __hash__ = None

    def __init__(self, instance_to_wrap: 'TorqueConverterCompoundParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2332.TorqueConverter':
        '''TorqueConverter: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2332.TorqueConverter)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def assembly_design(self) -> '_2332.TorqueConverter':
        '''TorqueConverter: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2332.TorqueConverter)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_4148.TorqueConverterParametricStudyTool]':
        '''List[TorqueConverterParametricStudyTool]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCasesReady, constructor.new(_4148.TorqueConverterParametricStudyTool))
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_4148.TorqueConverterParametricStudyTool]':
        '''List[TorqueConverterParametricStudyTool]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCases, constructor.new(_4148.TorqueConverterParametricStudyTool))
        return value
