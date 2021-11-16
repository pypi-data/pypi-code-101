'''_3681.py

KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis
'''


from typing import List

from mastapy.system_model.analyses_and_results.stability_analyses import _3552
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3647
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_COMPOUND_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound', 'KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis',)


class KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis(_3647.ConicalGearCompoundStabilityAnalysis):
    '''KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis

    This is a mastapy class.
    '''

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_COMPOUND_STABILITY_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_3552.KlingelnbergCycloPalloidConicalGearStabilityAnalysis]':
        '''List[KlingelnbergCycloPalloidConicalGearStabilityAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCases, constructor.new(_3552.KlingelnbergCycloPalloidConicalGearStabilityAnalysis))
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_3552.KlingelnbergCycloPalloidConicalGearStabilityAnalysis]':
        '''List[KlingelnbergCycloPalloidConicalGearStabilityAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCasesReady, constructor.new(_3552.KlingelnbergCycloPalloidConicalGearStabilityAnalysis))
        return value
