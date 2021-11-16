'''_5644.py

ZerolBevelGearCompoundHarmonicAnalysisOfSingleExcitation
'''


from typing import List

from mastapy.system_model.part_model.gears import _2278
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5515
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _5534
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound', 'ZerolBevelGearCompoundHarmonicAnalysisOfSingleExcitation')


__docformat__ = 'restructuredtext en'
__all__ = ('ZerolBevelGearCompoundHarmonicAnalysisOfSingleExcitation',)


class ZerolBevelGearCompoundHarmonicAnalysisOfSingleExcitation(_5534.BevelGearCompoundHarmonicAnalysisOfSingleExcitation):
    '''ZerolBevelGearCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    '''

    TYPE = _ZEROL_BEVEL_GEAR_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ZerolBevelGearCompoundHarmonicAnalysisOfSingleExcitation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2278.ZerolBevelGear':
        '''ZerolBevelGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2278.ZerolBevelGear)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_5515.ZerolBevelGearHarmonicAnalysisOfSingleExcitation]':
        '''List[ZerolBevelGearHarmonicAnalysisOfSingleExcitation]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCasesReady, constructor.new(_5515.ZerolBevelGearHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def component_analysis_cases(self) -> 'List[_5515.ZerolBevelGearHarmonicAnalysisOfSingleExcitation]':
        '''List[ZerolBevelGearHarmonicAnalysisOfSingleExcitation]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCases, constructor.new(_5515.ZerolBevelGearHarmonicAnalysisOfSingleExcitation))
        return value
