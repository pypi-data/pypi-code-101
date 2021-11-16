'''__init__.py'''


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._508 import BevelGearMeshRating
    from ._509 import BevelGearRating
    from ._510 import BevelGearSetRating
