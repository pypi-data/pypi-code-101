import json
import importlib
from dataclasses import dataclass
from typing import Callable, Dict, List, Optional

from numba.pycc import CC


@dataclass
class TargetFunction:
    module: str
    function_name: str
    signature: str

    def get_callable(self) -> Callable:
        return getattr(importlib.import_module(self.module), self.function_name)


def get_source_wrapper(name: str, compiled_submodule: Optional[str] = None):
    class SourceModuleWrapper:
        pass
    module = [name, compiled_submodule, "dummy"] if compiled_submodule else [name, "dummy"]
    SourceModuleWrapper.__name__ = ".".join(module)  # TODO: think of a better way for doing this...
    return SourceModuleWrapper


class Registry:

    def __init__(
            self,
            target_functions: List[TargetFunction],
            export_on_start: bool = False,
            submodule: Optional[str] = None
    ):

        self.target_functions = target_functions
        self.modules: Dict = {}
        for target_function in target_functions:
            top_level, *submodules = target_function.module.split(".")
            submodules = submodules or ["default"]
            ext_name = "_".join(submodules)
            if target_function.module not in self.modules.keys():
                self.modules[ext_name] = {
                    "cc": CC(
                        extension_name=ext_name.replace(".", "_"),
                        source_module=get_source_wrapper(name=top_level, compiled_submodule=submodule)
                    ),
                    "ext_name": ext_name,
                    "functions": [target_function]
                }
            else:
                self.modules[ext_name]["functions"].append(target_function)
        if export_on_start:
            self.export()

    @staticmethod
    def from_dict(dictionary: Dict) -> 'Registry':
        return Registry(
            target_functions=[
                TargetFunction(**func_dict)
                for func_dict in dictionary.get("target_functions", [])
            ],
            export_on_start=dictionary.get("export_on_start", False),
            submodule=dictionary.get("submodule")
        )

    @staticmethod
    def from_json(filepath: str) -> 'Registry':
        with open(filepath, "r") as file:
            content = file.read()
        return Registry.from_dict(
            dictionary=json.loads(content)
        )

    def export(self):
        for _, module in self.modules.items():
            for target_function in module["functions"]:
                module["cc"].export(
                    exported_name=target_function.function_name,
                    sig=target_function.signature
                )(target_function.get_callable())

    def compile(self):
        for _, module in self.modules.items():
            module["cc"].compile()

    def ext_modules(self) -> List:
        return [
            module["cc"].distutils_extension()
            for _, module in self.modules.items()
        ]
