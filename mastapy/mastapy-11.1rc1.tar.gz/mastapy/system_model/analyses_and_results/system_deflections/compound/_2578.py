'''_2578.py

AssemblyCompoundSystemDeflection
'''


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model import _2161, _2200
from mastapy._internal.cast_exception import CastException
from mastapy.nodal_analysis import _47
from mastapy.shafts import _37
from mastapy.gears.analysis import _1166
from mastapy.system_model.analyses_and_results.system_deflections import _2417
from mastapy.system_model.analyses_and_results.system_deflections.compound import (
    _2579, _2581, _2584, _2590,
    _2591, _2592, _2597, _2602,
    _2612, _2614, _2616, _2620,
    _2627, _2628, _2629, _2636,
    _2643, _2646, _2647, _2648,
    _2650, _2652, _2657, _2658,
    _2659, _2669, _2661, _2663,
    _2667, _2674, _2675, _2680,
    _2683, _2686, _2690, _2694,
    _2698, _2701, _2571
)
from mastapy._internal.python_net import python_net_import

_ASSEMBLY_COMPOUND_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound', 'AssemblyCompoundSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('AssemblyCompoundSystemDeflection',)


class AssemblyCompoundSystemDeflection(_2571.AbstractAssemblyCompoundSystemDeflection):
    '''AssemblyCompoundSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _ASSEMBLY_COMPOUND_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'AssemblyCompoundSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def overall_duty_cycle_shaft_reliability(self) -> 'float':
        '''float: 'OverallDutyCycleShaftReliability' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.OverallDutyCycleShaftReliability

    @property
    def overall_duty_cycle_bearing_reliability(self) -> 'float':
        '''float: 'OverallDutyCycleBearingReliability' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.OverallDutyCycleBearingReliability

    @property
    def overall_duty_cycle_gear_reliability(self) -> 'float':
        '''float: 'OverallDutyCycleGearReliability' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.OverallDutyCycleGearReliability

    @property
    def overall_oil_seal_duty_cycle_reliability(self) -> 'float':
        '''float: 'OverallOilSealDutyCycleReliability' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.OverallOilSealDutyCycleReliability

    @property
    def overall_system_reliability(self) -> 'float':
        '''float: 'OverallSystemReliability' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.OverallSystemReliability

    @property
    def component_design(self) -> '_2161.Assembly':
        '''Assembly: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2161.Assembly.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to Assembly. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

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
    def analysis_settings(self) -> '_47.AnalysisSettingsObjects':
        '''AnalysisSettingsObjects: 'AnalysisSettings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_47.AnalysisSettingsObjects)(self.wrapped.AnalysisSettings) if self.wrapped.AnalysisSettings is not None else None

    @property
    def shaft_settings(self) -> '_37.ShaftSettings':
        '''ShaftSettings: 'ShaftSettings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_37.ShaftSettings)(self.wrapped.ShaftSettings) if self.wrapped.ShaftSettings is not None else None

    @property
    def rating_for_all_gear_sets(self) -> '_1166.GearSetGroupDutyCycle':
        '''GearSetGroupDutyCycle: 'RatingForAllGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_1166.GearSetGroupDutyCycle)(self.wrapped.RatingForAllGearSets) if self.wrapped.RatingForAllGearSets is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_2417.AssemblySystemDeflection]':
        '''List[AssemblySystemDeflection]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCasesReady, constructor.new(_2417.AssemblySystemDeflection))
        return value

    @property
    def bearings(self) -> 'List[_2579.BearingCompoundSystemDeflection]':
        '''List[BearingCompoundSystemDeflection]: 'Bearings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bearings, constructor.new(_2579.BearingCompoundSystemDeflection))
        return value

    @property
    def belt_drives(self) -> 'List[_2581.BeltDriveCompoundSystemDeflection]':
        '''List[BeltDriveCompoundSystemDeflection]: 'BeltDrives' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BeltDrives, constructor.new(_2581.BeltDriveCompoundSystemDeflection))
        return value

    @property
    def bevel_differential_gear_sets(self) -> 'List[_2584.BevelDifferentialGearSetCompoundSystemDeflection]':
        '''List[BevelDifferentialGearSetCompoundSystemDeflection]: 'BevelDifferentialGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BevelDifferentialGearSets, constructor.new(_2584.BevelDifferentialGearSetCompoundSystemDeflection))
        return value

    @property
    def bolts(self) -> 'List[_2590.BoltCompoundSystemDeflection]':
        '''List[BoltCompoundSystemDeflection]: 'Bolts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bolts, constructor.new(_2590.BoltCompoundSystemDeflection))
        return value

    @property
    def bolted_joints(self) -> 'List[_2591.BoltedJointCompoundSystemDeflection]':
        '''List[BoltedJointCompoundSystemDeflection]: 'BoltedJoints' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BoltedJoints, constructor.new(_2591.BoltedJointCompoundSystemDeflection))
        return value

    @property
    def clutches(self) -> 'List[_2592.ClutchCompoundSystemDeflection]':
        '''List[ClutchCompoundSystemDeflection]: 'Clutches' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Clutches, constructor.new(_2592.ClutchCompoundSystemDeflection))
        return value

    @property
    def concept_couplings(self) -> 'List[_2597.ConceptCouplingCompoundSystemDeflection]':
        '''List[ConceptCouplingCompoundSystemDeflection]: 'ConceptCouplings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptCouplings, constructor.new(_2597.ConceptCouplingCompoundSystemDeflection))
        return value

    @property
    def concept_gear_sets(self) -> 'List[_2602.ConceptGearSetCompoundSystemDeflection]':
        '''List[ConceptGearSetCompoundSystemDeflection]: 'ConceptGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptGearSets, constructor.new(_2602.ConceptGearSetCompoundSystemDeflection))
        return value

    @property
    def cv_ts(self) -> 'List[_2612.CVTCompoundSystemDeflection]':
        '''List[CVTCompoundSystemDeflection]: 'CVTs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CVTs, constructor.new(_2612.CVTCompoundSystemDeflection))
        return value

    @property
    def cycloidal_assemblies(self) -> 'List[_2614.CycloidalAssemblyCompoundSystemDeflection]':
        '''List[CycloidalAssemblyCompoundSystemDeflection]: 'CycloidalAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CycloidalAssemblies, constructor.new(_2614.CycloidalAssemblyCompoundSystemDeflection))
        return value

    @property
    def cycloidal_discs(self) -> 'List[_2616.CycloidalDiscCompoundSystemDeflection]':
        '''List[CycloidalDiscCompoundSystemDeflection]: 'CycloidalDiscs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CycloidalDiscs, constructor.new(_2616.CycloidalDiscCompoundSystemDeflection))
        return value

    @property
    def cylindrical_gear_sets(self) -> 'List[_2620.CylindricalGearSetCompoundSystemDeflection]':
        '''List[CylindricalGearSetCompoundSystemDeflection]: 'CylindricalGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CylindricalGearSets, constructor.new(_2620.CylindricalGearSetCompoundSystemDeflection))
        return value

    @property
    def face_gear_sets(self) -> 'List[_2627.FaceGearSetCompoundSystemDeflection]':
        '''List[FaceGearSetCompoundSystemDeflection]: 'FaceGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FaceGearSets, constructor.new(_2627.FaceGearSetCompoundSystemDeflection))
        return value

    @property
    def fe_parts(self) -> 'List[_2628.FEPartCompoundSystemDeflection]':
        '''List[FEPartCompoundSystemDeflection]: 'FEParts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FEParts, constructor.new(_2628.FEPartCompoundSystemDeflection))
        return value

    @property
    def flexible_pin_assemblies(self) -> 'List[_2629.FlexiblePinAssemblyCompoundSystemDeflection]':
        '''List[FlexiblePinAssemblyCompoundSystemDeflection]: 'FlexiblePinAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FlexiblePinAssemblies, constructor.new(_2629.FlexiblePinAssemblyCompoundSystemDeflection))
        return value

    @property
    def hypoid_gear_sets(self) -> 'List[_2636.HypoidGearSetCompoundSystemDeflection]':
        '''List[HypoidGearSetCompoundSystemDeflection]: 'HypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.HypoidGearSets, constructor.new(_2636.HypoidGearSetCompoundSystemDeflection))
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_sets(self) -> 'List[_2643.KlingelnbergCycloPalloidHypoidGearSetCompoundSystemDeflection]':
        '''List[KlingelnbergCycloPalloidHypoidGearSetCompoundSystemDeflection]: 'KlingelnbergCycloPalloidHypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidHypoidGearSets, constructor.new(_2643.KlingelnbergCycloPalloidHypoidGearSetCompoundSystemDeflection))
        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_sets(self) -> 'List[_2646.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection]':
        '''List[KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection]: 'KlingelnbergCycloPalloidSpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearSets, constructor.new(_2646.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection))
        return value

    @property
    def mass_discs(self) -> 'List[_2647.MassDiscCompoundSystemDeflection]':
        '''List[MassDiscCompoundSystemDeflection]: 'MassDiscs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MassDiscs, constructor.new(_2647.MassDiscCompoundSystemDeflection))
        return value

    @property
    def measurement_components(self) -> 'List[_2648.MeasurementComponentCompoundSystemDeflection]':
        '''List[MeasurementComponentCompoundSystemDeflection]: 'MeasurementComponents' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MeasurementComponents, constructor.new(_2648.MeasurementComponentCompoundSystemDeflection))
        return value

    @property
    def oil_seals(self) -> 'List[_2650.OilSealCompoundSystemDeflection]':
        '''List[OilSealCompoundSystemDeflection]: 'OilSeals' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.OilSeals, constructor.new(_2650.OilSealCompoundSystemDeflection))
        return value

    @property
    def part_to_part_shear_couplings(self) -> 'List[_2652.PartToPartShearCouplingCompoundSystemDeflection]':
        '''List[PartToPartShearCouplingCompoundSystemDeflection]: 'PartToPartShearCouplings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PartToPartShearCouplings, constructor.new(_2652.PartToPartShearCouplingCompoundSystemDeflection))
        return value

    @property
    def planet_carriers(self) -> 'List[_2657.PlanetCarrierCompoundSystemDeflection]':
        '''List[PlanetCarrierCompoundSystemDeflection]: 'PlanetCarriers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PlanetCarriers, constructor.new(_2657.PlanetCarrierCompoundSystemDeflection))
        return value

    @property
    def point_loads(self) -> 'List[_2658.PointLoadCompoundSystemDeflection]':
        '''List[PointLoadCompoundSystemDeflection]: 'PointLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PointLoads, constructor.new(_2658.PointLoadCompoundSystemDeflection))
        return value

    @property
    def power_loads(self) -> 'List[_2659.PowerLoadCompoundSystemDeflection]':
        '''List[PowerLoadCompoundSystemDeflection]: 'PowerLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PowerLoads, constructor.new(_2659.PowerLoadCompoundSystemDeflection))
        return value

    @property
    def shaft_hub_connections(self) -> 'List[_2669.ShaftHubConnectionCompoundSystemDeflection]':
        '''List[ShaftHubConnectionCompoundSystemDeflection]: 'ShaftHubConnections' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ShaftHubConnections, constructor.new(_2669.ShaftHubConnectionCompoundSystemDeflection))
        return value

    @property
    def ring_pins(self) -> 'List[_2661.RingPinsCompoundSystemDeflection]':
        '''List[RingPinsCompoundSystemDeflection]: 'RingPins' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.RingPins, constructor.new(_2661.RingPinsCompoundSystemDeflection))
        return value

    @property
    def rolling_ring_assemblies(self) -> 'List[_2663.RollingRingAssemblyCompoundSystemDeflection]':
        '''List[RollingRingAssemblyCompoundSystemDeflection]: 'RollingRingAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.RollingRingAssemblies, constructor.new(_2663.RollingRingAssemblyCompoundSystemDeflection))
        return value

    @property
    def shafts(self) -> 'List[_2667.ShaftCompoundSystemDeflection]':
        '''List[ShaftCompoundSystemDeflection]: 'Shafts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Shafts, constructor.new(_2667.ShaftCompoundSystemDeflection))
        return value

    @property
    def spiral_bevel_gear_sets(self) -> 'List[_2674.SpiralBevelGearSetCompoundSystemDeflection]':
        '''List[SpiralBevelGearSetCompoundSystemDeflection]: 'SpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpiralBevelGearSets, constructor.new(_2674.SpiralBevelGearSetCompoundSystemDeflection))
        return value

    @property
    def spring_dampers(self) -> 'List[_2675.SpringDamperCompoundSystemDeflection]':
        '''List[SpringDamperCompoundSystemDeflection]: 'SpringDampers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpringDampers, constructor.new(_2675.SpringDamperCompoundSystemDeflection))
        return value

    @property
    def straight_bevel_diff_gear_sets(self) -> 'List[_2680.StraightBevelDiffGearSetCompoundSystemDeflection]':
        '''List[StraightBevelDiffGearSetCompoundSystemDeflection]: 'StraightBevelDiffGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelDiffGearSets, constructor.new(_2680.StraightBevelDiffGearSetCompoundSystemDeflection))
        return value

    @property
    def straight_bevel_gear_sets(self) -> 'List[_2683.StraightBevelGearSetCompoundSystemDeflection]':
        '''List[StraightBevelGearSetCompoundSystemDeflection]: 'StraightBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelGearSets, constructor.new(_2683.StraightBevelGearSetCompoundSystemDeflection))
        return value

    @property
    def synchronisers(self) -> 'List[_2686.SynchroniserCompoundSystemDeflection]':
        '''List[SynchroniserCompoundSystemDeflection]: 'Synchronisers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Synchronisers, constructor.new(_2686.SynchroniserCompoundSystemDeflection))
        return value

    @property
    def torque_converters(self) -> 'List[_2690.TorqueConverterCompoundSystemDeflection]':
        '''List[TorqueConverterCompoundSystemDeflection]: 'TorqueConverters' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.TorqueConverters, constructor.new(_2690.TorqueConverterCompoundSystemDeflection))
        return value

    @property
    def unbalanced_masses(self) -> 'List[_2694.UnbalancedMassCompoundSystemDeflection]':
        '''List[UnbalancedMassCompoundSystemDeflection]: 'UnbalancedMasses' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.UnbalancedMasses, constructor.new(_2694.UnbalancedMassCompoundSystemDeflection))
        return value

    @property
    def worm_gear_sets(self) -> 'List[_2698.WormGearSetCompoundSystemDeflection]':
        '''List[WormGearSetCompoundSystemDeflection]: 'WormGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.WormGearSets, constructor.new(_2698.WormGearSetCompoundSystemDeflection))
        return value

    @property
    def zerol_bevel_gear_sets(self) -> 'List[_2701.ZerolBevelGearSetCompoundSystemDeflection]':
        '''List[ZerolBevelGearSetCompoundSystemDeflection]: 'ZerolBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ZerolBevelGearSets, constructor.new(_2701.ZerolBevelGearSetCompoundSystemDeflection))
        return value

    @property
    def rolling_bearings(self) -> 'List[_2579.BearingCompoundSystemDeflection]':
        '''List[BearingCompoundSystemDeflection]: 'RollingBearings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.RollingBearings, constructor.new(_2579.BearingCompoundSystemDeflection))
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_2417.AssemblySystemDeflection]':
        '''List[AssemblySystemDeflection]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCases, constructor.new(_2417.AssemblySystemDeflection))
        return value
