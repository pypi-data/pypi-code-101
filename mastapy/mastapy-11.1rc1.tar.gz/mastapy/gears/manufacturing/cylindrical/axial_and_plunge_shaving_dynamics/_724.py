'''_724.py

ShavingDynamicsViewModel
'''


from typing import List, Generic, TypeVar

from mastapy._internal.implicit import enum_with_selected_value
from mastapy.gears.gear_designs.cylindrical import _1028, _976
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import enum_with_selected_value_runtime, conversion, constructor
from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import (
    _703, _720, _706, _707,
    _712, _713, _715, _725,
    _719
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAVING_DYNAMICS_VIEW_MODEL = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.AxialAndPlungeShavingDynamics', 'ShavingDynamicsViewModel')


__docformat__ = 'restructuredtext en'
__all__ = ('ShavingDynamicsViewModel',)


T = TypeVar('T', bound='_719.ShavingDynamics')


class ShavingDynamicsViewModel(_725.ShavingDynamicsViewModelBase, Generic[T]):
    '''ShavingDynamicsViewModel

    This is a mastapy class.

    Generic Types:
        T
    '''

    TYPE = _SHAVING_DYNAMICS_VIEW_MODEL

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ShavingDynamicsViewModel.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def selected_measurement_method(self) -> 'enum_with_selected_value.EnumWithSelectedValue_ThicknessType':
        '''enum_with_selected_value.EnumWithSelectedValue_ThicknessType: 'SelectedMeasurementMethod' is the original name of this property.'''

        value = enum_with_selected_value.EnumWithSelectedValue_ThicknessType.wrapped_type()
        return enum_with_selected_value_runtime.create(self.wrapped.SelectedMeasurementMethod, value) if self.wrapped.SelectedMeasurementMethod is not None else None

    @selected_measurement_method.setter
    def selected_measurement_method(self, value: 'enum_with_selected_value.EnumWithSelectedValue_ThicknessType.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_ThicknessType.implicit_type()
        value = conversion.mp_to_pn_enum(value)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.SelectedMeasurementMethod = value

    @property
    def shaver_tip_diameter_adjustment(self) -> 'float':
        '''float: 'ShaverTipDiameterAdjustment' is the original name of this property.'''

        return self.wrapped.ShaverTipDiameterAdjustment

    @shaver_tip_diameter_adjustment.setter
    def shaver_tip_diameter_adjustment(self, value: 'float'):
        self.wrapped.ShaverTipDiameterAdjustment = float(value) if value else 0.0

    @property
    def chart_display_method(self) -> '_976.CylindricalGearProfileMeasurementType':
        '''CylindricalGearProfileMeasurementType: 'ChartDisplayMethod' is the original name of this property.'''

        value = conversion.pn_to_mp_enum(self.wrapped.ChartDisplayMethod)
        return constructor.new(_976.CylindricalGearProfileMeasurementType)(value) if value is not None else None

    @chart_display_method.setter
    def chart_display_method(self, value: '_976.CylindricalGearProfileMeasurementType'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.ChartDisplayMethod = value

    @property
    def active_profile_range_calculation_source(self) -> '_703.ActiveProfileRangeCalculationSource':
        '''ActiveProfileRangeCalculationSource: 'ActiveProfileRangeCalculationSource' is the original name of this property.'''

        value = conversion.pn_to_mp_enum(self.wrapped.ActiveProfileRangeCalculationSource)
        return constructor.new(_703.ActiveProfileRangeCalculationSource)(value) if value is not None else None

    @active_profile_range_calculation_source.setter
    def active_profile_range_calculation_source(self, value: '_703.ActiveProfileRangeCalculationSource'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.ActiveProfileRangeCalculationSource = value

    @property
    def use_shaver_from_database(self) -> 'bool':
        '''bool: 'UseShaverFromDatabase' is the original name of this property.'''

        return self.wrapped.UseShaverFromDatabase

    @use_shaver_from_database.setter
    def use_shaver_from_database(self, value: 'bool'):
        self.wrapped.UseShaverFromDatabase = bool(value) if value else False

    @property
    def calculation(self) -> '_720.ShavingDynamicsCalculation[T]':
        '''ShavingDynamicsCalculation[T]: 'Calculation' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _720.ShavingDynamicsCalculation[T].TYPE not in self.wrapped.Calculation.__class__.__mro__:
            raise CastException('Failed to cast calculation to ShavingDynamicsCalculation[T]. Expected: {}.'.format(self.wrapped.Calculation.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Calculation.__class__)(self.wrapped.Calculation) if self.wrapped.Calculation is not None else None

    @property
    def calculation_of_type_conventional_shaving_dynamics_calculation_for_designed_gears(self) -> '_706.ConventionalShavingDynamicsCalculationForDesignedGears':
        '''ConventionalShavingDynamicsCalculationForDesignedGears: 'Calculation' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _706.ConventionalShavingDynamicsCalculationForDesignedGears.TYPE not in self.wrapped.Calculation.__class__.__mro__:
            raise CastException('Failed to cast calculation to ConventionalShavingDynamicsCalculationForDesignedGears. Expected: {}.'.format(self.wrapped.Calculation.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Calculation.__class__)(self.wrapped.Calculation) if self.wrapped.Calculation is not None else None

    @property
    def calculation_of_type_conventional_shaving_dynamics_calculation_for_hobbed_gears(self) -> '_707.ConventionalShavingDynamicsCalculationForHobbedGears':
        '''ConventionalShavingDynamicsCalculationForHobbedGears: 'Calculation' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _707.ConventionalShavingDynamicsCalculationForHobbedGears.TYPE not in self.wrapped.Calculation.__class__.__mro__:
            raise CastException('Failed to cast calculation to ConventionalShavingDynamicsCalculationForHobbedGears. Expected: {}.'.format(self.wrapped.Calculation.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Calculation.__class__)(self.wrapped.Calculation) if self.wrapped.Calculation is not None else None

    @property
    def calculation_of_type_plunge_shaving_dynamics_calculation_for_designed_gears(self) -> '_712.PlungeShavingDynamicsCalculationForDesignedGears':
        '''PlungeShavingDynamicsCalculationForDesignedGears: 'Calculation' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _712.PlungeShavingDynamicsCalculationForDesignedGears.TYPE not in self.wrapped.Calculation.__class__.__mro__:
            raise CastException('Failed to cast calculation to PlungeShavingDynamicsCalculationForDesignedGears. Expected: {}.'.format(self.wrapped.Calculation.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Calculation.__class__)(self.wrapped.Calculation) if self.wrapped.Calculation is not None else None

    @property
    def calculation_of_type_plunge_shaving_dynamics_calculation_for_hobbed_gears(self) -> '_713.PlungeShavingDynamicsCalculationForHobbedGears':
        '''PlungeShavingDynamicsCalculationForHobbedGears: 'Calculation' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _713.PlungeShavingDynamicsCalculationForHobbedGears.TYPE not in self.wrapped.Calculation.__class__.__mro__:
            raise CastException('Failed to cast calculation to PlungeShavingDynamicsCalculationForHobbedGears. Expected: {}.'.format(self.wrapped.Calculation.__class__.__qualname__))

        return constructor.new_override(self.wrapped.Calculation.__class__)(self.wrapped.Calculation) if self.wrapped.Calculation is not None else None

    @property
    def redressing_settings(self) -> 'List[_715.RedressingSettings[T]]':
        '''List[RedressingSettings[T]]: 'RedressingSettings' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.RedressingSettings, constructor.new(_715.RedressingSettings)[T])
        return value

    def calculate(self):
        ''' 'Calculate' is the original name of this method.'''

        self.wrapped.Calculate()

    def add_shaver_to_database(self):
        ''' 'AddShaverToDatabase' is the original name of this method.'''

        self.wrapped.AddShaverToDatabase()
