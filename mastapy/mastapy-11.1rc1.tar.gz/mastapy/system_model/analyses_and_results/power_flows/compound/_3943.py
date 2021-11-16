'''_3943.py

GearSetCompoundPowerFlow
'''


from typing import List

from mastapy.gears.rating import _327
from mastapy._internal import constructor, conversion
from mastapy.gears.rating.worm import _340
from mastapy._internal.cast_exception import CastException
from mastapy.gears.rating.face import _414
from mastapy.gears.rating.cylindrical import _426
from mastapy.gears.rating.conical import _495
from mastapy.gears.rating.concept import _506
from mastapy.system_model.analyses_and_results.power_flows import _3811
from mastapy.system_model.analyses_and_results.power_flows.compound import _3981
from mastapy._internal.python_net import python_net_import

_GEAR_SET_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'GearSetCompoundPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('GearSetCompoundPowerFlow',)


class GearSetCompoundPowerFlow(_3981.SpecialisedAssemblyCompoundPowerFlow):
    '''GearSetCompoundPowerFlow

    This is a mastapy class.
    '''

    TYPE = _GEAR_SET_COMPOUND_POWER_FLOW

    __hash__ = None

    def __init__(self, instance_to_wrap: 'GearSetCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gear_set_duty_cycle_rating(self) -> '_327.GearSetDutyCycleRating':
        '''GearSetDutyCycleRating: 'GearSetDutyCycleRating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _327.GearSetDutyCycleRating.TYPE not in self.wrapped.GearSetDutyCycleRating.__class__.__mro__:
            raise CastException('Failed to cast gear_set_duty_cycle_rating to GearSetDutyCycleRating. Expected: {}.'.format(self.wrapped.GearSetDutyCycleRating.__class__.__qualname__))

        return constructor.new_override(self.wrapped.GearSetDutyCycleRating.__class__)(self.wrapped.GearSetDutyCycleRating) if self.wrapped.GearSetDutyCycleRating is not None else None

    @property
    def gear_set_duty_cycle_rating_of_type_worm_gear_set_duty_cycle_rating(self) -> '_340.WormGearSetDutyCycleRating':
        '''WormGearSetDutyCycleRating: 'GearSetDutyCycleRating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _340.WormGearSetDutyCycleRating.TYPE not in self.wrapped.GearSetDutyCycleRating.__class__.__mro__:
            raise CastException('Failed to cast gear_set_duty_cycle_rating to WormGearSetDutyCycleRating. Expected: {}.'.format(self.wrapped.GearSetDutyCycleRating.__class__.__qualname__))

        return constructor.new_override(self.wrapped.GearSetDutyCycleRating.__class__)(self.wrapped.GearSetDutyCycleRating) if self.wrapped.GearSetDutyCycleRating is not None else None

    @property
    def gear_set_duty_cycle_rating_of_type_face_gear_set_duty_cycle_rating(self) -> '_414.FaceGearSetDutyCycleRating':
        '''FaceGearSetDutyCycleRating: 'GearSetDutyCycleRating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _414.FaceGearSetDutyCycleRating.TYPE not in self.wrapped.GearSetDutyCycleRating.__class__.__mro__:
            raise CastException('Failed to cast gear_set_duty_cycle_rating to FaceGearSetDutyCycleRating. Expected: {}.'.format(self.wrapped.GearSetDutyCycleRating.__class__.__qualname__))

        return constructor.new_override(self.wrapped.GearSetDutyCycleRating.__class__)(self.wrapped.GearSetDutyCycleRating) if self.wrapped.GearSetDutyCycleRating is not None else None

    @property
    def gear_set_duty_cycle_rating_of_type_cylindrical_gear_set_duty_cycle_rating(self) -> '_426.CylindricalGearSetDutyCycleRating':
        '''CylindricalGearSetDutyCycleRating: 'GearSetDutyCycleRating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _426.CylindricalGearSetDutyCycleRating.TYPE not in self.wrapped.GearSetDutyCycleRating.__class__.__mro__:
            raise CastException('Failed to cast gear_set_duty_cycle_rating to CylindricalGearSetDutyCycleRating. Expected: {}.'.format(self.wrapped.GearSetDutyCycleRating.__class__.__qualname__))

        return constructor.new_override(self.wrapped.GearSetDutyCycleRating.__class__)(self.wrapped.GearSetDutyCycleRating) if self.wrapped.GearSetDutyCycleRating is not None else None

    @property
    def gear_set_duty_cycle_rating_of_type_conical_gear_set_duty_cycle_rating(self) -> '_495.ConicalGearSetDutyCycleRating':
        '''ConicalGearSetDutyCycleRating: 'GearSetDutyCycleRating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _495.ConicalGearSetDutyCycleRating.TYPE not in self.wrapped.GearSetDutyCycleRating.__class__.__mro__:
            raise CastException('Failed to cast gear_set_duty_cycle_rating to ConicalGearSetDutyCycleRating. Expected: {}.'.format(self.wrapped.GearSetDutyCycleRating.__class__.__qualname__))

        return constructor.new_override(self.wrapped.GearSetDutyCycleRating.__class__)(self.wrapped.GearSetDutyCycleRating) if self.wrapped.GearSetDutyCycleRating is not None else None

    @property
    def gear_set_duty_cycle_rating_of_type_concept_gear_set_duty_cycle_rating(self) -> '_506.ConceptGearSetDutyCycleRating':
        '''ConceptGearSetDutyCycleRating: 'GearSetDutyCycleRating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _506.ConceptGearSetDutyCycleRating.TYPE not in self.wrapped.GearSetDutyCycleRating.__class__.__mro__:
            raise CastException('Failed to cast gear_set_duty_cycle_rating to ConceptGearSetDutyCycleRating. Expected: {}.'.format(self.wrapped.GearSetDutyCycleRating.__class__.__qualname__))

        return constructor.new_override(self.wrapped.GearSetDutyCycleRating.__class__)(self.wrapped.GearSetDutyCycleRating) if self.wrapped.GearSetDutyCycleRating is not None else None

    @property
    def assembly_analysis_cases(self) -> 'List[_3811.GearSetPowerFlow]':
        '''List[GearSetPowerFlow]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCases, constructor.new(_3811.GearSetPowerFlow))
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_3811.GearSetPowerFlow]':
        '''List[GearSetPowerFlow]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.AssemblyAnalysisCasesReady, constructor.new(_3811.GearSetPowerFlow))
        return value
