'''_7084.py

StraightBevelDiffGearMeshAdvancedSystemDeflection
'''


from typing import List

from mastapy.system_model.connections_and_sockets.gears import _2052
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6664
from mastapy.gears.rating.straight_bevel_diff import _360
from mastapy.system_model.analyses_and_results.system_deflections import _2533
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _6992
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_MESH_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections', 'StraightBevelDiffGearMeshAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelDiffGearMeshAdvancedSystemDeflection',)


class StraightBevelDiffGearMeshAdvancedSystemDeflection(_6992.BevelGearMeshAdvancedSystemDeflection):
    '''StraightBevelDiffGearMeshAdvancedSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_MESH_ADVANCED_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'StraightBevelDiffGearMeshAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2052.StraightBevelDiffGearMesh':
        '''StraightBevelDiffGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2052.StraightBevelDiffGearMesh)(self.wrapped.ConnectionDesign) if self.wrapped.ConnectionDesign is not None else None

    @property
    def connection_load_case(self) -> '_6664.StraightBevelDiffGearMeshLoadCase':
        '''StraightBevelDiffGearMeshLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6664.StraightBevelDiffGearMeshLoadCase)(self.wrapped.ConnectionLoadCase) if self.wrapped.ConnectionLoadCase is not None else None

    @property
    def component_detailed_analysis(self) -> '_360.StraightBevelDiffGearMeshRating':
        '''StraightBevelDiffGearMeshRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_360.StraightBevelDiffGearMeshRating)(self.wrapped.ComponentDetailedAnalysis) if self.wrapped.ComponentDetailedAnalysis is not None else None

    @property
    def connection_system_deflection_results(self) -> 'List[_2533.StraightBevelDiffGearMeshSystemDeflection]':
        '''List[StraightBevelDiffGearMeshSystemDeflection]: 'ConnectionSystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConnectionSystemDeflectionResults, constructor.new(_2533.StraightBevelDiffGearMeshSystemDeflection))
        return value
