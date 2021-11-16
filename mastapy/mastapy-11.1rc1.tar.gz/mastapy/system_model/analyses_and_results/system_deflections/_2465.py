'''_2465.py

CylindricalGearSystemDeflection
'''


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model.gears import _2250, _2252
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.analyses_and_results.static_loads import _6560, _6565
from mastapy.system_model.analyses_and_results.power_flows import _3799, _3801
from mastapy.gears.rating.cylindrical import _422
from mastapy.gears.manufacturing.cylindrical import _571
from mastapy.system_model.analyses_and_results.system_deflections import _2469, _2481
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'CylindricalGearSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearSystemDeflection',)


class CylindricalGearSystemDeflection(_2481.GearSystemDeflection):
    '''CylindricalGearSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _CYLINDRICAL_GEAR_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CylindricalGearSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def operating_root_diameter(self) -> 'float':
        '''float: 'OperatingRootDiameter' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.OperatingRootDiameter

    @property
    def power(self) -> 'float':
        '''float: 'Power' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.Power

    @property
    def torque(self) -> 'float':
        '''float: 'Torque' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return self.wrapped.Torque

    @property
    def component_design(self) -> '_2250.CylindricalGear':
        '''CylindricalGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2250.CylindricalGear.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to CylindricalGear. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_load_case(self) -> '_6560.CylindricalGearLoadCase':
        '''CylindricalGearLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _6560.CylindricalGearLoadCase.TYPE not in self.wrapped.ComponentLoadCase.__class__.__mro__:
            raise CastException('Failed to cast component_load_case to CylindricalGearLoadCase. Expected: {}.'.format(self.wrapped.ComponentLoadCase.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentLoadCase.__class__)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase is not None else None

    @property
    def power_flow_results(self) -> '_3799.CylindricalGearPowerFlow':
        '''CylindricalGearPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _3799.CylindricalGearPowerFlow.TYPE not in self.wrapped.PowerFlowResults.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to CylindricalGearPowerFlow. Expected: {}.'.format(self.wrapped.PowerFlowResults.__class__.__qualname__))

        return constructor.new_override(self.wrapped.PowerFlowResults.__class__)(self.wrapped.PowerFlowResults) if self.wrapped.PowerFlowResults is not None else None

    @property
    def component_detailed_analysis(self) -> '_422.CylindricalGearRating':
        '''CylindricalGearRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_422.CylindricalGearRating)(self.wrapped.ComponentDetailedAnalysis) if self.wrapped.ComponentDetailedAnalysis is not None else None

    @property
    def manufacturing_analysis(self) -> '_571.CylindricalManufacturedGearLoadCase':
        '''CylindricalManufacturedGearLoadCase: 'ManufacturingAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_571.CylindricalManufacturedGearLoadCase)(self.wrapped.ManufacturingAnalysis) if self.wrapped.ManufacturingAnalysis is not None else None

    @property
    def planetaries(self) -> 'List[CylindricalGearSystemDeflection]':
        '''List[CylindricalGearSystemDeflection]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Planetaries, constructor.new(CylindricalGearSystemDeflection))
        return value

    @property
    def cylindrical_meshed_gear_system_deflections(self) -> 'List[_2469.CylindricalMeshedGearSystemDeflection]':
        '''List[CylindricalMeshedGearSystemDeflection]: 'CylindricalMeshedGearSystemDeflections' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CylindricalMeshedGearSystemDeflections, constructor.new(_2469.CylindricalMeshedGearSystemDeflection))
        return value

    @property
    def cylindrical_gear_system_deflections_in_meshes(self) -> 'List[_2469.CylindricalMeshedGearSystemDeflection]':
        '''List[CylindricalMeshedGearSystemDeflection]: 'CylindricalGearSystemDeflectionsInMeshes' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.CylindricalGearSystemDeflectionsInMeshes, constructor.new(_2469.CylindricalMeshedGearSystemDeflection))
        return value
