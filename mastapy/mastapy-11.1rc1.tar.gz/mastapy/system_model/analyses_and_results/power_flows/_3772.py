'''_3772.py

ClutchHalfPowerFlow
'''


from mastapy.system_model.part_model.couplings import _2304
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6533
from mastapy.system_model.analyses_and_results.power_flows import _3788
from mastapy._internal.python_net import python_net_import

_CLUTCH_HALF_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows', 'ClutchHalfPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('ClutchHalfPowerFlow',)


class ClutchHalfPowerFlow(_3788.CouplingHalfPowerFlow):
    '''ClutchHalfPowerFlow

    This is a mastapy class.
    '''

    TYPE = _CLUTCH_HALF_POWER_FLOW

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ClutchHalfPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2304.ClutchHalf':
        '''ClutchHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2304.ClutchHalf)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_load_case(self) -> '_6533.ClutchHalfLoadCase':
        '''ClutchHalfLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6533.ClutchHalfLoadCase)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase is not None else None
