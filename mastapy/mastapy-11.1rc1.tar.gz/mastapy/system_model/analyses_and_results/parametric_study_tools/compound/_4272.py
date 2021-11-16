'''_4272.py

SynchroniserCompoundParametricStudyTool
'''


from typing import List

from mastapy.system_model.part_model.couplings import _2327
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4144
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4257
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound', 'SynchroniserCompoundParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('SynchroniserCompoundParametricStudyTool',)


class SynchroniserCompoundParametricStudyTool(_4257.SpecialisedAssemblyCompoundParametricStudyTool):
    '''SynchroniserCompoundParametricStudyTool

    This is a mastapy class.
    '''

    TYPE = _SYNCHRONISER_COMPOUND_PARAMETRIC_STUDY_TOOL

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SynchroniserCompoundParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2327.Synchroniser':
        '''Synchroniser: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2327.Synchroniser)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def assembly_design(self) -> '_2327.Synchroniser':
        '''Synchroniser: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2327.Synchroniser)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_4144.SynchroniserParametricStudyTool]':
        '''List[SynchroniserParametricStudyTool]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCasesReady, constructor.new(_4144.SynchroniserParametricStudyTool))
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_4144.SynchroniserParametricStudyTool]':
        '''List[SynchroniserParametricStudyTool]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCases, constructor.new(_4144.SynchroniserParametricStudyTool))
        return value
