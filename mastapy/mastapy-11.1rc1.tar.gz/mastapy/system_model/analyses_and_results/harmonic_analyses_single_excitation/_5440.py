'''_5440.py

ExternalCADModelHarmonicAnalysisOfSingleExcitation
'''


from mastapy.system_model.part_model import _2178
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6583
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5413
from mastapy._internal.python_net import python_net_import

_EXTERNAL_CAD_MODEL_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation', 'ExternalCADModelHarmonicAnalysisOfSingleExcitation')


__docformat__ = 'restructuredtext en'
__all__ = ('ExternalCADModelHarmonicAnalysisOfSingleExcitation',)


class ExternalCADModelHarmonicAnalysisOfSingleExcitation(_5413.ComponentHarmonicAnalysisOfSingleExcitation):
    '''ExternalCADModelHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    '''

    TYPE = _EXTERNAL_CAD_MODEL_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ExternalCADModelHarmonicAnalysisOfSingleExcitation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2178.ExternalCADModel':
        '''ExternalCADModel: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2178.ExternalCADModel)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_load_case(self) -> '_6583.ExternalCADModelLoadCase':
        '''ExternalCADModelLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6583.ExternalCADModelLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase is not None else None
