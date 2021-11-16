'''__init__.py'''


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._2082 import AlignConnectedComponentOptions
    from ._2083 import AlignmentMethod
    from ._2084 import AlignmentMethodForRaceBearing
    from ._2085 import AlignmentUsingAxialNodePositions
    from ._2086 import AngleSource
    from ._2087 import BaseFEWithSelection
    from ._2088 import BatchOperations
    from ._2089 import BearingNodeAlignmentOption
    from ._2090 import BearingNodeOption
    from ._2091 import BearingRaceNodeLink
    from ._2092 import BearingRacePosition
    from ._2093 import ComponentOrientationOption
    from ._2094 import ContactPairWithSelection
    from ._2095 import CoordinateSystemWithSelection
    from ._2096 import CreateConnectedComponentOptions
    from ._2097 import DegreeOfFreedomBoundaryCondition
    from ._2098 import DegreeOfFreedomBoundaryConditionAngular
    from ._2099 import DegreeOfFreedomBoundaryConditionLinear
    from ._2100 import ElectricMachineDataSet
    from ._2101 import ElectricMachineDynamicLoadData
    from ._2102 import ElementFaceGroupWithSelection
    from ._2103 import ElementPropertiesWithSelection
    from ._2104 import FEEntityGroupWithSelection
    from ._2105 import FEExportSettings
    from ._2106 import FEPartWithBatchOptions
    from ._2107 import FEStiffnessGeometry
    from ._2108 import FEStiffnessTester
    from ._2109 import FESubstructure
    from ._2110 import FESubstructureExportOptions
    from ._2111 import FESubstructureNode
    from ._2112 import FESubstructureNodeModeShape
    from ._2113 import FESubstructureNodeModeShapes
    from ._2114 import FESubstructureType
    from ._2115 import FESubstructureWithBatchOptions
    from ._2116 import FESubstructureWithSelection
    from ._2117 import FESubstructureWithSelectionComponents
    from ._2118 import FESubstructureWithSelectionForHarmonicAnalysis
    from ._2119 import FESubstructureWithSelectionForModalAnalysis
    from ._2120 import FESubstructureWithSelectionForStaticAnalysis
    from ._2121 import GearMeshingOptions
    from ._2122 import IndependentMastaCreatedCondensationNode
    from ._2123 import LinkComponentAxialPositionErrorReporter
    from ._2124 import LinkNodeSource
    from ._2125 import MaterialPropertiesWithSelection
    from ._2126 import NodeBoundaryConditionStaticAnalysis
    from ._2127 import NodeGroupWithSelection
    from ._2128 import NodeSelectionDepthOption
    from ._2129 import OptionsWhenExternalFEFileAlreadyExists
    from ._2130 import PerLinkExportOptions
    from ._2131 import PerNodeExportOptions
    from ._2132 import RaceBearingFE
    from ._2133 import RaceBearingFESystemDeflection
    from ._2134 import RaceBearingFEWithSelection
    from ._2135 import ReplacedShaftSelectionHelper
    from ._2136 import SystemDeflectionFEExportOptions
    from ._2137 import ThermalExpansionOption
