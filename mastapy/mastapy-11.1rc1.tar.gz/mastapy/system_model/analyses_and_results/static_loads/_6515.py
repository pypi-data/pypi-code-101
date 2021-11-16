'''_6515.py

AGMAGleasonConicalGearSetLoadCase
'''


from mastapy._internal import constructor
from mastapy.system_model.part_model.gears import (
    _2239, _2241, _2245, _2260,
    _2269, _2271, _2273, _2279
)
from mastapy._internal.cast_exception import CastException
from mastapy.gears.manufacturing.bevel import _747, _745, _746
from mastapy.system_model.analyses_and_results.static_loads import _6547
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_SET_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'AGMAGleasonConicalGearSetLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('AGMAGleasonConicalGearSetLoadCase',)


class AGMAGleasonConicalGearSetLoadCase(_6547.ConicalGearSetLoadCase):
    '''AGMAGleasonConicalGearSetLoadCase

    This is a mastapy class.
    '''

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_SET_LOAD_CASE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'AGMAGleasonConicalGearSetLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def override_manufacturing_config_micro_geometry(self) -> 'bool':
        '''bool: 'OverrideManufacturingConfigMicroGeometry' is the original name of this property.'''

        return self.wrapped.OverrideManufacturingConfigMicroGeometry

    @override_manufacturing_config_micro_geometry.setter
    def override_manufacturing_config_micro_geometry(self, value: 'bool'):
        self.wrapped.OverrideManufacturingConfigMicroGeometry = bool(value) if value else False

    @property
    def assembly_design(self) -> '_2239.AGMAGleasonConicalGearSet':
        '''AGMAGleasonConicalGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2239.AGMAGleasonConicalGearSet.TYPE not in self.wrapped.AssemblyDesign.__class__.__mro__:
            raise CastException('Failed to cast assembly_design to AGMAGleasonConicalGearSet. Expected: {}.'.format(self.wrapped.AssemblyDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.AssemblyDesign.__class__)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def assembly_design_of_type_bevel_differential_gear_set(self) -> '_2241.BevelDifferentialGearSet':
        '''BevelDifferentialGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2241.BevelDifferentialGearSet.TYPE not in self.wrapped.AssemblyDesign.__class__.__mro__:
            raise CastException('Failed to cast assembly_design to BevelDifferentialGearSet. Expected: {}.'.format(self.wrapped.AssemblyDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.AssemblyDesign.__class__)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def assembly_design_of_type_bevel_gear_set(self) -> '_2245.BevelGearSet':
        '''BevelGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2245.BevelGearSet.TYPE not in self.wrapped.AssemblyDesign.__class__.__mro__:
            raise CastException('Failed to cast assembly_design to BevelGearSet. Expected: {}.'.format(self.wrapped.AssemblyDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.AssemblyDesign.__class__)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def assembly_design_of_type_hypoid_gear_set(self) -> '_2260.HypoidGearSet':
        '''HypoidGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2260.HypoidGearSet.TYPE not in self.wrapped.AssemblyDesign.__class__.__mro__:
            raise CastException('Failed to cast assembly_design to HypoidGearSet. Expected: {}.'.format(self.wrapped.AssemblyDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.AssemblyDesign.__class__)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def assembly_design_of_type_spiral_bevel_gear_set(self) -> '_2269.SpiralBevelGearSet':
        '''SpiralBevelGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2269.SpiralBevelGearSet.TYPE not in self.wrapped.AssemblyDesign.__class__.__mro__:
            raise CastException('Failed to cast assembly_design to SpiralBevelGearSet. Expected: {}.'.format(self.wrapped.AssemblyDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.AssemblyDesign.__class__)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def assembly_design_of_type_straight_bevel_diff_gear_set(self) -> '_2271.StraightBevelDiffGearSet':
        '''StraightBevelDiffGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2271.StraightBevelDiffGearSet.TYPE not in self.wrapped.AssemblyDesign.__class__.__mro__:
            raise CastException('Failed to cast assembly_design to StraightBevelDiffGearSet. Expected: {}.'.format(self.wrapped.AssemblyDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.AssemblyDesign.__class__)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def assembly_design_of_type_straight_bevel_gear_set(self) -> '_2273.StraightBevelGearSet':
        '''StraightBevelGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2273.StraightBevelGearSet.TYPE not in self.wrapped.AssemblyDesign.__class__.__mro__:
            raise CastException('Failed to cast assembly_design to StraightBevelGearSet. Expected: {}.'.format(self.wrapped.AssemblyDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.AssemblyDesign.__class__)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def assembly_design_of_type_zerol_bevel_gear_set(self) -> '_2279.ZerolBevelGearSet':
        '''ZerolBevelGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2279.ZerolBevelGearSet.TYPE not in self.wrapped.AssemblyDesign.__class__.__mro__:
            raise CastException('Failed to cast assembly_design to ZerolBevelGearSet. Expected: {}.'.format(self.wrapped.AssemblyDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.AssemblyDesign.__class__)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def overridden_manufacturing_config_micro_geometry(self) -> '_747.ConicalSetMicroGeometryConfigBase':
        '''ConicalSetMicroGeometryConfigBase: 'OverriddenManufacturingConfigMicroGeometry' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _747.ConicalSetMicroGeometryConfigBase.TYPE not in self.wrapped.OverriddenManufacturingConfigMicroGeometry.__class__.__mro__:
            raise CastException('Failed to cast overridden_manufacturing_config_micro_geometry to ConicalSetMicroGeometryConfigBase. Expected: {}.'.format(self.wrapped.OverriddenManufacturingConfigMicroGeometry.__class__.__qualname__))

        return constructor.new_override(self.wrapped.OverriddenManufacturingConfigMicroGeometry.__class__)(self.wrapped.OverriddenManufacturingConfigMicroGeometry) if self.wrapped.OverriddenManufacturingConfigMicroGeometry is not None else None

    @property
    def overridden_manufacturing_config_micro_geometry_of_type_conical_set_manufacturing_config(self) -> '_745.ConicalSetManufacturingConfig':
        '''ConicalSetManufacturingConfig: 'OverriddenManufacturingConfigMicroGeometry' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _745.ConicalSetManufacturingConfig.TYPE not in self.wrapped.OverriddenManufacturingConfigMicroGeometry.__class__.__mro__:
            raise CastException('Failed to cast overridden_manufacturing_config_micro_geometry to ConicalSetManufacturingConfig. Expected: {}.'.format(self.wrapped.OverriddenManufacturingConfigMicroGeometry.__class__.__qualname__))

        return constructor.new_override(self.wrapped.OverriddenManufacturingConfigMicroGeometry.__class__)(self.wrapped.OverriddenManufacturingConfigMicroGeometry) if self.wrapped.OverriddenManufacturingConfigMicroGeometry is not None else None

    @property
    def overridden_manufacturing_config_micro_geometry_of_type_conical_set_micro_geometry_config(self) -> '_746.ConicalSetMicroGeometryConfig':
        '''ConicalSetMicroGeometryConfig: 'OverriddenManufacturingConfigMicroGeometry' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _746.ConicalSetMicroGeometryConfig.TYPE not in self.wrapped.OverriddenManufacturingConfigMicroGeometry.__class__.__mro__:
            raise CastException('Failed to cast overridden_manufacturing_config_micro_geometry to ConicalSetMicroGeometryConfig. Expected: {}.'.format(self.wrapped.OverriddenManufacturingConfigMicroGeometry.__class__.__qualname__))

        return constructor.new_override(self.wrapped.OverriddenManufacturingConfigMicroGeometry.__class__)(self.wrapped.OverriddenManufacturingConfigMicroGeometry) if self.wrapped.OverriddenManufacturingConfigMicroGeometry is not None else None
