'''_6518.py

AssemblyLoadCase
'''


from typing import List

from mastapy.system_model.part_model import _2161, _2200
from mastapy._internal import constructor, conversion
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.analyses_and_results.static_loads import (
    _6519, _6521, _6524, _6531,
    _6530, _6534, _6539, _6542,
    _6554, _6556, _6558, _6564,
    _6586, _6587, _6588, _6609,
    _6619, _6622, _6623, _6624,
    _6629, _6634, _6638, _6641,
    _6642, _6652, _6646, _6648,
    _6653, _6659, _6662, _6665,
    _6668, _6672, _6677, _6684,
    _6688, _6691, _6508, _6532,
    _6592, _6647, _6506
)
from mastapy._internal.python_net import python_net_import

_ASSEMBLY_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'AssemblyLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('AssemblyLoadCase',)


class AssemblyLoadCase(_6506.AbstractAssemblyLoadCase):
    '''AssemblyLoadCase

    This is a mastapy class.
    '''

    TYPE = _ASSEMBLY_LOAD_CASE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'AssemblyLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2161.Assembly':
        '''Assembly: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2161.Assembly.TYPE not in self.wrapped.AssemblyDesign.__class__.__mro__:
            raise CastException('Failed to cast assembly_design to Assembly. Expected: {}.'.format(self.wrapped.AssemblyDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.AssemblyDesign.__class__)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def bearings(self) -> 'List[_6519.BearingLoadCase]':
        '''List[BearingLoadCase]: 'Bearings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bearings, constructor.new(_6519.BearingLoadCase))
        return value

    @property
    def belt_drives(self) -> 'List[_6521.BeltDriveLoadCase]':
        '''List[BeltDriveLoadCase]: 'BeltDrives' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BeltDrives, constructor.new(_6521.BeltDriveLoadCase))
        return value

    @property
    def bevel_differential_gear_sets(self) -> 'List[_6524.BevelDifferentialGearSetLoadCase]':
        '''List[BevelDifferentialGearSetLoadCase]: 'BevelDifferentialGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BevelDifferentialGearSets, constructor.new(_6524.BevelDifferentialGearSetLoadCase))
        return value

    @property
    def bolts(self) -> 'List[_6531.BoltLoadCase]':
        '''List[BoltLoadCase]: 'Bolts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bolts, constructor.new(_6531.BoltLoadCase))
        return value

    @property
    def bolted_joints(self) -> 'List[_6530.BoltedJointLoadCase]':
        '''List[BoltedJointLoadCase]: 'BoltedJoints' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BoltedJoints, constructor.new(_6530.BoltedJointLoadCase))
        return value

    @property
    def clutches(self) -> 'List[_6534.ClutchLoadCase]':
        '''List[ClutchLoadCase]: 'Clutches' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Clutches, constructor.new(_6534.ClutchLoadCase))
        return value

    @property
    def concept_couplings(self) -> 'List[_6539.ConceptCouplingLoadCase]':
        '''List[ConceptCouplingLoadCase]: 'ConceptCouplings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptCouplings, constructor.new(_6539.ConceptCouplingLoadCase))
        return value

    @property
    def concept_gear_sets(self) -> 'List[_6542.ConceptGearSetLoadCase]':
        '''List[ConceptGearSetLoadCase]: 'ConceptGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptGearSets, constructor.new(_6542.ConceptGearSetLoadCase))
        return value

    @property
    def cv_ts(self) -> 'List[_6554.CVTLoadCase]':
        '''List[CVTLoadCase]: 'CVTs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CVTs, constructor.new(_6554.CVTLoadCase))
        return value

    @property
    def cycloidal_assemblies(self) -> 'List[_6556.CycloidalAssemblyLoadCase]':
        '''List[CycloidalAssemblyLoadCase]: 'CycloidalAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CycloidalAssemblies, constructor.new(_6556.CycloidalAssemblyLoadCase))
        return value

    @property
    def cycloidal_discs(self) -> 'List[_6558.CycloidalDiscLoadCase]':
        '''List[CycloidalDiscLoadCase]: 'CycloidalDiscs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CycloidalDiscs, constructor.new(_6558.CycloidalDiscLoadCase))
        return value

    @property
    def cylindrical_gear_sets(self) -> 'List[_6564.CylindricalGearSetLoadCase]':
        '''List[CylindricalGearSetLoadCase]: 'CylindricalGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CylindricalGearSets, constructor.new(_6564.CylindricalGearSetLoadCase))
        return value

    @property
    def face_gear_sets(self) -> 'List[_6586.FaceGearSetLoadCase]':
        '''List[FaceGearSetLoadCase]: 'FaceGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FaceGearSets, constructor.new(_6586.FaceGearSetLoadCase))
        return value

    @property
    def fe_parts(self) -> 'List[_6587.FEPartLoadCase]':
        '''List[FEPartLoadCase]: 'FEParts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FEParts, constructor.new(_6587.FEPartLoadCase))
        return value

    @property
    def flexible_pin_assemblies(self) -> 'List[_6588.FlexiblePinAssemblyLoadCase]':
        '''List[FlexiblePinAssemblyLoadCase]: 'FlexiblePinAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FlexiblePinAssemblies, constructor.new(_6588.FlexiblePinAssemblyLoadCase))
        return value

    @property
    def hypoid_gear_sets(self) -> 'List[_6609.HypoidGearSetLoadCase]':
        '''List[HypoidGearSetLoadCase]: 'HypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.HypoidGearSets, constructor.new(_6609.HypoidGearSetLoadCase))
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_sets(self) -> 'List[_6619.KlingelnbergCycloPalloidHypoidGearSetLoadCase]':
        '''List[KlingelnbergCycloPalloidHypoidGearSetLoadCase]: 'KlingelnbergCycloPalloidHypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidHypoidGearSets, constructor.new(_6619.KlingelnbergCycloPalloidHypoidGearSetLoadCase))
        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_sets(self) -> 'List[_6622.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase]':
        '''List[KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase]: 'KlingelnbergCycloPalloidSpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearSets, constructor.new(_6622.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase))
        return value

    @property
    def mass_discs(self) -> 'List[_6623.MassDiscLoadCase]':
        '''List[MassDiscLoadCase]: 'MassDiscs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MassDiscs, constructor.new(_6623.MassDiscLoadCase))
        return value

    @property
    def measurement_components(self) -> 'List[_6624.MeasurementComponentLoadCase]':
        '''List[MeasurementComponentLoadCase]: 'MeasurementComponents' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MeasurementComponents, constructor.new(_6624.MeasurementComponentLoadCase))
        return value

    @property
    def oil_seals(self) -> 'List[_6629.OilSealLoadCase]':
        '''List[OilSealLoadCase]: 'OilSeals' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.OilSeals, constructor.new(_6629.OilSealLoadCase))
        return value

    @property
    def part_to_part_shear_couplings(self) -> 'List[_6634.PartToPartShearCouplingLoadCase]':
        '''List[PartToPartShearCouplingLoadCase]: 'PartToPartShearCouplings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PartToPartShearCouplings, constructor.new(_6634.PartToPartShearCouplingLoadCase))
        return value

    @property
    def planet_carriers(self) -> 'List[_6638.PlanetCarrierLoadCase]':
        '''List[PlanetCarrierLoadCase]: 'PlanetCarriers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PlanetCarriers, constructor.new(_6638.PlanetCarrierLoadCase))
        return value

    @property
    def point_loads(self) -> 'List[_6641.PointLoadLoadCase]':
        '''List[PointLoadLoadCase]: 'PointLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PointLoads, constructor.new(_6641.PointLoadLoadCase))
        return value

    @property
    def power_loads(self) -> 'List[_6642.PowerLoadLoadCase]':
        '''List[PowerLoadLoadCase]: 'PowerLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PowerLoads, constructor.new(_6642.PowerLoadLoadCase))
        return value

    @property
    def shaft_hub_connections(self) -> 'List[_6652.ShaftHubConnectionLoadCase]':
        '''List[ShaftHubConnectionLoadCase]: 'ShaftHubConnections' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ShaftHubConnections, constructor.new(_6652.ShaftHubConnectionLoadCase))
        return value

    @property
    def ring_pins(self) -> 'List[_6646.RingPinsLoadCase]':
        '''List[RingPinsLoadCase]: 'RingPins' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.RingPins, constructor.new(_6646.RingPinsLoadCase))
        return value

    @property
    def rolling_ring_assemblies(self) -> 'List[_6648.RollingRingAssemblyLoadCase]':
        '''List[RollingRingAssemblyLoadCase]: 'RollingRingAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.RollingRingAssemblies, constructor.new(_6648.RollingRingAssemblyLoadCase))
        return value

    @property
    def shafts(self) -> 'List[_6653.ShaftLoadCase]':
        '''List[ShaftLoadCase]: 'Shafts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Shafts, constructor.new(_6653.ShaftLoadCase))
        return value

    @property
    def spiral_bevel_gear_sets(self) -> 'List[_6659.SpiralBevelGearSetLoadCase]':
        '''List[SpiralBevelGearSetLoadCase]: 'SpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpiralBevelGearSets, constructor.new(_6659.SpiralBevelGearSetLoadCase))
        return value

    @property
    def spring_dampers(self) -> 'List[_6662.SpringDamperLoadCase]':
        '''List[SpringDamperLoadCase]: 'SpringDampers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpringDampers, constructor.new(_6662.SpringDamperLoadCase))
        return value

    @property
    def straight_bevel_diff_gear_sets(self) -> 'List[_6665.StraightBevelDiffGearSetLoadCase]':
        '''List[StraightBevelDiffGearSetLoadCase]: 'StraightBevelDiffGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelDiffGearSets, constructor.new(_6665.StraightBevelDiffGearSetLoadCase))
        return value

    @property
    def straight_bevel_gear_sets(self) -> 'List[_6668.StraightBevelGearSetLoadCase]':
        '''List[StraightBevelGearSetLoadCase]: 'StraightBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelGearSets, constructor.new(_6668.StraightBevelGearSetLoadCase))
        return value

    @property
    def synchronisers(self) -> 'List[_6672.SynchroniserLoadCase]':
        '''List[SynchroniserLoadCase]: 'Synchronisers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Synchronisers, constructor.new(_6672.SynchroniserLoadCase))
        return value

    @property
    def torque_converters(self) -> 'List[_6677.TorqueConverterLoadCase]':
        '''List[TorqueConverterLoadCase]: 'TorqueConverters' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.TorqueConverters, constructor.new(_6677.TorqueConverterLoadCase))
        return value

    @property
    def unbalanced_masses(self) -> 'List[_6684.UnbalancedMassLoadCase]':
        '''List[UnbalancedMassLoadCase]: 'UnbalancedMasses' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.UnbalancedMasses, constructor.new(_6684.UnbalancedMassLoadCase))
        return value

    @property
    def worm_gear_sets(self) -> 'List[_6688.WormGearSetLoadCase]':
        '''List[WormGearSetLoadCase]: 'WormGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.WormGearSets, constructor.new(_6688.WormGearSetLoadCase))
        return value

    @property
    def zerol_bevel_gear_sets(self) -> 'List[_6691.ZerolBevelGearSetLoadCase]':
        '''List[ZerolBevelGearSetLoadCase]: 'ZerolBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ZerolBevelGearSets, constructor.new(_6691.ZerolBevelGearSetLoadCase))
        return value

    @property
    def shafts_and_housings(self) -> 'List[_6508.AbstractShaftOrHousingLoadCase]':
        '''List[AbstractShaftOrHousingLoadCase]: 'ShaftsAndHousings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ShaftsAndHousings, constructor.new(_6508.AbstractShaftOrHousingLoadCase))
        return value

    @property
    def clutch_connections(self) -> 'List[_6532.ClutchConnectionLoadCase]':
        '''List[ClutchConnectionLoadCase]: 'ClutchConnections' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ClutchConnections, constructor.new(_6532.ClutchConnectionLoadCase))
        return value

    @property
    def gear_meshes(self) -> 'List[_6592.GearMeshLoadCase]':
        '''List[GearMeshLoadCase]: 'GearMeshes' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.GearMeshes, constructor.new(_6592.GearMeshLoadCase))
        return value

    @property
    def ring_pins_to_cycloidal_disc_connections(self) -> 'List[_6647.RingPinsToDiscConnectionLoadCase]':
        '''List[RingPinsToDiscConnectionLoadCase]: 'RingPinsToCycloidalDiscConnections' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.RingPinsToCycloidalDiscConnections, constructor.new(_6647.RingPinsToDiscConnectionLoadCase))
        return value
