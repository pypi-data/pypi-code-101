'''_5923.py

PlanetaryConnectionCompoundHarmonicAnalysis
'''


from typing import List

from mastapy.system_model.connections_and_sockets import _2014
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5756
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5937
from mastapy._internal.python_net import python_net_import

_PLANETARY_CONNECTION_COMPOUND_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound', 'PlanetaryConnectionCompoundHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('PlanetaryConnectionCompoundHarmonicAnalysis',)


class PlanetaryConnectionCompoundHarmonicAnalysis(_5937.ShaftToMountableComponentConnectionCompoundHarmonicAnalysis):
    '''PlanetaryConnectionCompoundHarmonicAnalysis

    This is a mastapy class.
    '''

    TYPE = _PLANETARY_CONNECTION_COMPOUND_HARMONIC_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'PlanetaryConnectionCompoundHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2014.PlanetaryConnection':
        '''PlanetaryConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2014.PlanetaryConnection)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def connection_design(self) -> '_2014.PlanetaryConnection':
        '''PlanetaryConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2014.PlanetaryConnection)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign is not None else None

    @property
    def connection_analysis_cases_ready(self) -> 'List[_5756.PlanetaryConnectionHarmonicAnalysis]':
        '''List[PlanetaryConnectionHarmonicAnalysis]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConnectionAnalysisCasesReady, constructor.new(_5756.PlanetaryConnectionHarmonicAnalysis))
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_5756.PlanetaryConnectionHarmonicAnalysis]':
        '''List[PlanetaryConnectionHarmonicAnalysis]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConnectionAnalysisCases, constructor.new(_5756.PlanetaryConnectionHarmonicAnalysis))
        return value
