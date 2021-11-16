'''__init__.py'''


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._1238 import AssemblyMethods
    from ._1239 import CalculationMethods
    from ._1240 import InterferenceFitDesign
    from ._1241 import InterferenceFitHalfDesign
    from ._1242 import StressRegions
    from ._1243 import Table4JointInterfaceTypes
