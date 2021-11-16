'''_5099.py

BeltDriveMultibodyDynamicsAnalysis
'''


from typing import List

from mastapy.system_model.part_model.couplings import _2301, _2311
from mastapy._internal import constructor, conversion
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.analyses_and_results.static_loads import _6521, _6554
from mastapy.system_model.analyses_and_results.mbd_analyses import _5186, _5199
from mastapy._internal.python_net import python_net_import

_BELT_DRIVE_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses', 'BeltDriveMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('BeltDriveMultibodyDynamicsAnalysis',)


class BeltDriveMultibodyDynamicsAnalysis(_5199.SpecialisedAssemblyMultibodyDynamicsAnalysis):
    '''BeltDriveMultibodyDynamicsAnalysis

    This is a mastapy class.
    '''

    TYPE = _BELT_DRIVE_MULTIBODY_DYNAMICS_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BeltDriveMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2301.BeltDrive':
        '''BeltDrive: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2301.BeltDrive.TYPE not in self.wrapped.AssemblyDesign.__class__.__mro__:
            raise CastException('Failed to cast assembly_design to BeltDrive. Expected: {}.'.format(self.wrapped.AssemblyDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.AssemblyDesign.__class__)(self.wrapped.AssemblyDesign) if self.wrapped.AssemblyDesign is not None else None

    @property
    def assembly_load_case(self) -> '_6521.BeltDriveLoadCase':
        '''BeltDriveLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _6521.BeltDriveLoadCase.TYPE not in self.wrapped.AssemblyLoadCase.__class__.__mro__:
            raise CastException('Failed to cast assembly_load_case to BeltDriveLoadCase. Expected: {}.'.format(self.wrapped.AssemblyLoadCase.__class__.__qualname__))

        return constructor.new_override(self.wrapped.AssemblyLoadCase.__class__)(self.wrapped.AssemblyLoadCase) if self.wrapped.AssemblyLoadCase is not None else None

    @property
    def pulleys(self) -> 'List[_5186.PulleyMultibodyDynamicsAnalysis]':
        '''List[PulleyMultibodyDynamicsAnalysis]: 'Pulleys' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.Pulleys, constructor.new(_5186.PulleyMultibodyDynamicsAnalysis))
        return value
