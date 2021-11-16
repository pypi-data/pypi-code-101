'''__init__.py'''


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._932 import KlingelnbergConicalGearDesign
    from ._933 import KlingelnbergConicalGearMeshDesign
    from ._934 import KlingelnbergConicalGearSetDesign
    from ._935 import KlingelnbergConicalMeshedGearDesign
