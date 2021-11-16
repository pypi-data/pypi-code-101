'''_3622.py

AssemblyCompoundStabilityAnalysis
'''


from typing import List

from mastapy.system_model.part_model import _2161, _2200
from mastapy._internal import constructor, conversion
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.analyses_and_results.stability_analyses import _3490
from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
    _3623, _3625, _3628, _3634,
    _3635, _3636, _3641, _3646,
    _3656, _3658, _3660, _3664,
    _3670, _3671, _3672, _3679,
    _3686, _3689, _3690, _3691,
    _3693, _3695, _3700, _3701,
    _3702, _3711, _3704, _3706,
    _3710, _3716, _3717, _3722,
    _3725, _3728, _3732, _3736,
    _3740, _3743, _3615
)
from mastapy._internal.python_net import python_net_import

_ASSEMBLY_COMPOUND_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound', 'AssemblyCompoundStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('AssemblyCompoundStabilityAnalysis',)


class AssemblyCompoundStabilityAnalysis(_3615.AbstractAssemblyCompoundStabilityAnalysis):
    '''AssemblyCompoundStabilityAnalysis

    This is a mastapy class.
    '''

    TYPE = _ASSEMBLY_COMPOUND_STABILITY_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'AssemblyCompoundStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def assembly_analysis_cases_ready(self) -> 'List[_3490.AssemblyStabilityAnalysis]':
        '''List[AssemblyStabilityAnalysis]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCasesReady, constructor.new(_3490.AssemblyStabilityAnalysis))
        return value

    @property
    def bearings(self) -> 'List[_3623.BearingCompoundStabilityAnalysis]':
        '''List[BearingCompoundStabilityAnalysis]: 'Bearings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bearings, constructor.new(_3623.BearingCompoundStabilityAnalysis))
        return value

    @property
    def belt_drives(self) -> 'List[_3625.BeltDriveCompoundStabilityAnalysis]':
        '''List[BeltDriveCompoundStabilityAnalysis]: 'BeltDrives' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BeltDrives, constructor.new(_3625.BeltDriveCompoundStabilityAnalysis))
        return value

    @property
    def bevel_differential_gear_sets(self) -> 'List[_3628.BevelDifferentialGearSetCompoundStabilityAnalysis]':
        '''List[BevelDifferentialGearSetCompoundStabilityAnalysis]: 'BevelDifferentialGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BevelDifferentialGearSets, constructor.new(_3628.BevelDifferentialGearSetCompoundStabilityAnalysis))
        return value

    @property
    def bolts(self) -> 'List[_3634.BoltCompoundStabilityAnalysis]':
        '''List[BoltCompoundStabilityAnalysis]: 'Bolts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Bolts, constructor.new(_3634.BoltCompoundStabilityAnalysis))
        return value

    @property
    def bolted_joints(self) -> 'List[_3635.BoltedJointCompoundStabilityAnalysis]':
        '''List[BoltedJointCompoundStabilityAnalysis]: 'BoltedJoints' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.BoltedJoints, constructor.new(_3635.BoltedJointCompoundStabilityAnalysis))
        return value

    @property
    def clutches(self) -> 'List[_3636.ClutchCompoundStabilityAnalysis]':
        '''List[ClutchCompoundStabilityAnalysis]: 'Clutches' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Clutches, constructor.new(_3636.ClutchCompoundStabilityAnalysis))
        return value

    @property
    def concept_couplings(self) -> 'List[_3641.ConceptCouplingCompoundStabilityAnalysis]':
        '''List[ConceptCouplingCompoundStabilityAnalysis]: 'ConceptCouplings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptCouplings, constructor.new(_3641.ConceptCouplingCompoundStabilityAnalysis))
        return value

    @property
    def concept_gear_sets(self) -> 'List[_3646.ConceptGearSetCompoundStabilityAnalysis]':
        '''List[ConceptGearSetCompoundStabilityAnalysis]: 'ConceptGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ConceptGearSets, constructor.new(_3646.ConceptGearSetCompoundStabilityAnalysis))
        return value

    @property
    def cv_ts(self) -> 'List[_3656.CVTCompoundStabilityAnalysis]':
        '''List[CVTCompoundStabilityAnalysis]: 'CVTs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CVTs, constructor.new(_3656.CVTCompoundStabilityAnalysis))
        return value

    @property
    def cycloidal_assemblies(self) -> 'List[_3658.CycloidalAssemblyCompoundStabilityAnalysis]':
        '''List[CycloidalAssemblyCompoundStabilityAnalysis]: 'CycloidalAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CycloidalAssemblies, constructor.new(_3658.CycloidalAssemblyCompoundStabilityAnalysis))
        return value

    @property
    def cycloidal_discs(self) -> 'List[_3660.CycloidalDiscCompoundStabilityAnalysis]':
        '''List[CycloidalDiscCompoundStabilityAnalysis]: 'CycloidalDiscs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CycloidalDiscs, constructor.new(_3660.CycloidalDiscCompoundStabilityAnalysis))
        return value

    @property
    def cylindrical_gear_sets(self) -> 'List[_3664.CylindricalGearSetCompoundStabilityAnalysis]':
        '''List[CylindricalGearSetCompoundStabilityAnalysis]: 'CylindricalGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CylindricalGearSets, constructor.new(_3664.CylindricalGearSetCompoundStabilityAnalysis))
        return value

    @property
    def face_gear_sets(self) -> 'List[_3670.FaceGearSetCompoundStabilityAnalysis]':
        '''List[FaceGearSetCompoundStabilityAnalysis]: 'FaceGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FaceGearSets, constructor.new(_3670.FaceGearSetCompoundStabilityAnalysis))
        return value

    @property
    def fe_parts(self) -> 'List[_3671.FEPartCompoundStabilityAnalysis]':
        '''List[FEPartCompoundStabilityAnalysis]: 'FEParts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FEParts, constructor.new(_3671.FEPartCompoundStabilityAnalysis))
        return value

    @property
    def flexible_pin_assemblies(self) -> 'List[_3672.FlexiblePinAssemblyCompoundStabilityAnalysis]':
        '''List[FlexiblePinAssemblyCompoundStabilityAnalysis]: 'FlexiblePinAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.FlexiblePinAssemblies, constructor.new(_3672.FlexiblePinAssemblyCompoundStabilityAnalysis))
        return value

    @property
    def hypoid_gear_sets(self) -> 'List[_3679.HypoidGearSetCompoundStabilityAnalysis]':
        '''List[HypoidGearSetCompoundStabilityAnalysis]: 'HypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.HypoidGearSets, constructor.new(_3679.HypoidGearSetCompoundStabilityAnalysis))
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_sets(self) -> 'List[_3686.KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis]':
        '''List[KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis]: 'KlingelnbergCycloPalloidHypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidHypoidGearSets, constructor.new(_3686.KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis))
        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_sets(self) -> 'List[_3689.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis]':
        '''List[KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis]: 'KlingelnbergCycloPalloidSpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearSets, constructor.new(_3689.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis))
        return value

    @property
    def mass_discs(self) -> 'List[_3690.MassDiscCompoundStabilityAnalysis]':
        '''List[MassDiscCompoundStabilityAnalysis]: 'MassDiscs' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MassDiscs, constructor.new(_3690.MassDiscCompoundStabilityAnalysis))
        return value

    @property
    def measurement_components(self) -> 'List[_3691.MeasurementComponentCompoundStabilityAnalysis]':
        '''List[MeasurementComponentCompoundStabilityAnalysis]: 'MeasurementComponents' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.MeasurementComponents, constructor.new(_3691.MeasurementComponentCompoundStabilityAnalysis))
        return value

    @property
    def oil_seals(self) -> 'List[_3693.OilSealCompoundStabilityAnalysis]':
        '''List[OilSealCompoundStabilityAnalysis]: 'OilSeals' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.OilSeals, constructor.new(_3693.OilSealCompoundStabilityAnalysis))
        return value

    @property
    def part_to_part_shear_couplings(self) -> 'List[_3695.PartToPartShearCouplingCompoundStabilityAnalysis]':
        '''List[PartToPartShearCouplingCompoundStabilityAnalysis]: 'PartToPartShearCouplings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PartToPartShearCouplings, constructor.new(_3695.PartToPartShearCouplingCompoundStabilityAnalysis))
        return value

    @property
    def planet_carriers(self) -> 'List[_3700.PlanetCarrierCompoundStabilityAnalysis]':
        '''List[PlanetCarrierCompoundStabilityAnalysis]: 'PlanetCarriers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PlanetCarriers, constructor.new(_3700.PlanetCarrierCompoundStabilityAnalysis))
        return value

    @property
    def point_loads(self) -> 'List[_3701.PointLoadCompoundStabilityAnalysis]':
        '''List[PointLoadCompoundStabilityAnalysis]: 'PointLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PointLoads, constructor.new(_3701.PointLoadCompoundStabilityAnalysis))
        return value

    @property
    def power_loads(self) -> 'List[_3702.PowerLoadCompoundStabilityAnalysis]':
        '''List[PowerLoadCompoundStabilityAnalysis]: 'PowerLoads' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PowerLoads, constructor.new(_3702.PowerLoadCompoundStabilityAnalysis))
        return value

    @property
    def shaft_hub_connections(self) -> 'List[_3711.ShaftHubConnectionCompoundStabilityAnalysis]':
        '''List[ShaftHubConnectionCompoundStabilityAnalysis]: 'ShaftHubConnections' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ShaftHubConnections, constructor.new(_3711.ShaftHubConnectionCompoundStabilityAnalysis))
        return value

    @property
    def ring_pins(self) -> 'List[_3704.RingPinsCompoundStabilityAnalysis]':
        '''List[RingPinsCompoundStabilityAnalysis]: 'RingPins' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.RingPins, constructor.new(_3704.RingPinsCompoundStabilityAnalysis))
        return value

    @property
    def rolling_ring_assemblies(self) -> 'List[_3706.RollingRingAssemblyCompoundStabilityAnalysis]':
        '''List[RollingRingAssemblyCompoundStabilityAnalysis]: 'RollingRingAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.RollingRingAssemblies, constructor.new(_3706.RollingRingAssemblyCompoundStabilityAnalysis))
        return value

    @property
    def shafts(self) -> 'List[_3710.ShaftCompoundStabilityAnalysis]':
        '''List[ShaftCompoundStabilityAnalysis]: 'Shafts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Shafts, constructor.new(_3710.ShaftCompoundStabilityAnalysis))
        return value

    @property
    def spiral_bevel_gear_sets(self) -> 'List[_3716.SpiralBevelGearSetCompoundStabilityAnalysis]':
        '''List[SpiralBevelGearSetCompoundStabilityAnalysis]: 'SpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpiralBevelGearSets, constructor.new(_3716.SpiralBevelGearSetCompoundStabilityAnalysis))
        return value

    @property
    def spring_dampers(self) -> 'List[_3717.SpringDamperCompoundStabilityAnalysis]':
        '''List[SpringDamperCompoundStabilityAnalysis]: 'SpringDampers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.SpringDampers, constructor.new(_3717.SpringDamperCompoundStabilityAnalysis))
        return value

    @property
    def straight_bevel_diff_gear_sets(self) -> 'List[_3722.StraightBevelDiffGearSetCompoundStabilityAnalysis]':
        '''List[StraightBevelDiffGearSetCompoundStabilityAnalysis]: 'StraightBevelDiffGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelDiffGearSets, constructor.new(_3722.StraightBevelDiffGearSetCompoundStabilityAnalysis))
        return value

    @property
    def straight_bevel_gear_sets(self) -> 'List[_3725.StraightBevelGearSetCompoundStabilityAnalysis]':
        '''List[StraightBevelGearSetCompoundStabilityAnalysis]: 'StraightBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.StraightBevelGearSets, constructor.new(_3725.StraightBevelGearSetCompoundStabilityAnalysis))
        return value

    @property
    def synchronisers(self) -> 'List[_3728.SynchroniserCompoundStabilityAnalysis]':
        '''List[SynchroniserCompoundStabilityAnalysis]: 'Synchronisers' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Synchronisers, constructor.new(_3728.SynchroniserCompoundStabilityAnalysis))
        return value

    @property
    def torque_converters(self) -> 'List[_3732.TorqueConverterCompoundStabilityAnalysis]':
        '''List[TorqueConverterCompoundStabilityAnalysis]: 'TorqueConverters' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.TorqueConverters, constructor.new(_3732.TorqueConverterCompoundStabilityAnalysis))
        return value

    @property
    def unbalanced_masses(self) -> 'List[_3736.UnbalancedMassCompoundStabilityAnalysis]':
        '''List[UnbalancedMassCompoundStabilityAnalysis]: 'UnbalancedMasses' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.UnbalancedMasses, constructor.new(_3736.UnbalancedMassCompoundStabilityAnalysis))
        return value

    @property
    def worm_gear_sets(self) -> 'List[_3740.WormGearSetCompoundStabilityAnalysis]':
        '''List[WormGearSetCompoundStabilityAnalysis]: 'WormGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.WormGearSets, constructor.new(_3740.WormGearSetCompoundStabilityAnalysis))
        return value

    @property
    def zerol_bevel_gear_sets(self) -> 'List[_3743.ZerolBevelGearSetCompoundStabilityAnalysis]':
        '''List[ZerolBevelGearSetCompoundStabilityAnalysis]: 'ZerolBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ZerolBevelGearSets, constructor.new(_3743.ZerolBevelGearSetCompoundStabilityAnalysis))
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_3490.AssemblyStabilityAnalysis]':
        '''List[AssemblyStabilityAnalysis]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCases, constructor.new(_3490.AssemblyStabilityAnalysis))
        return value
