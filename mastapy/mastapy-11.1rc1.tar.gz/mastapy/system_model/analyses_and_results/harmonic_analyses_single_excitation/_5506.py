'''_5506.py

TorqueConverterConnectionHarmonicAnalysisOfSingleExcitation
'''


from mastapy.system_model.connections_and_sockets.couplings import _2079
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6676
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5425
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_CONNECTION_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation', 'TorqueConverterConnectionHarmonicAnalysisOfSingleExcitation')


__docformat__ = 'restructuredtext en'
__all__ = ('TorqueConverterConnectionHarmonicAnalysisOfSingleExcitation',)


class TorqueConverterConnectionHarmonicAnalysisOfSingleExcitation(_5425.CouplingConnectionHarmonicAnalysisOfSingleExcitation):
    '''TorqueConverterConnectionHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    '''

    TYPE = _TORQUE_CONVERTER_CONNECTION_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'TorqueConverterConnectionHarmonicAnalysisOfSingleExcitation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2079.TorqueConverterConnection':
        '''TorqueConverterConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2079.TorqueConverterConnection)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign is not None else None

    @property
    def connection_load_case(self) -> '_6676.TorqueConverterConnectionLoadCase':
        '''TorqueConverterConnectionLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6676.TorqueConverterConnectionLoadCase)(self.wrapped.ConnectionLoadCase) if self.wrapped.ConnectionLoadCase is not None else None
