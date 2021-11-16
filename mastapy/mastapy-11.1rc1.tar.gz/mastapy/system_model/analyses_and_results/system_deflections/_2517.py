'''_2517.py

RollingRingAssemblySystemDeflection
'''


from mastapy.system_model.part_model.couplings import _2322
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6648
from mastapy.system_model.analyses_and_results.power_flows import _3844
from mastapy.system_model.analyses_and_results.system_deflections import _2526
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_ASSEMBLY_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'RollingRingAssemblySystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('RollingRingAssemblySystemDeflection',)


class RollingRingAssemblySystemDeflection(_2526.SpecialisedAssemblySystemDeflection):
    '''RollingRingAssemblySystemDeflection

    This is a mastapy class.
    '''

    TYPE = _ROLLING_RING_ASSEMBLY_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'RollingRingAssemblySystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2322.RollingRingAssembly':
        '''RollingRingAssembly: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_2322.RollingRingAssembly)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def assembly_load_case(self) -> '_6648.RollingRingAssemblyLoadCase':
        '''RollingRingAssemblyLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_6648.RollingRingAssemblyLoadCase)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase is not None else None

    @property
    def power_flow_results(self) -> '_3844.RollingRingAssemblyPowerFlow':
        '''RollingRingAssemblyPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        '''

        return constructor.new(_3844.RollingRingAssemblyPowerFlow)(self.wrapped.PowerFlowResults) if self.wrapped.PowerFlowResults is not None else None
