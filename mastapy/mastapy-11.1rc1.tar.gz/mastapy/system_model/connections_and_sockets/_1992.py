'''_1992.py

AbstractShaftToMountableComponentConnection
'''


from mastapy.system_model.part_model import (
    _2190, _2167, _2174, _2188,
    _2189, _2192, _2195, _2197,
    _2198, _2203, _2205, _2163
)
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.part_model.gears import (
    _2238, _2240, _2242, _2243,
    _2244, _2246, _2248, _2250,
    _2252, _2253, _2255, _2259,
    _2261, _2263, _2265, _2268,
    _2270, _2272, _2274, _2275,
    _2276, _2278
)
from mastapy.system_model.part_model.cycloidal import _2295, _2294
from mastapy.system_model.part_model.couplings import (
    _2304, _2307, _2309, _2312,
    _2314, _2315, _2321, _2323,
    _2326, _2329, _2330, _2331,
    _2333, _2335
)
from mastapy.system_model.part_model.shaft_model import _2208
from mastapy.system_model.connections_and_sockets import _1999
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets', 'AbstractShaftToMountableComponentConnection')


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractShaftToMountableComponentConnection',)


class AbstractShaftToMountableComponentConnection(_1999.Connection):
    '''AbstractShaftToMountableComponentConnection

    This is a mastapy class.
    '''

    TYPE = _ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'AbstractShaftToMountableComponentConnection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def mountable_component(self) -> '_2190.MountableComponent':
        '''MountableComponent: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2190.MountableComponent.TYPE not in self.wrapped.MountableComponent.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to MountableComponent. Expected: {}.'.format(self.wrapped.MountableComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.MountableComponent.__class__)(self.wrapped.MountableComponent) if self.wrapped.MountableComponent is not None else None

    @property
    def mountable_component_of_type_bearing(self) -> '_2167.Bearing':
        '''Bearing: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2167.Bearing.TYPE not in self.wrapped.MountableComponent.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to Bearing. Expected: {}.'.format(self.wrapped.MountableComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.MountableComponent.__class__)(self.wrapped.MountableComponent) if self.wrapped.MountableComponent is not None else None

    @property
    def mountable_component_of_type_connector(self) -> '_2174.Connector':
        '''Connector: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2174.Connector.TYPE not in self.wrapped.MountableComponent.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to Connector. Expected: {}.'.format(self.wrapped.MountableComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.MountableComponent.__class__)(self.wrapped.MountableComponent) if self.wrapped.MountableComponent is not None else None

    @property
    def mountable_component_of_type_mass_disc(self) -> '_2188.MassDisc':
        '''MassDisc: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2188.MassDisc.TYPE not in self.wrapped.MountableComponent.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to MassDisc. Expected: {}.'.format(self.wrapped.MountableComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.MountableComponent.__class__)(self.wrapped.MountableComponent) if self.wrapped.MountableComponent is not None else None

    @property
    def mountable_component_of_type_measurement_component(self) -> '_2189.MeasurementComponent':
        '''MeasurementComponent: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2189.MeasurementComponent.TYPE not in self.wrapped.MountableComponent.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to MeasurementComponent. Expected: {}.'.format(self.wrapped.MountableComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.MountableComponent.__class__)(self.wrapped.MountableComponent) if self.wrapped.MountableComponent is not None else None

    @property
    def mountable_component_of_type_oil_seal(self) -> '_2192.OilSeal':
        '''OilSeal: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2192.OilSeal.TYPE not in self.wrapped.MountableComponent.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to OilSeal. Expected: {}.'.format(self.wrapped.MountableComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.MountableComponent.__class__)(self.wrapped.MountableComponent) if self.wrapped.MountableComponent is not None else None

    @property
    def mountable_component_of_type_planet_carrier(self) -> '_2195.PlanetCarrier':
        '''PlanetCarrier: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2195.PlanetCarrier.TYPE not in self.wrapped.MountableComponent.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to PlanetCarrier. Expected: {}.'.format(self.wrapped.MountableComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.MountableComponent.__class__)(self.wrapped.MountableComponent) if self.wrapped.MountableComponent is not None else None

    @property
    def mountable_component_of_type_point_load(self) -> '_2197.PointLoad':
        '''PointLoad: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2197.PointLoad.TYPE not in self.wrapped.MountableComponent.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to PointLoad. Expected: {}.'.format(self.wrapped.MountableComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.MountableComponent.__class__)(self.wrapped.MountableComponent) if self.wrapped.MountableComponent is not None else None

    @property
    def mountable_component_of_type_power_load(self) -> '_2198.PowerLoad':
        '''PowerLoad: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2198.PowerLoad.TYPE not in self.wrapped.MountableComponent.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to PowerLoad. Expected: {}.'.format(self.wrapped.MountableComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.MountableComponent.__class__)(self.wrapped.MountableComponent) if self.wrapped.MountableComponent is not None else None

    @property
    def mountable_component_of_type_unbalanced_mass(self) -> '_2203.UnbalancedMass':
        '''UnbalancedMass: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2203.UnbalancedMass.TYPE not in self.wrapped.MountableComponent.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to UnbalancedMass. Expected: {}.'.format(self.wrapped.MountableComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.MountableComponent.__class__)(self.wrapped.MountableComponent) if self.wrapped.MountableComponent is not None else None

    @property
    def mountable_component_of_type_virtual_component(self) -> '_2205.VirtualComponent':
        '''VirtualComponent: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2205.VirtualComponent.TYPE not in self.wrapped.MountableComponent.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to VirtualComponent. Expected: {}.'.format(self.wrapped.MountableComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.MountableComponent.__class__)(self.wrapped.MountableComponent) if self.wrapped.MountableComponent is not None else None

    @property
    def mountable_component_of_type_agma_gleason_conical_gear(self) -> '_2238.AGMAGleasonConicalGear':
        '''AGMAGleasonConicalGear: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2238.AGMAGleasonConicalGear.TYPE not in self.wrapped.MountableComponent.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to AGMAGleasonConicalGear. Expected: {}.'.format(self.wrapped.MountableComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.MountableComponent.__class__)(self.wrapped.MountableComponent) if self.wrapped.MountableComponent is not None else None

    @property
    def mountable_component_of_type_bevel_differential_gear(self) -> '_2240.BevelDifferentialGear':
        '''BevelDifferentialGear: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2240.BevelDifferentialGear.TYPE not in self.wrapped.MountableComponent.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to BevelDifferentialGear. Expected: {}.'.format(self.wrapped.MountableComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.MountableComponent.__class__)(self.wrapped.MountableComponent) if self.wrapped.MountableComponent is not None else None

    @property
    def mountable_component_of_type_bevel_differential_planet_gear(self) -> '_2242.BevelDifferentialPlanetGear':
        '''BevelDifferentialPlanetGear: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2242.BevelDifferentialPlanetGear.TYPE not in self.wrapped.MountableComponent.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to BevelDifferentialPlanetGear. Expected: {}.'.format(self.wrapped.MountableComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.MountableComponent.__class__)(self.wrapped.MountableComponent) if self.wrapped.MountableComponent is not None else None

    @property
    def mountable_component_of_type_bevel_differential_sun_gear(self) -> '_2243.BevelDifferentialSunGear':
        '''BevelDifferentialSunGear: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2243.BevelDifferentialSunGear.TYPE not in self.wrapped.MountableComponent.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to BevelDifferentialSunGear. Expected: {}.'.format(self.wrapped.MountableComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.MountableComponent.__class__)(self.wrapped.MountableComponent) if self.wrapped.MountableComponent is not None else None

    @property
    def mountable_component_of_type_bevel_gear(self) -> '_2244.BevelGear':
        '''BevelGear: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2244.BevelGear.TYPE not in self.wrapped.MountableComponent.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to BevelGear. Expected: {}.'.format(self.wrapped.MountableComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.MountableComponent.__class__)(self.wrapped.MountableComponent) if self.wrapped.MountableComponent is not None else None

    @property
    def mountable_component_of_type_concept_gear(self) -> '_2246.ConceptGear':
        '''ConceptGear: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2246.ConceptGear.TYPE not in self.wrapped.MountableComponent.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to ConceptGear. Expected: {}.'.format(self.wrapped.MountableComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.MountableComponent.__class__)(self.wrapped.MountableComponent) if self.wrapped.MountableComponent is not None else None

    @property
    def mountable_component_of_type_conical_gear(self) -> '_2248.ConicalGear':
        '''ConicalGear: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2248.ConicalGear.TYPE not in self.wrapped.MountableComponent.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to ConicalGear. Expected: {}.'.format(self.wrapped.MountableComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.MountableComponent.__class__)(self.wrapped.MountableComponent) if self.wrapped.MountableComponent is not None else None

    @property
    def mountable_component_of_type_cylindrical_gear(self) -> '_2250.CylindricalGear':
        '''CylindricalGear: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2250.CylindricalGear.TYPE not in self.wrapped.MountableComponent.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to CylindricalGear. Expected: {}.'.format(self.wrapped.MountableComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.MountableComponent.__class__)(self.wrapped.MountableComponent) if self.wrapped.MountableComponent is not None else None

    @property
    def mountable_component_of_type_cylindrical_planet_gear(self) -> '_2252.CylindricalPlanetGear':
        '''CylindricalPlanetGear: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2252.CylindricalPlanetGear.TYPE not in self.wrapped.MountableComponent.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to CylindricalPlanetGear. Expected: {}.'.format(self.wrapped.MountableComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.MountableComponent.__class__)(self.wrapped.MountableComponent) if self.wrapped.MountableComponent is not None else None

    @property
    def mountable_component_of_type_face_gear(self) -> '_2253.FaceGear':
        '''FaceGear: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2253.FaceGear.TYPE not in self.wrapped.MountableComponent.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to FaceGear. Expected: {}.'.format(self.wrapped.MountableComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.MountableComponent.__class__)(self.wrapped.MountableComponent) if self.wrapped.MountableComponent is not None else None

    @property
    def mountable_component_of_type_gear(self) -> '_2255.Gear':
        '''Gear: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2255.Gear.TYPE not in self.wrapped.MountableComponent.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to Gear. Expected: {}.'.format(self.wrapped.MountableComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.MountableComponent.__class__)(self.wrapped.MountableComponent) if self.wrapped.MountableComponent is not None else None

    @property
    def mountable_component_of_type_hypoid_gear(self) -> '_2259.HypoidGear':
        '''HypoidGear: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2259.HypoidGear.TYPE not in self.wrapped.MountableComponent.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to HypoidGear. Expected: {}.'.format(self.wrapped.MountableComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.MountableComponent.__class__)(self.wrapped.MountableComponent) if self.wrapped.MountableComponent is not None else None

    @property
    def mountable_component_of_type_klingelnberg_cyclo_palloid_conical_gear(self) -> '_2261.KlingelnbergCycloPalloidConicalGear':
        '''KlingelnbergCycloPalloidConicalGear: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2261.KlingelnbergCycloPalloidConicalGear.TYPE not in self.wrapped.MountableComponent.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to KlingelnbergCycloPalloidConicalGear. Expected: {}.'.format(self.wrapped.MountableComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.MountableComponent.__class__)(self.wrapped.MountableComponent) if self.wrapped.MountableComponent is not None else None

    @property
    def mountable_component_of_type_klingelnberg_cyclo_palloid_hypoid_gear(self) -> '_2263.KlingelnbergCycloPalloidHypoidGear':
        '''KlingelnbergCycloPalloidHypoidGear: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2263.KlingelnbergCycloPalloidHypoidGear.TYPE not in self.wrapped.MountableComponent.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to KlingelnbergCycloPalloidHypoidGear. Expected: {}.'.format(self.wrapped.MountableComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.MountableComponent.__class__)(self.wrapped.MountableComponent) if self.wrapped.MountableComponent is not None else None

    @property
    def mountable_component_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear(self) -> '_2265.KlingelnbergCycloPalloidSpiralBevelGear':
        '''KlingelnbergCycloPalloidSpiralBevelGear: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2265.KlingelnbergCycloPalloidSpiralBevelGear.TYPE not in self.wrapped.MountableComponent.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to KlingelnbergCycloPalloidSpiralBevelGear. Expected: {}.'.format(self.wrapped.MountableComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.MountableComponent.__class__)(self.wrapped.MountableComponent) if self.wrapped.MountableComponent is not None else None

    @property
    def mountable_component_of_type_spiral_bevel_gear(self) -> '_2268.SpiralBevelGear':
        '''SpiralBevelGear: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2268.SpiralBevelGear.TYPE not in self.wrapped.MountableComponent.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to SpiralBevelGear. Expected: {}.'.format(self.wrapped.MountableComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.MountableComponent.__class__)(self.wrapped.MountableComponent) if self.wrapped.MountableComponent is not None else None

    @property
    def mountable_component_of_type_straight_bevel_diff_gear(self) -> '_2270.StraightBevelDiffGear':
        '''StraightBevelDiffGear: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2270.StraightBevelDiffGear.TYPE not in self.wrapped.MountableComponent.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to StraightBevelDiffGear. Expected: {}.'.format(self.wrapped.MountableComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.MountableComponent.__class__)(self.wrapped.MountableComponent) if self.wrapped.MountableComponent is not None else None

    @property
    def mountable_component_of_type_straight_bevel_gear(self) -> '_2272.StraightBevelGear':
        '''StraightBevelGear: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2272.StraightBevelGear.TYPE not in self.wrapped.MountableComponent.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to StraightBevelGear. Expected: {}.'.format(self.wrapped.MountableComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.MountableComponent.__class__)(self.wrapped.MountableComponent) if self.wrapped.MountableComponent is not None else None

    @property
    def mountable_component_of_type_straight_bevel_planet_gear(self) -> '_2274.StraightBevelPlanetGear':
        '''StraightBevelPlanetGear: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2274.StraightBevelPlanetGear.TYPE not in self.wrapped.MountableComponent.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to StraightBevelPlanetGear. Expected: {}.'.format(self.wrapped.MountableComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.MountableComponent.__class__)(self.wrapped.MountableComponent) if self.wrapped.MountableComponent is not None else None

    @property
    def mountable_component_of_type_straight_bevel_sun_gear(self) -> '_2275.StraightBevelSunGear':
        '''StraightBevelSunGear: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2275.StraightBevelSunGear.TYPE not in self.wrapped.MountableComponent.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to StraightBevelSunGear. Expected: {}.'.format(self.wrapped.MountableComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.MountableComponent.__class__)(self.wrapped.MountableComponent) if self.wrapped.MountableComponent is not None else None

    @property
    def mountable_component_of_type_worm_gear(self) -> '_2276.WormGear':
        '''WormGear: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2276.WormGear.TYPE not in self.wrapped.MountableComponent.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to WormGear. Expected: {}.'.format(self.wrapped.MountableComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.MountableComponent.__class__)(self.wrapped.MountableComponent) if self.wrapped.MountableComponent is not None else None

    @property
    def mountable_component_of_type_zerol_bevel_gear(self) -> '_2278.ZerolBevelGear':
        '''ZerolBevelGear: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2278.ZerolBevelGear.TYPE not in self.wrapped.MountableComponent.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to ZerolBevelGear. Expected: {}.'.format(self.wrapped.MountableComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.MountableComponent.__class__)(self.wrapped.MountableComponent) if self.wrapped.MountableComponent is not None else None

    @property
    def mountable_component_of_type_ring_pins(self) -> '_2295.RingPins':
        '''RingPins: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2295.RingPins.TYPE not in self.wrapped.MountableComponent.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to RingPins. Expected: {}.'.format(self.wrapped.MountableComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.MountableComponent.__class__)(self.wrapped.MountableComponent) if self.wrapped.MountableComponent is not None else None

    @property
    def mountable_component_of_type_clutch_half(self) -> '_2304.ClutchHalf':
        '''ClutchHalf: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2304.ClutchHalf.TYPE not in self.wrapped.MountableComponent.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to ClutchHalf. Expected: {}.'.format(self.wrapped.MountableComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.MountableComponent.__class__)(self.wrapped.MountableComponent) if self.wrapped.MountableComponent is not None else None

    @property
    def mountable_component_of_type_concept_coupling_half(self) -> '_2307.ConceptCouplingHalf':
        '''ConceptCouplingHalf: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2307.ConceptCouplingHalf.TYPE not in self.wrapped.MountableComponent.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to ConceptCouplingHalf. Expected: {}.'.format(self.wrapped.MountableComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.MountableComponent.__class__)(self.wrapped.MountableComponent) if self.wrapped.MountableComponent is not None else None

    @property
    def mountable_component_of_type_coupling_half(self) -> '_2309.CouplingHalf':
        '''CouplingHalf: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2309.CouplingHalf.TYPE not in self.wrapped.MountableComponent.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to CouplingHalf. Expected: {}.'.format(self.wrapped.MountableComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.MountableComponent.__class__)(self.wrapped.MountableComponent) if self.wrapped.MountableComponent is not None else None

    @property
    def mountable_component_of_type_cvt_pulley(self) -> '_2312.CVTPulley':
        '''CVTPulley: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2312.CVTPulley.TYPE not in self.wrapped.MountableComponent.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to CVTPulley. Expected: {}.'.format(self.wrapped.MountableComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.MountableComponent.__class__)(self.wrapped.MountableComponent) if self.wrapped.MountableComponent is not None else None

    @property
    def mountable_component_of_type_part_to_part_shear_coupling_half(self) -> '_2314.PartToPartShearCouplingHalf':
        '''PartToPartShearCouplingHalf: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2314.PartToPartShearCouplingHalf.TYPE not in self.wrapped.MountableComponent.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to PartToPartShearCouplingHalf. Expected: {}.'.format(self.wrapped.MountableComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.MountableComponent.__class__)(self.wrapped.MountableComponent) if self.wrapped.MountableComponent is not None else None

    @property
    def mountable_component_of_type_pulley(self) -> '_2315.Pulley':
        '''Pulley: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2315.Pulley.TYPE not in self.wrapped.MountableComponent.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to Pulley. Expected: {}.'.format(self.wrapped.MountableComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.MountableComponent.__class__)(self.wrapped.MountableComponent) if self.wrapped.MountableComponent is not None else None

    @property
    def mountable_component_of_type_rolling_ring(self) -> '_2321.RollingRing':
        '''RollingRing: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2321.RollingRing.TYPE not in self.wrapped.MountableComponent.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to RollingRing. Expected: {}.'.format(self.wrapped.MountableComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.MountableComponent.__class__)(self.wrapped.MountableComponent) if self.wrapped.MountableComponent is not None else None

    @property
    def mountable_component_of_type_shaft_hub_connection(self) -> '_2323.ShaftHubConnection':
        '''ShaftHubConnection: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2323.ShaftHubConnection.TYPE not in self.wrapped.MountableComponent.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to ShaftHubConnection. Expected: {}.'.format(self.wrapped.MountableComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.MountableComponent.__class__)(self.wrapped.MountableComponent) if self.wrapped.MountableComponent is not None else None

    @property
    def mountable_component_of_type_spring_damper_half(self) -> '_2326.SpringDamperHalf':
        '''SpringDamperHalf: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2326.SpringDamperHalf.TYPE not in self.wrapped.MountableComponent.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to SpringDamperHalf. Expected: {}.'.format(self.wrapped.MountableComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.MountableComponent.__class__)(self.wrapped.MountableComponent) if self.wrapped.MountableComponent is not None else None

    @property
    def mountable_component_of_type_synchroniser_half(self) -> '_2329.SynchroniserHalf':
        '''SynchroniserHalf: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2329.SynchroniserHalf.TYPE not in self.wrapped.MountableComponent.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to SynchroniserHalf. Expected: {}.'.format(self.wrapped.MountableComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.MountableComponent.__class__)(self.wrapped.MountableComponent) if self.wrapped.MountableComponent is not None else None

    @property
    def mountable_component_of_type_synchroniser_part(self) -> '_2330.SynchroniserPart':
        '''SynchroniserPart: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2330.SynchroniserPart.TYPE not in self.wrapped.MountableComponent.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to SynchroniserPart. Expected: {}.'.format(self.wrapped.MountableComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.MountableComponent.__class__)(self.wrapped.MountableComponent) if self.wrapped.MountableComponent is not None else None

    @property
    def mountable_component_of_type_synchroniser_sleeve(self) -> '_2331.SynchroniserSleeve':
        '''SynchroniserSleeve: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2331.SynchroniserSleeve.TYPE not in self.wrapped.MountableComponent.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to SynchroniserSleeve. Expected: {}.'.format(self.wrapped.MountableComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.MountableComponent.__class__)(self.wrapped.MountableComponent) if self.wrapped.MountableComponent is not None else None

    @property
    def mountable_component_of_type_torque_converter_pump(self) -> '_2333.TorqueConverterPump':
        '''TorqueConverterPump: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2333.TorqueConverterPump.TYPE not in self.wrapped.MountableComponent.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to TorqueConverterPump. Expected: {}.'.format(self.wrapped.MountableComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.MountableComponent.__class__)(self.wrapped.MountableComponent) if self.wrapped.MountableComponent is not None else None

    @property
    def mountable_component_of_type_torque_converter_turbine(self) -> '_2335.TorqueConverterTurbine':
        '''TorqueConverterTurbine: 'MountableComponent' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2335.TorqueConverterTurbine.TYPE not in self.wrapped.MountableComponent.__class__.__mro__:
            raise CastException('Failed to cast mountable_component to TorqueConverterTurbine. Expected: {}.'.format(self.wrapped.MountableComponent.__class__.__qualname__))

        return constructor.new_override(self.wrapped.MountableComponent.__class__)(self.wrapped.MountableComponent) if self.wrapped.MountableComponent is not None else None

    @property
    def shaft(self) -> '_2163.AbstractShaft':
        '''AbstractShaft: 'Shaft' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2163.AbstractShaft.TYPE not in self.wrapped.Shaft.__class__.__mro__:
            raise CastException('Failed to cast shaft to AbstractShaft. Expected: {}.'.format(self.wrapped.Shaft.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Shaft.__class__)(self.wrapped.Shaft) if self.wrapped.Shaft is not None else None

    @property
    def shaft_of_type_shaft(self) -> '_2208.Shaft':
        '''Shaft: 'Shaft' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2208.Shaft.TYPE not in self.wrapped.Shaft.__class__.__mro__:
            raise CastException('Failed to cast shaft to Shaft. Expected: {}.'.format(self.wrapped.Shaft.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Shaft.__class__)(self.wrapped.Shaft) if self.wrapped.Shaft is not None else None

    @property
    def shaft_of_type_cycloidal_disc(self) -> '_2294.CycloidalDisc':
        '''CycloidalDisc: 'Shaft' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2294.CycloidalDisc.TYPE not in self.wrapped.Shaft.__class__.__mro__:
            raise CastException('Failed to cast shaft to CycloidalDisc. Expected: {}.'.format(self.wrapped.Shaft.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Shaft.__class__)(self.wrapped.Shaft) if self.wrapped.Shaft is not None else None
