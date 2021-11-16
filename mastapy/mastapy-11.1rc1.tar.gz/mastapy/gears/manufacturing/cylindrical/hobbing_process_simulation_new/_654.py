'''_654.py

WormGrindingProcessSimulationNew
'''


from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
    _647, _652, _649, _650,
    _646, _656, _651, _640,
    _653
)
from mastapy._internal import constructor
from mastapy._internal.python_net import python_net_import

_WORM_GRINDING_PROCESS_SIMULATION_NEW = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.HobbingProcessSimulationNew', 'WormGrindingProcessSimulationNew')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGrindingProcessSimulationNew',)


class WormGrindingProcessSimulationNew(_640.ProcessSimulationNew['_653.WormGrindingProcessSimulationInput']):
    '''WormGrindingProcessSimulationNew

    This is a mastapy class.
    '''

    TYPE = _WORM_GRINDING_PROCESS_SIMULATION_NEW

    __hash__ = None

    def __init__(self, instance_to_wrap: 'WormGrindingProcessSimulationNew.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def worm_grinding_process_lead_calculation(self) -> '_647.WormGrindingLeadCalculation':
        '''WormGrindingLeadCalculation: 'WormGrindingProcessLeadCalculation' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_647.WormGrindingLeadCalculation)(self.wrapped.WormGrindingProcessLeadCalculation) if self.wrapped.WormGrindingProcessLeadCalculation is not None else None

    @property
    def worm_grinding_process_profile_calculation(self) -> '_652.WormGrindingProcessProfileCalculation':
        '''WormGrindingProcessProfileCalculation: 'WormGrindingProcessProfileCalculation' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_652.WormGrindingProcessProfileCalculation)(self.wrapped.WormGrindingProcessProfileCalculation) if self.wrapped.WormGrindingProcessProfileCalculation is not None else None

    @property
    def worm_grinding_process_gear_shape_calculation(self) -> '_649.WormGrindingProcessGearShape':
        '''WormGrindingProcessGearShape: 'WormGrindingProcessGearShapeCalculation' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_649.WormGrindingProcessGearShape)(self.wrapped.WormGrindingProcessGearShapeCalculation) if self.wrapped.WormGrindingProcessGearShapeCalculation is not None else None

    @property
    def worm_grinding_process_mark_on_shaft_calculation(self) -> '_650.WormGrindingProcessMarkOnShaft':
        '''WormGrindingProcessMarkOnShaft: 'WormGrindingProcessMarkOnShaftCalculation' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_650.WormGrindingProcessMarkOnShaft)(self.wrapped.WormGrindingProcessMarkOnShaftCalculation) if self.wrapped.WormGrindingProcessMarkOnShaftCalculation is not None else None

    @property
    def worm_grinding_cutter_calculation(self) -> '_646.WormGrindingCutterCalculation':
        '''WormGrindingCutterCalculation: 'WormGrindingCutterCalculation' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_646.WormGrindingCutterCalculation)(self.wrapped.WormGrindingCutterCalculation) if self.wrapped.WormGrindingCutterCalculation is not None else None

    @property
    def worm_grinding_process_total_modification_calculation(self) -> '_656.WormGrindingProcessTotalModificationCalculation':
        '''WormGrindingProcessTotalModificationCalculation: 'WormGrindingProcessTotalModificationCalculation' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_656.WormGrindingProcessTotalModificationCalculation)(self.wrapped.WormGrindingProcessTotalModificationCalculation) if self.wrapped.WormGrindingProcessTotalModificationCalculation is not None else None

    @property
    def worm_grinding_process_pitch_calculation(self) -> '_651.WormGrindingProcessPitchCalculation':
        '''WormGrindingProcessPitchCalculation: 'WormGrindingProcessPitchCalculation' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_651.WormGrindingProcessPitchCalculation)(self.wrapped.WormGrindingProcessPitchCalculation) if self.wrapped.WormGrindingProcessPitchCalculation is not None else None
