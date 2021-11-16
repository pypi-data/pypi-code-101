'''_5387.py

PartStaticLoadCaseGroup
'''


from typing import List

from mastapy.system_model.part_model import (
    _2194, _2161, _2162, _2163,
    _2164, _2167, _2169, _2170,
    _2171, _2174, _2175, _2178,
    _2179, _2180, _2181, _2188,
    _2189, _2190, _2192, _2195,
    _2197, _2198, _2200, _2202,
    _2203, _2205
)
from mastapy._internal import constructor, conversion
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.part_model.shaft_model import _2208
from mastapy.system_model.part_model.gears import (
    _2238, _2239, _2240, _2241,
    _2242, _2243, _2244, _2245,
    _2246, _2247, _2248, _2249,
    _2250, _2251, _2252, _2253,
    _2254, _2255, _2257, _2259,
    _2260, _2261, _2262, _2263,
    _2264, _2265, _2266, _2267,
    _2268, _2269, _2270, _2271,
    _2272, _2273, _2274, _2275,
    _2276, _2277, _2278, _2279
)
from mastapy.system_model.part_model.cycloidal import _2293, _2294, _2295
from mastapy.system_model.part_model.couplings import (
    _2301, _2303, _2304, _2306,
    _2307, _2308, _2309, _2311,
    _2312, _2313, _2314, _2315,
    _2321, _2322, _2323, _2325,
    _2326, _2327, _2329, _2330,
    _2331, _2332, _2333, _2335
)
from mastapy.system_model.analyses_and_results.static_loads import _6631
from mastapy.system_model.analyses_and_results.load_case_groups.design_entity_static_load_case_groups import _5385
from mastapy._internal.python_net import python_net_import

_PART_STATIC_LOAD_CASE_GROUP = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.LoadCaseGroups.DesignEntityStaticLoadCaseGroups', 'PartStaticLoadCaseGroup')


__docformat__ = 'restructuredtext en'
__all__ = ('PartStaticLoadCaseGroup',)


