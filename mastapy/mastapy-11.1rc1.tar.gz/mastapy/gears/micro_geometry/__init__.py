'''__init__.py'''


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._523 import BiasModification
    from ._524 import FlankMicroGeometry
    from ._525 import FlankSide
    from ._526 import LeadModification
    from ._527 import LocationOfEvaluationLowerLimit
    from ._528 import LocationOfEvaluationUpperLimit
    from ._529 import LocationOfRootReliefEvaluation
    from ._530 import LocationOfTipReliefEvaluation
    from ._531 import MainProfileReliefEndsAtTheStartOfRootReliefOption
    from ._532 import MainProfileReliefEndsAtTheStartOfTipReliefOption
    from ._533 import Modification
    from ._534 import ParabolicRootReliefStartsTangentToMainProfileRelief
    from ._535 import ParabolicTipReliefStartsTangentToMainProfileRelief
    from ._536 import ProfileModification
