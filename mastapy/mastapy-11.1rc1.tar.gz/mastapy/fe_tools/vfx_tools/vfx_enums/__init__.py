'''__init__.py'''


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._1178 import ProSolveMpcType
    from ._1179 import ProSolveSolverType
