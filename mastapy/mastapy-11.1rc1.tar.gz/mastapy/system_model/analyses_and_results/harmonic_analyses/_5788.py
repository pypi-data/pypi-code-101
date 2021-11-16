'''_5788.py

SynchroniserHalfHarmonicAnalysis
'''


from mastapy.system_model.part_model.couplings import _2329
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6671
from mastapy.system_model.analyses_and_results.system_deflections import _2541
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5790
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_HALF_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'SynchroniserHalfHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('SynchroniserHalfHarmonicAnalysis',)


class SynchroniserHalfHarmonicAnalysis(_5790.SynchroniserPartHarmonicAnalysis):
    '''SynchroniserHalfHarmonicAnalysis

    This is a mastapy class.
    '''

    TYPE = _SYNCHRONISER_HALF_HARMONIC_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SynchroniserHalfHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2329.SynchroniserHalf':
        '''SynchroniserHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2329.SynchroniserHalf)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_load_case(self) -> '_6671.SynchroniserHalfLoadCase':
        '''SynchroniserHalfLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6671.SynchroniserHalfLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase is not None else None

    @property
    def system_deflection_results(self) -> '_2541.SynchroniserHalfSystemDeflection':
        '''SynchroniserHalfSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2541.SynchroniserHalfSystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None
