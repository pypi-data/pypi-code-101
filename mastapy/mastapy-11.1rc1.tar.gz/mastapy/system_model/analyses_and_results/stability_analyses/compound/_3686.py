'''_3686.py

KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis
'''


from typing import List

from mastapy.system_model.part_model.gears import _2264
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3684, _3685, _3683
from mastapy.system_model.analyses_and_results.stability_analyses import _3554
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_COMPOUND_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound', 'KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis',)


class KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis(_3683.KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis):
    '''KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis

    This is a mastapy class.
    '''

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_COMPOUND_STABILITY_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2264.KlingelnbergCycloPalloidHypoidGearSet':
        '''KlingelnbergCycloPalloidHypoidGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2264.KlingelnbergCycloPalloidHypoidGearSet)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def assembly_design(self) -> '_2264.KlingelnbergCycloPalloidHypoidGearSet':
        '''KlingelnbergCycloPalloidHypoidGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2264.KlingelnbergCycloPalloidHypoidGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def klingelnberg_cyclo_palloid_hypoid_gears_compound_stability_analysis(self) -> 'List[_3684.KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis]':
        '''List[KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis]: 'KlingelnbergCycloPalloidHypoidGearsCompoundStabilityAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidHypoidGearsCompoundStabilityAnalysis, constructor.new(_3684.KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis))
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_meshes_compound_stability_analysis(self) -> 'List[_3685.KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis]':
        '''List[KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis]: 'KlingelnbergCycloPalloidHypoidMeshesCompoundStabilityAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidHypoidMeshesCompoundStabilityAnalysis, constructor.new(_3685.KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis))
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_3554.KlingelnbergCycloPalloidHypoidGearSetStabilityAnalysis]':
        '''List[KlingelnbergCycloPalloidHypoidGearSetStabilityAnalysis]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCasesReady, constructor.new(_3554.KlingelnbergCycloPalloidHypoidGearSetStabilityAnalysis))
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_3554.KlingelnbergCycloPalloidHypoidGearSetStabilityAnalysis]':
        '''List[KlingelnbergCycloPalloidHypoidGearSetStabilityAnalysis]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCases, constructor.new(_3554.KlingelnbergCycloPalloidHypoidGearSetStabilityAnalysis))
        return value
