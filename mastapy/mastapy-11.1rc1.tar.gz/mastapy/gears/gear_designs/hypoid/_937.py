'''_937.py

HypoidGearMeshDesign
'''


from typing import List

from mastapy.gears.gear_designs.hypoid import _938, _936, _939
from mastapy._internal import constructor, conversion
from mastapy.gears.gear_designs.agma_gleason_conical import _1136
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_MESH_DESIGN = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Hypoid', 'HypoidGearMeshDesign')


__docformat__ = 'restructuredtext en'
__all__ = ('HypoidGearMeshDesign',)


class HypoidGearMeshDesign(_1136.AGMAGleasonConicalGearMeshDesign):
    '''HypoidGearMeshDesign

    This is a mastapy class.
    '''

    TYPE = _HYPOID_GEAR_MESH_DESIGN

    __hash__ = None

    def __init__(self, instance_to_wrap: 'HypoidGearMeshDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def hypoid_gear_set(self) -> '_938.HypoidGearSetDesign':
        '''HypoidGearSetDesign: 'HypoidGearSet' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_938.HypoidGearSetDesign)(self.wrapped.HypoidGearSet) if self.wrapped.HypoidGearSet is not None else None

    @property
    def hypoid_gears(self) -> 'List[_936.HypoidGearDesign]':
        '''List[HypoidGearDesign]: 'HypoidGears' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.HypoidGears, constructor.new(_936.HypoidGearDesign))
        return value

    @property
    def hypoid_meshed_gears(self) -> 'List[_939.HypoidMeshedGearDesign]':
        '''List[HypoidMeshedGearDesign]: 'HypoidMeshedGears' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.HypoidMeshedGears, constructor.new(_939.HypoidMeshedGearDesign))
        return value
