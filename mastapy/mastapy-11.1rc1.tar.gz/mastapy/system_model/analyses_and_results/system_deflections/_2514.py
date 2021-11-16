'''_2514.py

RingPinsSystemDeflection
'''


from mastapy.system_model.part_model.cycloidal import _2295
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6646
from mastapy.system_model.analyses_and_results.power_flows import _3842
from mastapy.system_model.analyses_and_results.system_deflections import _2502
from mastapy._internal.python_net import python_net_import

_RING_PINS_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'RingPinsSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('RingPinsSystemDeflection',)


class RingPinsSystemDeflection(_2502.MountableComponentSystemDeflection):
    '''RingPinsSystemDeflection

    This is a mastapy class.
    '''

    TYPE = _RING_PINS_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'RingPinsSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2295.RingPins':
        '''RingPins: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2295.RingPins)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_load_case(self) -> '_6646.RingPinsLoadCase':
        '''RingPinsLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6646.RingPinsLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase is not None else None

    @property
    def power_flow_results(self) -> '_3842.RingPinsPowerFlow':
        '''RingPinsPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_3842.RingPinsPowerFlow)(self.wrapped.PowerFlowResults) if self.wrapped.PowerFlowResults is not None else None
