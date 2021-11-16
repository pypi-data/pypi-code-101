"""# Import Hook
"""
import sys
from pathlib import Path
from ..notebook.importer import NotebookImporter
from ..notebook.patch import patch

class ModuleImporter(NotebookImporter):
    pass

    def determine_package_name(self, path: Path) -> str:
        """Determine the corresponding importable name for a package directory given by
    a particular file path. Return `None` if path is not contained within `sys.path`.

    :param path: path to package
    :return:
    """
        for p in sys.path:
            if str(path) == p:
                continue
            try:
                relative_path = path.relative_to(p)
            except ValueError:
                continue
            return '.'.join(relative_path.parts)
        return None

    def install_hook(self):
        """Install notebook import hook

    Don't allow the user to specify a custom search path, because we also need this to
    interoperate with the default Python module importers which use sys.path

    :return:
    """
        cwd = Path.cwd()
        sys.path = [p for p in sys.path if Path(p).resolve() != cwd]
        super().install_hook()

    def update_namespace(self, namespace):
        cwd = Path.cwd()
        namespace.update({'__package__': self.determine_package_name(cwd), 'patch': patch})