'''_3793.py

CycloidalAssemblyPowerFlow
'''


from mastapy.system_model.part_model.cycloidal import _2293
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6556
from mastapy.system_model.analyses_and_results.power_flows import _3851
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_ASSEMBLY_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows', 'CycloidalAssemblyPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('CycloidalAssemblyPowerFlow',)


class CycloidalAssemblyPowerFlow(_3851.SpecialisedAssemblyPowerFlow):
    '''CycloidalAssemblyPowerFlow

    This is a mastapy class.
    '''

    TYPE = _CYCLOIDAL_ASSEMBLY_POWER_FLOW

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CycloidalAssemblyPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2293.CycloidalAssembly':
        '''CycloidalAssembly: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2293.CycloidalAssembly)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def assembly_load_case(self) -> '_6556.CycloidalAssemblyLoadCase':
        '''CycloidalAssemblyLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6556.CycloidalAssemblyLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase is not None else None