class PartStaticLoadCaseGroup(_5385.DesignEntityStaticLoadCaseGroup):
    '''PartStaticLoadCaseGroup

    This is a mastapy class.
    '''

    TYPE = _PART_STATIC_LOAD_CASE_GROUP

    __hash__ = None

    def __init__(self, instance_to_wrap: 'PartStaticLoadCaseGroup.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def part(self) -> '_2194.Part':
        '''Part: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2194.Part.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to Part. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_assembly(self) -> '_2161.Assembly':
        '''Assembly: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2161.Assembly.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to Assembly. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_abstract_assembly(self) -> '_2162.AbstractAssembly':
        '''AbstractAssembly: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2162.AbstractAssembly.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to AbstractAssembly. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_abstract_shaft(self) -> '_2163.AbstractShaft':
        '''AbstractShaft: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2163.AbstractShaft.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to AbstractShaft. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_abstract_shaft_or_housing(self) -> '_2164.AbstractShaftOrHousing':
        '''AbstractShaftOrHousing: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2164.AbstractShaftOrHousing.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to AbstractShaftOrHousing. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_bearing(self) -> '_2167.Bearing':
        '''Bearing: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2167.Bearing.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to Bearing. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_bolt(self) -> '_2169.Bolt':
        '''Bolt: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2169.Bolt.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to Bolt. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_bolted_joint(self) -> '_2170.BoltedJoint':
        '''BoltedJoint: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2170.BoltedJoint.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to BoltedJoint. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_component(self) -> '_2171.Component':
        '''Component: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2171.Component.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to Component. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_connector(self) -> '_2174.Connector':
        '''Connector: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2174.Connector.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to Connector. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_datum(self) -> '_2175.Datum':
        '''Datum: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2175.Datum.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to Datum. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_external_cad_model(self) -> '_2178.ExternalCADModel':
        '''ExternalCADModel: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2178.ExternalCADModel.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to ExternalCADModel. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_fe_part(self) -> '_2179.FEPart':
        '''FEPart: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2179.FEPart.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to FEPart. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_flexible_pin_assembly(self) -> '_2180.FlexiblePinAssembly':
        '''FlexiblePinAssembly: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2180.FlexiblePinAssembly.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to FlexiblePinAssembly. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_guide_dxf_model(self) -> '_2181.GuideDxfModel':
        '''GuideDxfModel: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2181.GuideDxfModel.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to GuideDxfModel. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_mass_disc(self) -> '_2188.MassDisc':
        '''MassDisc: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2188.MassDisc.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to MassDisc. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_measurement_component(self) -> '_2189.MeasurementComponent':
        '''MeasurementComponent: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2189.MeasurementComponent.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to MeasurementComponent. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_mountable_component(self) -> '_2190.MountableComponent':
        '''MountableComponent: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2190.MountableComponent.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to MountableComponent. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_oil_seal(self) -> '_2192.OilSeal':
        '''OilSeal: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2192.OilSeal.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to OilSeal. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_planet_carrier(self) -> '_2195.PlanetCarrier':
        '''PlanetCarrier: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2195.PlanetCarrier.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to PlanetCarrier. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_point_load(self) -> '_2197.PointLoad':
        '''PointLoad: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2197.PointLoad.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to PointLoad. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_power_load(self) -> '_2198.PowerLoad':
        '''PowerLoad: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2198.PowerLoad.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to PowerLoad. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_root_assembly(self) -> '_2200.RootAssembly':
        '''RootAssembly: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2200.RootAssembly.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to RootAssembly. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_specialised_assembly(self) -> '_2202.SpecialisedAssembly':
        '''SpecialisedAssembly: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2202.SpecialisedAssembly.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to SpecialisedAssembly. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_unbalanced_mass(self) -> '_2203.UnbalancedMass':
        '''UnbalancedMass: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2203.UnbalancedMass.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to UnbalancedMass. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_virtual_component(self) -> '_2205.VirtualComponent':
        '''VirtualComponent: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2205.VirtualComponent.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to VirtualComponent. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_shaft(self) -> '_2208.Shaft':
        '''Shaft: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2208.Shaft.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to Shaft. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_agma_gleason_conical_gear(self) -> '_2238.AGMAGleasonConicalGear':
        '''AGMAGleasonConicalGear: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2238.AGMAGleasonConicalGear.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to AGMAGleasonConicalGear. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_agma_gleason_conical_gear_set(self) -> '_2239.AGMAGleasonConicalGearSet':
        '''AGMAGleasonConicalGearSet: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2239.AGMAGleasonConicalGearSet.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to AGMAGleasonConicalGearSet. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_bevel_differential_gear(self) -> '_2240.BevelDifferentialGear':
        '''BevelDifferentialGear: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2240.BevelDifferentialGear.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to BevelDifferentialGear. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_bevel_differential_gear_set(self) -> '_2241.BevelDifferentialGearSet':
        '''BevelDifferentialGearSet: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2241.BevelDifferentialGearSet.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to BevelDifferentialGearSet. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_bevel_differential_planet_gear(self) -> '_2242.BevelDifferentialPlanetGear':
        '''BevelDifferentialPlanetGear: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2242.BevelDifferentialPlanetGear.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to BevelDifferentialPlanetGear. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_bevel_differential_sun_gear(self) -> '_2243.BevelDifferentialSunGear':
        '''BevelDifferentialSunGear: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2243.BevelDifferentialSunGear.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to BevelDifferentialSunGear. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_bevel_gear(self) -> '_2244.BevelGear':
        '''BevelGear: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2244.BevelGear.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to BevelGear. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_bevel_gear_set(self) -> '_2245.BevelGearSet':
        '''BevelGearSet: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2245.BevelGearSet.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to BevelGearSet. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_concept_gear(self) -> '_2246.ConceptGear':
        '''ConceptGear: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2246.ConceptGear.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to ConceptGear. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_concept_gear_set(self) -> '_2247.ConceptGearSet':
        '''ConceptGearSet: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2247.ConceptGearSet.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to ConceptGearSet. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_conical_gear(self) -> '_2248.ConicalGear':
        '''ConicalGear: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2248.ConicalGear.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to ConicalGear. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_conical_gear_set(self) -> '_2249.ConicalGearSet':
        '''ConicalGearSet: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2249.ConicalGearSet.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to ConicalGearSet. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_cylindrical_gear(self) -> '_2250.CylindricalGear':
        '''CylindricalGear: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2250.CylindricalGear.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to CylindricalGear. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_cylindrical_gear_set(self) -> '_2251.CylindricalGearSet':
        '''CylindricalGearSet: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2251.CylindricalGearSet.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to CylindricalGearSet. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_cylindrical_planet_gear(self) -> '_2252.CylindricalPlanetGear':
        '''CylindricalPlanetGear: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2252.CylindricalPlanetGear.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to CylindricalPlanetGear. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_face_gear(self) -> '_2253.FaceGear':
        '''FaceGear: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2253.FaceGear.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to FaceGear. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_face_gear_set(self) -> '_2254.FaceGearSet':
        '''FaceGearSet: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2254.FaceGearSet.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to FaceGearSet. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_gear(self) -> '_2255.Gear':
        '''Gear: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2255.Gear.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to Gear. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_gear_set(self) -> '_2257.GearSet':
        '''GearSet: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2257.GearSet.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to GearSet. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_hypoid_gear(self) -> '_2259.HypoidGear':
        '''HypoidGear: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2259.HypoidGear.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to HypoidGear. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_hypoid_gear_set(self) -> '_2260.HypoidGearSet':
        '''HypoidGearSet: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2260.HypoidGearSet.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to HypoidGearSet. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_klingelnberg_cyclo_palloid_conical_gear(self) -> '_2261.KlingelnbergCycloPalloidConicalGear':
        '''KlingelnbergCycloPalloidConicalGear: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2261.KlingelnbergCycloPalloidConicalGear.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to KlingelnbergCycloPalloidConicalGear. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_klingelnberg_cyclo_palloid_conical_gear_set(self) -> '_2262.KlingelnbergCycloPalloidConicalGearSet':
        '''KlingelnbergCycloPalloidConicalGearSet: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2262.KlingelnbergCycloPalloidConicalGearSet.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to KlingelnbergCycloPalloidConicalGearSet. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_klingelnberg_cyclo_palloid_hypoid_gear(self) -> '_2263.KlingelnbergCycloPalloidHypoidGear':
        '''KlingelnbergCycloPalloidHypoidGear: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2263.KlingelnbergCycloPalloidHypoidGear.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to KlingelnbergCycloPalloidHypoidGear. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_klingelnberg_cyclo_palloid_hypoid_gear_set(self) -> '_2264.KlingelnbergCycloPalloidHypoidGearSet':
        '''KlingelnbergCycloPalloidHypoidGearSet: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2264.KlingelnbergCycloPalloidHypoidGearSet.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to KlingelnbergCycloPalloidHypoidGearSet. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear(self) -> '_2265.KlingelnbergCycloPalloidSpiralBevelGear':
        '''KlingelnbergCycloPalloidSpiralBevelGear: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2265.KlingelnbergCycloPalloidSpiralBevelGear.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to KlingelnbergCycloPalloidSpiralBevelGear. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_set(self) -> '_2266.KlingelnbergCycloPalloidSpiralBevelGearSet':
        '''KlingelnbergCycloPalloidSpiralBevelGearSet: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2266.KlingelnbergCycloPalloidSpiralBevelGearSet.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to KlingelnbergCycloPalloidSpiralBevelGearSet. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_planetary_gear_set(self) -> '_2267.PlanetaryGearSet':
        '''PlanetaryGearSet: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2267.PlanetaryGearSet.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to PlanetaryGearSet. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_spiral_bevel_gear(self) -> '_2268.SpiralBevelGear':
        '''SpiralBevelGear: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2268.SpiralBevelGear.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to SpiralBevelGear. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_spiral_bevel_gear_set(self) -> '_2269.SpiralBevelGearSet':
        '''SpiralBevelGearSet: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2269.SpiralBevelGearSet.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to SpiralBevelGearSet. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_straight_bevel_diff_gear(self) -> '_2270.StraightBevelDiffGear':
        '''StraightBevelDiffGear: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2270.StraightBevelDiffGear.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to StraightBevelDiffGear. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_straight_bevel_diff_gear_set(self) -> '_2271.StraightBevelDiffGearSet':
        '''StraightBevelDiffGearSet: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2271.StraightBevelDiffGearSet.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to StraightBevelDiffGearSet. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_straight_bevel_gear(self) -> '_2272.StraightBevelGear':
        '''StraightBevelGear: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2272.StraightBevelGear.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to StraightBevelGear. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_straight_bevel_gear_set(self) -> '_2273.StraightBevelGearSet':
        '''StraightBevelGearSet: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2273.StraightBevelGearSet.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to StraightBevelGearSet. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_straight_bevel_planet_gear(self) -> '_2274.StraightBevelPlanetGear':
        '''StraightBevelPlanetGear: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2274.StraightBevelPlanetGear.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to StraightBevelPlanetGear. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_straight_bevel_sun_gear(self) -> '_2275.StraightBevelSunGear':
        '''StraightBevelSunGear: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2275.StraightBevelSunGear.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to StraightBevelSunGear. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_worm_gear(self) -> '_2276.WormGear':
        '''WormGear: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2276.WormGear.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to WormGear. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_worm_gear_set(self) -> '_2277.WormGearSet':
        '''WormGearSet: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2277.WormGearSet.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to WormGearSet. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_zerol_bevel_gear(self) -> '_2278.ZerolBevelGear':
        '''ZerolBevelGear: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2278.ZerolBevelGear.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to ZerolBevelGear. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_zerol_bevel_gear_set(self) -> '_2279.ZerolBevelGearSet':
        '''ZerolBevelGearSet: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2279.ZerolBevelGearSet.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to ZerolBevelGearSet. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_cycloidal_assembly(self) -> '_2293.CycloidalAssembly':
        '''CycloidalAssembly: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2293.CycloidalAssembly.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to CycloidalAssembly. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_cycloidal_disc(self) -> '_2294.CycloidalDisc':
        '''CycloidalDisc: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2294.CycloidalDisc.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to CycloidalDisc. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_ring_pins(self) -> '_2295.RingPins':
        '''RingPins: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2295.RingPins.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to RingPins. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_belt_drive(self) -> '_2301.BeltDrive':
        '''BeltDrive: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2301.BeltDrive.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to BeltDrive. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_clutch(self) -> '_2303.Clutch':
        '''Clutch: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2303.Clutch.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to Clutch. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_clutch_half(self) -> '_2304.ClutchHalf':
        '''ClutchHalf: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2304.ClutchHalf.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to ClutchHalf. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_concept_coupling(self) -> '_2306.ConceptCoupling':
        '''ConceptCoupling: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2306.ConceptCoupling.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to ConceptCoupling. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_concept_coupling_half(self) -> '_2307.ConceptCouplingHalf':
        '''ConceptCouplingHalf: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2307.ConceptCouplingHalf.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to ConceptCouplingHalf. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_coupling(self) -> '_2308.Coupling':
        '''Coupling: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2308.Coupling.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to Coupling. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_coupling_half(self) -> '_2309.CouplingHalf':
        '''CouplingHalf: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2309.CouplingHalf.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to CouplingHalf. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_cvt(self) -> '_2311.CVT':
        '''CVT: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2311.CVT.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to CVT. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_cvt_pulley(self) -> '_2312.CVTPulley':
        '''CVTPulley: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2312.CVTPulley.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to CVTPulley. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_part_to_part_shear_coupling(self) -> '_2313.PartToPartShearCoupling':
        '''PartToPartShearCoupling: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2313.PartToPartShearCoupling.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to PartToPartShearCoupling. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_part_to_part_shear_coupling_half(self) -> '_2314.PartToPartShearCouplingHalf':
        '''PartToPartShearCouplingHalf: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2314.PartToPartShearCouplingHalf.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to PartToPartShearCouplingHalf. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_pulley(self) -> '_2315.Pulley':
        '''Pulley: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2315.Pulley.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to Pulley. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_rolling_ring(self) -> '_2321.RollingRing':
        '''RollingRing: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2321.RollingRing.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to RollingRing. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_rolling_ring_assembly(self) -> '_2322.RollingRingAssembly':
        '''RollingRingAssembly: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2322.RollingRingAssembly.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to RollingRingAssembly. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_shaft_hub_connection(self) -> '_2323.ShaftHubConnection':
        '''ShaftHubConnection: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2323.ShaftHubConnection.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to ShaftHubConnection. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_spring_damper(self) -> '_2325.SpringDamper':
        '''SpringDamper: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2325.SpringDamper.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to SpringDamper. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_spring_damper_half(self) -> '_2326.SpringDamperHalf':
        '''SpringDamperHalf: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2326.SpringDamperHalf.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to SpringDamperHalf. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_synchroniser(self) -> '_2327.Synchroniser':
        '''Synchroniser: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2327.Synchroniser.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to Synchroniser. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_synchroniser_half(self) -> '_2329.SynchroniserHalf':
        '''SynchroniserHalf: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2329.SynchroniserHalf.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to SynchroniserHalf. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_synchroniser_part(self) -> '_2330.SynchroniserPart':
        '''SynchroniserPart: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2330.SynchroniserPart.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to SynchroniserPart. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_synchroniser_sleeve(self) -> '_2331.SynchroniserSleeve':
        '''SynchroniserSleeve: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2331.SynchroniserSleeve.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to SynchroniserSleeve. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_torque_converter(self) -> '_2332.TorqueConverter':
        '''TorqueConverter: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2332.TorqueConverter.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to TorqueConverter. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_torque_converter_pump(self) -> '_2333.TorqueConverterPump':
        '''TorqueConverterPump: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2333.TorqueConverterPump.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to TorqueConverterPump. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_of_type_torque_converter_turbine(self) -> '_2335.TorqueConverterTurbine':
        '''TorqueConverterTurbine: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2335.TorqueConverterTurbine.TYPE not in self.wrapped.Part.__class__.__mro__:
            raise CastException('Failed to cast part to TorqueConverterTurbine. Expected: {}.'.format(self.wrapped.Part.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Part.__class__)(self.wrapped.Part) if self.wrapped.Part is not None else None

    @property
    def part_load_cases(self) -> 'List[_6631.PartLoadCase]':
        '''List[PartLoadCase]: 'PartLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PartLoadCases, constructor.new(_6631.PartLoadCase))
        return value

    def clear_user_specified_excitation_data_for_all_load_cases(self):
        ''' 'ClearUserSpecifiedExcitationDataForAllLoadCases' is the original name of this method.'''

        self.wrapped.ClearUserSpecifiedExcitationDataForAllLoadCases()
