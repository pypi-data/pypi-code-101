'''_3646.py

ConceptGearSetCompoundStabilityAnalysis
'''


from typing import List

from mastapy.system_model.part_model.gears import _2247
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3644, _3645, _3675
from mastapy.system_model.analyses_and_results.stability_analyses import _3513
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_SET_COMPOUND_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound', 'ConceptGearSetCompoundStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptGearSetCompoundStabilityAnalysis',)


class ConceptGearSetCompoundStabilityAnalysis(_3675.GearSetCompoundStabilityAnalysis):
    '''ConceptGearSetCompoundStabilityAnalysis

    This is a mastapy class.
    '''

    TYPE = _CONCEPT_GEAR_SET_COMPOUND_STABILITY_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConceptGearSetCompoundStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2247.ConceptGearSet':
        '''ConceptGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2247.ConceptGearSet)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def assembly_design(self) -> '_2247.ConceptGearSet':
        '''ConceptGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2247.ConceptGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def concept_gears_compound_stability_analysis(self) -> 'List[_3644.ConceptGearCompoundStabilityAnalysis]':
        '''List[ConceptGearCompoundStabilityAnalysis]: 'ConceptGearsCompoundStabilityAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptGearsCompoundStabilityAnalysis, constructor.new(_3644.ConceptGearCompoundStabilityAnalysis))
        return value

    @property
    def concept_meshes_compound_stability_analysis(self) -> 'List[_3645.ConceptGearMeshCompoundStabilityAnalysis]':
        '''List[ConceptGearMeshCompoundStabilityAnalysis]: 'ConceptMeshesCompoundStabilityAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptMeshesCompoundStabilityAnalysis, constructor.new(_3645.ConceptGearMeshCompoundStabilityAnalysis))
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_3513.ConceptGearSetStabilityAnalysis]':
        '''List[ConceptGearSetStabilityAnalysis]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCasesReady, constructor.new(_3513.ConceptGearSetStabilityAnalysis))
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_3513.ConceptGearSetStabilityAnalysis]':
        '''List[ConceptGearSetStabilityAnalysis]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCases, constructor.new(_3513.ConceptGearSetStabilityAnalysis))
        return value
