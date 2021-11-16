'''__init__.py'''


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._1508 import ScriptingSetup
    from ._1509 import UserDefinedPropertyKey
    from ._1510 import UserSpecifiedData
