import logging
from importlib import import_module


class Module(object):
    def __init__(self, module_id=None):

        if module_id:
            self.module_id = module_id

    def _load_function(self, function_name: str):
        if function_name is None:
            return None

        try:
            module_path, _, fn_name = function_name.rpartition(".")
            function = getattr(import_module(module_path), fn_name)
            logging.info(f"Loaded function {function_name}")

            return function
        except Exception as e:
            logging.exception(f"Unable to load function {function_name}")
            return None