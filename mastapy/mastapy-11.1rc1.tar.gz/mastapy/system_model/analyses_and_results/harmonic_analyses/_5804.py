'''_5804.py

ZerolBevelGearSetHarmonicAnalysis
'''


from typing import List

from mastapy.system_model.part_model.gears import _2279
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6691
from mastapy.system_model.analyses_and_results.system_deflections import _2560
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5802, _5803, _5666
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_SET_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'ZerolBevelGearSetHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ZerolBevelGearSetHarmonicAnalysis',)


class ZerolBevelGearSetHarmonicAnalysis(_5666.BevelGearSetHarmonicAnalysis):
    '''ZerolBevelGearSetHarmonicAnalysis

    This is a mastapy class.
    '''

    TYPE = _ZEROL_BEVEL_GEAR_SET_HARMONIC_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ZerolBevelGearSetHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2279.ZerolBevelGearSet':
        '''ZerolBevelGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2279.ZerolBevelGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def assembly_load_case(self) -> '_6691.ZerolBevelGearSetLoadCase':
        '''ZerolBevelGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6691.ZerolBevelGearSetLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase is not None else None

    @property
    def system_deflection_results(self) -> '_2560.ZerolBevelGearSetSystemDeflection':
        '''ZerolBevelGearSetSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2560.ZerolBevelGearSetSystemDeflection)(self.wrapped.SystemDeflectionResults) if self.wrapped.SystemDeflectionResults is not None else None

    @property
    def gears_harmonic_analysis(self) -> 'List[_5802.ZerolBevelGearHarmonicAnalysis]':
        '''List[ZerolBevelGearHarmonicAnalysis]: 'GearsHarmonicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.GearsHarmonicAnalysis, constructor.new(_5802.ZerolBevelGearHarmonicAnalysis))
        return value

    @property
    def zerol_bevel_gears_harmonic_analysis(self) -> 'List[_5802.ZerolBevelGearHarmonicAnalysis]':
        '''List[ZerolBevelGearHarmonicAnalysis]: 'ZerolBevelGearsHarmonicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ZerolBevelGearsHarmonicAnalysis, constructor.new(_5802.ZerolBevelGearHarmonicAnalysis))
        return value

    @property
    def meshes_harmonic_analysis(self) -> 'List[_5803.ZerolBevelGearMeshHarmonicAnalysis]':
        '''List[ZerolBevelGearMeshHarmonicAnalysis]: 'MeshesHarmonicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MeshesHarmonicAnalysis, constructor.new(_5803.ZerolBevelGearMeshHarmonicAnalysis))
        return value

    @property
    def zerol_bevel_meshes_harmonic_analysis(self) -> 'List[_5803.ZerolBevelGearMeshHarmonicAnalysis]':
        '''List[ZerolBevelGearMeshHarmonicAnalysis]: 'ZerolBevelMeshesHarmonicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ZerolBevelMeshesHarmonicAnalysis, constructor.new(_5803.ZerolBevelGearMeshHarmonicAnalysis))
        return value
