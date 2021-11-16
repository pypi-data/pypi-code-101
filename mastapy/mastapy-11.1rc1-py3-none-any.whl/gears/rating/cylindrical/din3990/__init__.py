'''__init__.py'''


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._487 import DIN3990GearSingleFlankRating
    from ._488 import DIN3990MeshSingleFlankRating
