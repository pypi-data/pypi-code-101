'''_5867.py

ConceptCouplingConnectionCompoundHarmonicAnalysis
'''


from typing import List

from mastapy.system_model.connections_and_sockets.couplings import _2071
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5675
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5878
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_CONNECTION_COMPOUND_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound', 'ConceptCouplingConnectionCompoundHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptCouplingConnectionCompoundHarmonicAnalysis',)


class ConceptCouplingConnectionCompoundHarmonicAnalysis(_5878.CouplingConnectionCompoundHarmonicAnalysis):
    '''ConceptCouplingConnectionCompoundHarmonicAnalysis

    This is a mastapy class.
    '''

    TYPE = _CONCEPT_COUPLING_CONNECTION_COMPOUND_HARMONIC_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConceptCouplingConnectionCompoundHarmonicAnalysis.TYPE'):
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
    def connection_analysis_cases_ready(self) -> 'List[_5675.ConceptCouplingConnectionHarmonicAnalysis]':
        '''List[ConceptCouplingConnectionHarmonicAnalysis]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConnectionAnalysisCasesReady, constructor.new(_5675.ConceptCouplingConnectionHarmonicAnalysis))
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_5675.ConceptCouplingConnectionHarmonicAnalysis]':
        '''List[ConceptCouplingConnectionHarmonicAnalysis]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConnectionAnalysisCases, constructor.new(_5675.ConceptCouplingConnectionHarmonicAnalysis))
        return value
