'''_627.py

HobbingProcessSimulationNew
'''


from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
    _622, _624, _625, _621,
    _623, _629, _640, _626
)
from mastapy._internal import constructor
from mastapy._internal.python_net import python_net_import

_HOBBING_PROCESS_SIMULATION_NEW = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.HobbingProcessSimulationNew', 'HobbingProcessSimulationNew')


__docformat__ = 'restructuredtext en'
__all__ = ('HobbingProcessSimulationNew',)


class HobbingProcessSimulationNew(_640.ProcessSimulationNew['_626.HobbingProcessSimulationInput']):
    '''HobbingProcessSimulationNew

    This is a mastapy class.
    '''

    TYPE = _HOBBING_PROCESS_SIMULATION_NEW

    __hash__ = None

    def __init__(self, instance_to_wrap: 'HobbingProcessSimulationNew.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def hobbing_process_lead_calculation(self) -> '_622.HobbingProcessLeadCalculation':
        '''HobbingProcessLeadCalculation: 'HobbingProcessLeadCalculation' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_622.HobbingProcessLeadCalculation)(self.wrapped.HobbingProcessLeadCalculation) if self.wrapped.HobbingProcessLeadCalculation is not None else None

    @property
    def hobbing_process_pitch_calculation(self) -> '_624.HobbingProcessPitchCalculation':
        '''HobbingProcessPitchCalculation: 'HobbingProcessPitchCalculation' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_624.HobbingProcessPitchCalculation)(self.wrapped.HobbingProcessPitchCalculation) if self.wrapped.HobbingProcessPitchCalculation is not None else None

    @property
    def hobbing_process_profile_calculation(self) -> '_625.HobbingProcessProfileCalculation':
        '''HobbingProcessProfileCalculation: 'HobbingProcessProfileCalculation' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_625.HobbingProcessProfileCalculation)(self.wrapped.HobbingProcessProfileCalculation) if self.wrapped.HobbingProcessProfileCalculation is not None else None

    @property
    def hobbing_process_gear_shape_calculation(self) -> '_621.HobbingProcessGearShape':
        '''HobbingProcessGearShape: 'HobbingProcessGearShapeCalculation' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_621.HobbingProcessGearShape)(self.wrapped.HobbingProcessGearShapeCalculation) if self.wrapped.HobbingProcessGearShapeCalculation is not None else None

    @property
    def hobbing_process_mark_on_shaft_calculation(self) -> '_623.HobbingProcessMarkOnShaft':
        '''HobbingProcessMarkOnShaft: 'HobbingProcessMarkOnShaftCalculation' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_623.HobbingProcessMarkOnShaft)(self.wrapped.HobbingProcessMarkOnShaftCalculation) if self.wrapped.HobbingProcessMarkOnShaftCalculation is not None else None

    @property
    def hobbing_process_total_modification(self) -> '_629.HobbingProcessTotalModificationCalculation':
        '''HobbingProcessTotalModificationCalculation: 'HobbingProcessTotalModification' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_629.HobbingProcessTotalModificationCalculation)(self.wrapped.HobbingProcessTotalModification) if self.wrapped.HobbingProcessTotalModification is not None else None
