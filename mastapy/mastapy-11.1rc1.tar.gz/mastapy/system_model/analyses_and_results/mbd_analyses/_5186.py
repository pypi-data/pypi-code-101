'''_5186.py

PulleyMultibodyDynamicsAnalysis
'''


from typing import List

from mastapy._internal import constructor, conversion
from mastapy._math.vector_3d import Vector3D
from mastapy.system_model.part_model.couplings import _2315, _2312
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.analyses_and_results.static_loads import _6643, _6555
from mastapy.system_model.analyses_and_results.mbd_analyses.reporting import _5236
from mastapy.system_model.analyses_and_results.mbd_analyses import _5128
from mastapy._internal.python_net import python_net_import

_PULLEY_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses', 'PulleyMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('PulleyMultibodyDynamicsAnalysis',)


class PulleyMultibodyDynamicsAnalysis(_5128.CouplingHalfMultibodyDynamicsAnalysis):
    '''PulleyMultibodyDynamicsAnalysis

    This is a mastapy class.
    '''

    TYPE = _PULLEY_MULTIBODY_DYNAMICS_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'PulleyMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def pulley_torque(self) -> 'List[float]':
        '''List[float]: 'PulleyTorque' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_list_float(self.wrapped.PulleyTorque)
        return value

    @property
    def force_on_pulley_from_belts(self) -> 'Vector3D':
        '''Vector3D: 'ForceOnPulleyFromBelts' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_vector3d(self.wrapped.ForceOnPulleyFromBelts)
        return value

    @property
    def component_design(self) -> '_2315.Pulley':
        '''Pulley: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _2315.Pulley.TYPE not in self.wrapped.ComponentDesign.__class__.__mro__:
            raise CastException('Failed to cast component_design to Pulley. Expected: {}.'.format(self.wrapped.ComponentDesign.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentDesign.__class__)(self.wrapped.ComponentDesign) if self.wrapped.ComponentDesign is not None else None

    @property
    def component_load_case(self) -> '_6643.PulleyLoadCase':
        '''PulleyLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        '''

        if _6643.PulleyLoadCase.TYPE not in self.wrapped.ComponentLoadCase.__class__.__mro__:
            raise CastException('Failed to cast component_load_case to PulleyLoadCase. Expected: {}.'.format(self.wrapped.ComponentLoadCase.__class__.__qualname__))

        return constructor.new_override(self.wrapped.ComponentLoadCase.__class__)(self.wrapped.ComponentLoadCase) if self.wrapped.ComponentLoadCase is not None else None

    @property
    def peak_pulley_torque(self) -> 'List[_5236.DynamicTorqueResultAtTime]':
        '''List[DynamicTorqueResultAtTime]: 'PeakPulleyTorque' is the original name of this property.

        Note:
            This property is readonly.
        '''

        value = conversion.pn_to_mp_objects_in_list(self.wrapped.PeakPulleyTorque, constructor.new(_5236.DynamicTorqueResultAtTime))
        return value
