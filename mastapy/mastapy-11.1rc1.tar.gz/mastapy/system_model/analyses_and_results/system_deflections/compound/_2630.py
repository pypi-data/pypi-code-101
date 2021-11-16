'''_2630.py

GearCompoundSystemDeflection
'''


from typing import List

from mastapy.gears.rating import _323
from mastapy._internal import constructor, conversion
from mastapy.gears.rating.worm import _337
from mastapy._internal.cast_exception import CastException
from mastapy.gears.rating.face import _410
from mastapy.gears.rating.cylindrical import _417
from mastapy.gears.rating.conical import _492
from mastapy.gears.rating.concept import _502
from mastapy.system_model.analyses_and_results.system_deflections import _2481
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2649
from mastapy._internal.python_net import python_net_import

_GEAR_COMPOUND_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound', 'GearCompoundSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('GearCompoundSystemDeflection',)


class GearCompoundSystemDeflection(_2649.MountableComponentCompoundSystemDeflection):
    '''GearCompoundSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _GEAR_COMPOUND_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'GearCompoundSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def duty_cycle_rating(self) -> '_323.GearDutyCycleRating':
        '''GearDutyCycleRating: 'DutyCycleRating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _323.GearDutyCycleRating.TYPE not in self.wrapped.DutyCycleRating.__class__.__mro__:
            raise CastException('Failed to cast duty_cycle_rating to GearDutyCycleRating. Expected: {}.'.format(self.wrapped.DutyCycleRating.__class__.__qualname__))

        return constructor.new_override(self.wrapped.DutyCycleRating.__class__)(self.wrapped.DutyCycleRating) if self.wrapped.DutyCycleRating is not None else None

    @property
    def duty_cycle_rating_of_type_worm_gear_duty_cycle_rating(self) -> '_337.WormGearDutyCycleRating':
        '''WormGearDutyCycleRating: 'DutyCycleRating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _337.WormGearDutyCycleRating.TYPE not in self.wrapped.DutyCycleRating.__class__.__mro__:
            raise CastException('Failed to cast duty_cycle_rating to WormGearDutyCycleRating. Expected: {}.'.format(self.wrapped.DutyCycleRating.__class__.__qualname__))

        return constructor.new_override(self.wrapped.DutyCycleRating.__class__)(self.wrapped.DutyCycleRating) if self.wrapped.DutyCycleRating is not None else None

    @property
    def duty_cycle_rating_of_type_face_gear_duty_cycle_rating(self) -> '_410.FaceGearDutyCycleRating':
        '''FaceGearDutyCycleRating: 'DutyCycleRating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _410.FaceGearDutyCycleRating.TYPE not in self.wrapped.DutyCycleRating.__class__.__mro__:
            raise CastException('Failed to cast duty_cycle_rating to FaceGearDutyCycleRating. Expected: {}.'.format(self.wrapped.DutyCycleRating.__class__.__qualname__))

        return constructor.new_override(self.wrapped.DutyCycleRating.__class__)(self.wrapped.DutyCycleRating) if self.wrapped.DutyCycleRating is not None else None

    @property
    def duty_cycle_rating_of_type_cylindrical_gear_duty_cycle_rating(self) -> '_417.CylindricalGearDutyCycleRating':
        '''CylindricalGearDutyCycleRating: 'DutyCycleRating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _417.CylindricalGearDutyCycleRating.TYPE not in self.wrapped.DutyCycleRating.__class__.__mro__:
            raise CastException('Failed to cast duty_cycle_rating to CylindricalGearDutyCycleRating. Expected: {}.'.format(self.wrapped.DutyCycleRating.__class__.__qualname__))

        return constructor.new_override(self.wrapped.DutyCycleRating.__class__)(self.wrapped.DutyCycleRating) if self.wrapped.DutyCycleRating is not None else None

    @property
    def duty_cycle_rating_of_type_conical_gear_duty_cycle_rating(self) -> '_492.ConicalGearDutyCycleRating':
        '''ConicalGearDutyCycleRating: 'DutyCycleRating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _492.ConicalGearDutyCycleRating.TYPE not in self.wrapped.DutyCycleRating.__class__.__mro__:
            raise CastException('Failed to cast duty_cycle_rating to ConicalGearDutyCycleRating. Expected: {}.'.format(self.wrapped.DutyCycleRating.__class__.__qualname__))

        return constructor.new_override(self.wrapped.DutyCycleRating.__class__)(self.wrapped.DutyCycleRating) if self.wrapped.DutyCycleRating is not None else None

    @property
    def duty_cycle_rating_of_type_concept_gear_duty_cycle_rating(self) -> '_502.ConceptGearDutyCycleRating':
        '''ConceptGearDutyCycleRating: 'DutyCycleRating' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _502.ConceptGearDutyCycleRating.TYPE not in self.wrapped.DutyCycleRating.__class__.__mro__:
            raise CastException('Failed to cast duty_cycle_rating to ConceptGearDutyCycleRating. Expected: {}.'.format(self.wrapped.DutyCycleRating.__class__.__qualname__))

        return constructor.new_override(self.wrapped.DutyCycleRating.__class__)(self.wrapped.DutyCycleRating) if self.wrapped.DutyCycleRating is not None else None

    @property
    def component_analysis_cases(self) -> 'List[_2481.GearSystemDeflection]':
        '''List[GearSystemDeflection]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCases, constructor.new(_2481.GearSystemDeflection))
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_2481.GearSystemDeflection]':
        '''List[GearSystemDeflection]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.ComponentAnalysisCasesReady, constructor.new(_2481.GearSystemDeflection))
        return value
