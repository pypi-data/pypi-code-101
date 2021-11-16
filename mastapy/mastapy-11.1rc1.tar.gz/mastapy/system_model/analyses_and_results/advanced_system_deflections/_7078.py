'''_7078.py

SpiralBevelGearMeshAdvancedSystemDeflection
'''


from typing import List

from mastapy.system_model.connections_and_sockets.gears import _2050
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6658
from mastapy.gears.rating.spiral_bevel import _367
from mastapy.system_model.analyses_and_results.system_deflections import _2527
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _6992
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_MESH_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections', 'SpiralBevelGearMeshAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('SpiralBevelGearMeshAdvancedSystemDeflection',)


class SpiralBevelGearMeshAdvancedSystemDeflection(_6992.BevelGearMeshAdvancedSystemDeflection):
    '''SpiralBevelGearMeshAdvancedSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _SPIRAL_BEVEL_GEAR_MESH_ADVANCED_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SpiralBevelGearMeshAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2050.SpiralBevelGearMesh':
        '''SpiralBevelGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2050.SpiralBevelGearMesh)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign is not None else None

    @property
    def connection_load_case(self) -> '_6658.SpiralBevelGearMeshLoadCase':
        '''SpiralBevelGearMeshLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6658.SpiralBevelGearMeshLoadCase)(self.wrapped.ConnectionLoadCase) if self.wrapped.ConnectionLoadCase is not None else None

    @property
    def component_detailed_analysis(self) -> '_367.SpiralBevelGearMeshRating':
        '''SpiralBevelGearMeshRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_367.SpiralBevelGearMeshRating)(self.wrapped.ComponentDetailedAnalysis) if self.wrapped.ComponentDetailedAnalysis is not None else None

    @property
    def connection_system_deflection_results(self) -> 'List[_2527.SpiralBevelGearMeshSystemDeflection]':
        '''List[SpiralBevelGearMeshSystemDeflection]: 'ConnectionSystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConnectionSystemDeflectionResults, constructor.new(_2527.SpiralBevelGearMeshSystemDeflection))
        return value
