'''_5763.py

RingPinsToDiscConnectionHarmonicAnalysis
'''


from mastapy.system_model.connections_and_sockets.cycloidal import _2068
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6647
from mastapy.system_model.analyses_and_results.system_deflections import _2515
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5737
from mastapy._internal.python_net import python_net_import

_RING_PINS_TO_DISC_CONNECTION_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'RingPinsToDiscConnectionHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('RingPinsToDiscConnectionHarmonicAnalysis',)


class RingPinsToDiscConnectionHarmonicAnalysis(_5737.InterMountableComponentConnectionHarmonicAnalysis):
    '''RingPinsToDiscConnectionHarmonicAnalysis

    This is a mastapy class.
    '''

    TYPE = _RING_PINS_TO_DISC_CONNECTION_HARMONIC_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'RingPinsToDiscConnectionHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2068.RingPinsToDiscConnection':
        '''RingPinsToDiscConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2068.RingPinsToDiscConnection)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign is not None else None

    @property
    def connection_load_case(self) -> '_6647.RingPinsToDiscConnectionLoadCase':
        '''RingPinsToDiscConnectionLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6647.RingPinsToDiscConnectionLoadCase)(self.wrapped.ConnectionLoadCase) if self.wrapped.ConnectionLoadCase is not None else None

    @property
    def system_deflection_results(self) -> '_2515.RingPinsToDiscConnectionSystemDeflection':
        '''RingPinsToDiscConnectionSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2515.RingPinsToDiscConnectionSystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None
