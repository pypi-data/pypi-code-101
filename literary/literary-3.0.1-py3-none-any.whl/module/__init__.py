"""# Notebook Modules
"""
import sys
from pathlib import Path
from ..core.config import find_project_config, load_project_config
from .importer import ModuleImporter

def load_ipython_extension(ipython):
    """Load the import hook and setup the global state for the Literary extension.
    When IPython invokes this function, the determined package root path will be
    added to `sys.path`.

    :param ipython: IPython shell instance
    """
    path = find_project_config(Path.cwd())
    config = load_project_config(path)
    importer = ModuleImporter(config=config)
    importer.install_hook()
    importer.update_namespace(ipython.user_ns)