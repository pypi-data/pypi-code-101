'''_5547.py

ConceptGearCompoundHarmonicAnalysisOfSingleExcitation
'''


from typing import List

from mastapy.system_model.part_model.gears import _2246
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5417
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _5576
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound', 'ConceptGearCompoundHarmonicAnalysisOfSingleExcitation')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptGearCompoundHarmonicAnalysisOfSingleExcitation',)


class ConceptGearCompoundHarmonicAnalysisOfSingleExcitation(_5576.GearCompoundHarmonicAnalysisOfSingleExcitation):
    '''ConceptGearCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    '''

    TYPE = _CONCEPT_GEAR_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConceptGearCompoundHarmonicAnalysisOfSingleExcitation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2246.ConceptGear':
        '''ConceptGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2246.ConceptGear)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_5417.ConceptGearHarmonicAnalysisOfSingleExcitation]':
        '''List[ConceptGearHarmonicAnalysisOfSingleExcitation]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCasesReady, constructor.new(_5417.ConceptGearHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def component_analysis_cases(self) -> 'List[_5417.ConceptGearHarmonicAnalysisOfSingleExcitation]':
        '''List[ConceptGearHarmonicAnalysisOfSingleExcitation]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCases, constructor.new(_5417.ConceptGearHarmonicAnalysisOfSingleExcitation))
        return value
