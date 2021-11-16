'''_5741.py

KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis
'''


from mastapy.system_model.part_model.gears import _2263
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6617
from mastapy.system_model.analyses_and_results.system_deflections import _2493
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5738
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis',)


class KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis(_5738.KlingelnbergCycloPalloidConicalGearHarmonicAnalysis):
    '''KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis

    This is a mastapy class.
    '''

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_HARMONIC_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2263.KlingelnbergCycloPalloidHypoidGear':
        '''KlingelnbergCycloPalloidHypoidGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2263.KlingelnbergCycloPalloidHypoidGear)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_load_case(self) -> '_6617.KlingelnbergCycloPalloidHypoidGearLoadCase':
        '''KlingelnbergCycloPalloidHypoidGearLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6617.KlingelnbergCycloPalloidHypoidGearLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase is not None else None

    @property
    def system_deflection_results(self) -> '_2493.KlingelnbergCycloPalloidHypoidGearSystemDeflection':
        '''KlingelnbergCycloPalloidHypoidGearSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2493.KlingelnbergCycloPalloidHypoidGearSystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None
