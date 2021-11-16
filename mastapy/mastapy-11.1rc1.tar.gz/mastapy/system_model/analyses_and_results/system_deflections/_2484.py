'''_2484.py

HypoidGearSetSystemDeflection
'''


from typing import List

from mastapy.system_model.part_model.gears import _2260
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6609
from mastapy.system_model.analyses_and_results.power_flows import _3815
from mastapy.gears.rating.hypoid import _405
from mastapy.system_model.analyses_and_results.system_deflections import _2485, _2483, _2415
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_SET_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'HypoidGearSetSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('HypoidGearSetSystemDeflection',)


class HypoidGearSetSystemDeflection(_2415.AGMAGleasonConicalGearSetSystemDeflection):
    '''HypoidGearSetSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _HYPOID_GEAR_SET_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'HypoidGearSetSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2260.HypoidGearSet':
        '''HypoidGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2260.HypoidGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def assembly_load_case(self) -> '_6609.HypoidGearSetLoadCase':
        '''HypoidGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6609.HypoidGearSetLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase is not None else None

    @property
    def power_flow_results(self) -> '_3815.HypoidGearSetPowerFlow':
        '''HypoidGearSetPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_3815.HypoidGearSetPowerFlow)(self.wrapped.PowerFlowResults) if self.wrapped.PowerFlowResults is not None else None

    @property
    def rating(self) -> '_405.HypoidGearSetRating':
        '''HypoidGearSetRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_405.HypoidGearSetRating)(self.wrapped.Rating) if self.wrapped.Rating is not None else None

    @property
    def component_detailed_analysis(self) -> '_405.HypoidGearSetRating':
        '''HypoidGearSetRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_405.HypoidGearSetRating)(self.wrapped.ComponentDetailedAnalysis) if self.wrapped.ComponentDetailedAnalysis is not None else None

    @property
    def hypoid_gears_system_deflection(self) -> 'List[_2485.HypoidGearSystemDeflection]':
        '''List[HypoidGearSystemDeflection]: 'HypoidGearsSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.HypoidGearsSystemDeflection, constructor.new(_2485.HypoidGearSystemDeflection))
        return value

    @property
    def hypoid_meshes_system_deflection(self) -> 'List[_2483.HypoidGearMeshSystemDeflection]':
        '''List[HypoidGearMeshSystemDeflection]: 'HypoidMeshesSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.HypoidMeshesSystemDeflection, constructor.new(_2483.HypoidGearMeshSystemDeflection))
        return value
