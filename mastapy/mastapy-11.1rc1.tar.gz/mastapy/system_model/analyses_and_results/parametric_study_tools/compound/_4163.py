'''_4163.py

AGMAGleasonConicalGearCompoundParametricStudyTool
'''


from typing import List

from mastapy.system_model.analyses_and_results.parametric_study_tools import _4017
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4191
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound', 'AGMAGleasonConicalGearCompoundParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('AGMAGleasonConicalGearCompoundParametricStudyTool',)


class AGMAGleasonConicalGearCompoundParametricStudyTool(_4191.ConicalGearCompoundParametricStudyTool):
    '''AGMAGleasonConicalGearCompoundParametricStudyTool

    This is a mastapy class.
    '''

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_COMPOUND_PARAMETRIC_STUDY_TOOL

    __hash__ = None

    def __init__(self, instance_to_wrap: 'AGMAGleasonConicalGearCompoundParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_4017.AGMAGleasonConicalGearParametricStudyTool]':
        '''List[AGMAGleasonConicalGearParametricStudyTool]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCases, constructor.new(_4017.AGMAGleasonConicalGearParametricStudyTool))
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_4017.AGMAGleasonConicalGearParametricStudyTool]':
        '''List[AGMAGleasonConicalGearParametricStudyTool]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCasesReady, constructor.new(_4017.AGMAGleasonConicalGearParametricStudyTool))
        return value
