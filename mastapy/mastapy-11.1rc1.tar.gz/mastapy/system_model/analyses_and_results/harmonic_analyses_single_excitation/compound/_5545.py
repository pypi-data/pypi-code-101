'''_5545.py

ConceptCouplingConnectionCompoundHarmonicAnalysisOfSingleExcitation
'''


from typing import List

from mastapy.system_model.connections_and_sockets.couplings import _2071
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5414
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _5556
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_CONNECTION_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound', 'ConceptCouplingConnectionCompoundHarmonicAnalysisOfSingleExcitation')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptCouplingConnectionCompoundHarmonicAnalysisOfSingleExcitation',)


class ConceptCouplingConnectionCompoundHarmonicAnalysisOfSingleExcitation(_5556.CouplingConnectionCompoundHarmonicAnalysisOfSingleExcitation):
    '''ConceptCouplingConnectionCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    '''

    TYPE = _CONCEPT_COUPLING_CONNECTION_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConceptCouplingConnectionCompoundHarmonicAnalysisOfSingleExcitation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2071.ConceptCouplingConnection':
        '''ConceptCouplingConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2071.ConceptCouplingConnection)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def connection_design(self) -> '_2071.ConceptCouplingConnection':
        '''ConceptCouplingConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2071.ConceptCouplingConnection)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign is not None else None

    @property
    def connection_analysis_cases_ready(self) -> 'List[_5414.ConceptCouplingConnectionHarmonicAnalysisOfSingleExcitation]':
        '''List[ConceptCouplingConnectionHarmonicAnalysisOfSingleExcitation]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConnectionAnalysisCasesReady, constructor.new(_5414.ConceptCouplingConnectionHarmonicAnalysisOfSingleExcitation))
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_5414.ConceptCouplingConnectionHarmonicAnalysisOfSingleExcitation]':
        '''List[ConceptCouplingConnectionHarmonicAnalysisOfSingleExcitation]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConnectionAnalysisCases, constructor.new(_5414.ConceptCouplingConnectionHarmonicAnalysisOfSingleExcitation))
        return value
