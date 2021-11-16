'''_3738.py

WormGearCompoundStabilityAnalysis
'''


from typing import List

from mastapy.system_model.part_model.gears import _2276
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses import _3611
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3673
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_COMPOUND_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound', 'WormGearCompoundStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGearCompoundStabilityAnalysis',)


class WormGearCompoundStabilityAnalysis(_3673.GearCompoundStabilityAnalysis):
    '''WormGearCompoundStabilityAnalysis

    This is a mastapy class.
    '''

    TYPE = _WORM_GEAR_COMPOUND_STABILITY_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'WormGearCompoundStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2276.WormGear':
        '''WormGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2276.WormGear)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_3611.WormGearStabilityAnalysis]':
        '''List[WormGearStabilityAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCasesReady, constructor.new(_3611.WormGearStabilityAnalysis))
        return value

    @property
    def component_analysis_cases(self) -> 'List[_3611.WormGearStabilityAnalysis]':
        '''List[WormGearStabilityAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCases, constructor.new(_3611.WormGearStabilityAnalysis))
        return value
