'''_5746.py

KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis
'''


from typing import List

from mastapy.system_model.part_model.gears import _2266
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6622
from mastapy.system_model.analyses_and_results.system_deflections import _2495
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5744, _5745, _5740
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis',)


class KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis(_5740.KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis):
    '''KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis

    This is a mastapy class.
    '''

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET_HARMONIC_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2266.KlingelnbergCycloPalloidSpiralBevelGearSet':
        '''KlingelnbergCycloPalloidSpiralBevelGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2266.KlingelnbergCycloPalloidSpiralBevelGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def assembly_load_case(self) -> '_6622.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase':
        '''KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6622.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase is not None else None

    @property
    def system_deflection_results(self) -> '_2495.KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection':
        '''KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2495.KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None

    @property
    def gears_harmonic_analysis(self) -> 'List[_5744.KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysis]':
        '''List[KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysis]: 'GearsHarmonicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.GearsHarmonicAnalysis, constructor.new(_5744.KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysis))
        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gears_harmonic_analysis(self) -> 'List[_5744.KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysis]':
        '''List[KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysis]: 'KlingelnbergCycloPalloidSpiralBevelGearsHarmonicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearsHarmonicAnalysis, constructor.new(_5744.KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysis))
        return value

    @property
    def meshes_harmonic_analysis(self) -> 'List[_5745.KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysis]':
        '''List[KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysis]: 'MeshesHarmonicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MeshesHarmonicAnalysis, constructor.new(_5745.KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysis))
        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_meshes_harmonic_analysis(self) -> 'List[_5745.KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysis]':
        '''List[KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysis]: 'KlingelnbergCycloPalloidSpiralBevelMeshesHarmonicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidSpiralBevelMeshesHarmonicAnalysis, constructor.new(_5745.KlingelnbergCycloPalloidSpiralBevelGearMeshHarmonicAnalysis))
        return value
