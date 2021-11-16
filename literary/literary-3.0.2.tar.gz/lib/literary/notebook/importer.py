"""# Import Hook
"""
import os
import sys
import traceback
import typing as tp
from pathlib import Path
from nbconvert import Exporter
from traitlets import Bool, Instance, Type, default
from ..core.exporter import LiteraryExporter
from ..core.project import ProjectOperator
from .finder import inject_loaders
from .loader import NotebookLoader
from .patch import patch

class NotebookImporter(ProjectOperator):
    exporter = Instance(Exporter)
    exporter_class = Type(LiteraryExporter, help='Exporter class').tag(config=True)
    set_except_hook = Bool(True, help='Overwrite `sys.excepthook` to correctly display tracebacks').tag(config=True)

    @default('exporter')
    def _exporter_default(self):
        return self.exporter_class(parent=self)

    def install_hook(self):
        """Install notebook import hook

    Don't allow the user to specify a custom search path, because we also need this to
    interoperate with the default Python module importers which use sys.path

    :return:
    """
        sys.path.append(str(self.packages_path))
        exporter = self.exporter_class(parent=self)

        def create_notebook_loader(fullname, path):
            return NotebookLoader(fullname, path, exporter=exporter)
        inject_loaders(sys.path_hooks, (create_notebook_loader, ['.ipynb']))
        if self.set_except_hook:
            sys.excepthook = traceback.print_exception

    def update_namespace(self, namespace):
        namespace.update({'patch': patch})