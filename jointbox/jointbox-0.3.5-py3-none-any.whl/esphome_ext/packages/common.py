#    JointBox CLI
#    Copyright (C) 2021 Dmitry Berezovsky
#    The MIT License (MIT)
#
#    Permission is hereby granted, free of charge, to any person obtaining
#    a copy of this software and associated documentation files
#    (the "Software"), to deal in the Software without restriction,
#    including without limitation the rights to use, copy, modify, merge,
#    publish, distribute, sublicense, and/or sell copies of the Software,
#    and to permit persons to whom the Software is furnished to do so,
#    subject to the following conditions:
#
#    The above copyright notice and this permission notice shall be
#    included in all copies or substantial portions of the Software.
#
#    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#    EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#    MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#    IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
#    CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
#    TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
#    SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from typing import Union, Optional, Any, Dict, List, Callable, Sequence

from cli_rack.loader import BaseLocatorDef

PackageConfig = dict
PackageSource = Union[dict, str]
PackageParams = Dict[str, Any]


class MacroDef(object):
    def __init__(self, name: str, package: "PackageDefinition") -> None:
        self.name = name
        self.package: PackageDefinition = package
        self.description: Optional[str] = None
        self.params_def: Dict[str, Dict] = {}
        self.params_validator: Callable[[Any], Any] = lambda val: val
        self.body: Dict[str, Any] = {}


class BaseMeta(object):
    def __init__(self) -> None:
        super().__init__()
        self.author: Optional[str] = None
        self.name: Optional[str] = None
        self.description: Optional[str] = None
        self.license: Optional[str] = None
        self.tags: List[str] = []
        self.macros_def: Dict[str, MacroDef] = {}
        self.variables: Dict[str, Dict] = {}


class RootMeta(BaseMeta):
    pass


class PackageMeta(BaseMeta):
    def __init__(self) -> None:
        super().__init__()
        self.params_def: Dict[str, Dict] = {}
        self.export: Sequence[Dict[str, Any]] = []
        self.params_validator: Callable[[Any], Any] = lambda val: val


class PackageDefinition(object):
    """
    The class representing package instantiated with particular params
    """

    __VIRTUAL_ROOT = "VIRTUALROOT"
    __ROOT = "ROOT"

    def __init__(self, local_name: str, parent: Optional["PackageDefinition"] = None) -> None:
        self.local_name: str = local_name
        self.parent: Optional[PackageDefinition] = parent
        self.content: Optional[dict] = None
        self.external_ref: Optional[str] = None
        self.locator: Optional[BaseLocatorDef] = None
        self.file_system_location: Optional[str] = None
        self.params: PackageParams = {}
        self.macros: Dict[str, MacroDef] = {}
        self.meta: PackageMeta = PackageMeta()
        self.outputs: Dict[str, Dict] = {}
        self.packages: Dict[str, PackageDefinition] = {}
        self.evaluated_content: Optional[dict] = None

    @classmethod
    def create_root(self, content: Optional[dict], fs_location: Optional[str]) -> "PackageDefinition":
        res = PackageDefinition(self.__ROOT, None)
        res.file_system_location = fs_location
        res.content = content
        return res

    @classmethod
    def create_virtual_root(self, content: Optional[dict], fs_location: Optional[str]) -> "PackageDefinition":
        res = PackageDefinition(self.__VIRTUAL_ROOT, None)
        res.file_system_location = fs_location
        res.content = content
        return res

    @property
    def is_root(self):
        return self.parent is None

    @property
    def is_virtual_root(self):
        return self.local_name == self.__VIRTUAL_ROOT

    @property
    def instance_name(self):
        return self.local_name

    @classmethod
    def __get_depth_helper(cls, package: "PackageDefinition", level=0):
        if package.parent is not None:
            return cls.__get_depth_helper(package.parent, level + 1)
        return level

    def get_depth(self) -> int:
        if self.is_root:
            return 0
        return self.__get_depth_helper(self)
