'''_2492.py

KlingelnbergCycloPalloidHypoidGearSetSystemDeflection
'''


from typing import List

from mastapy.system_model.part_model.gears import _2264
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6619
from mastapy.system_model.analyses_and_results.power_flows import _3822
from mastapy.gears.rating.klingelnberg_hypoid import _375
from mastapy.system_model.analyses_and_results.system_deflections import _2493, _2491, _2489
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'KlingelnbergCycloPalloidHypoidGearSetSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidHypoidGearSetSystemDeflection',)


class KlingelnbergCycloPalloidHypoidGearSetSystemDeflection(_2489.KlingelnbergCycloPalloidConicalGearSetSystemDeflection):
    '''KlingelnbergCycloPalloidHypoidGearSetSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidHypoidGearSetSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2264.KlingelnbergCycloPalloidHypoidGearSet':
        '''KlingelnbergCycloPalloidHypoidGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2264.KlingelnbergCycloPalloidHypoidGearSet)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def assembly_load_case(self) -> '_6619.KlingelnbergCycloPalloidHypoidGearSetLoadCase':
        '''KlingelnbergCycloPalloidHypoidGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6619.KlingelnbergCycloPalloidHypoidGearSetLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase is not None else None

    @property
    def power_flow_results(self) -> '_3822.KlingelnbergCycloPalloidHypoidGearSetPowerFlow':
        '''KlingelnbergCycloPalloidHypoidGearSetPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_3822.KlingelnbergCycloPalloidHypoidGearSetPowerFlow)(self.wrapped.PowerFlowResults) if self.wrapped.PowerFlowResults is not None else None

    @property
    def rating(self) -> '_375.KlingelnbergCycloPalloidHypoidGearSetRating':
        '''KlingelnbergCycloPalloidHypoidGearSetRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_375.KlingelnbergCycloPalloidHypoidGearSetRating)(self.wrapped.Rating) if self.wrapped.Rating is not None else None

    @property
    def component_detailed_analysis(self) -> '_375.KlingelnbergCycloPalloidHypoidGearSetRating':
        '''KlingelnbergCycloPalloidHypoidGearSetRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_375.KlingelnbergCycloPalloidHypoidGearSetRating)(self.wrapped.ComponentDetailedAnalysis) if self.wrapped.ComponentDetailedAnalysis is not None else None

    @property
    def klingelnberg_cyclo_palloid_hypoid_gears_system_deflection(self) -> 'List[_2493.KlingelnbergCycloPalloidHypoidGearSystemDeflection]':
        '''List[KlingelnbergCycloPalloidHypoidGearSystemDeflection]: 'KlingelnbergCycloPalloidHypoidGearsSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidHypoidGearsSystemDeflection, constructor.new(_2493.KlingelnbergCycloPalloidHypoidGearSystemDeflection))
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_meshes_system_deflection(self) -> 'List[_2491.KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection]':
        '''List[KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection]: 'KlingelnbergCycloPalloidHypoidMeshesSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidHypoidMeshesSystemDeflection, constructor.new(_2491.KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection))
        return value
