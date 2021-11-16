"""# Project Operations
Most Literary operations act upon the *project* - that is, the set of notebooks which are considered "packages". Here we define a `Configurable` which defines the configuration that refers to these notebooks
"""
from pathlib import Path
from traitlets import List, Unicode, default, observe, validate
from traitlets.config import Config, LoggingConfigurable
from .trait import Path as PathTrait

class ProjectOperator(LoggingConfigurable):
    project_path = PathTrait(help='Path to Literary project top-level directory').tag(config=True)
    packages_dir = Unicode('src', help='Path to Literary packages top-level directory').tag(config=True)

    @validate('project_path')
    def _validate_project_path(self, proposal):
        path = Path(proposal.value)
        if not path.exists():
            raise ValueError()
        return path

    def resolve_path(self, path):
        return self.project_path / path

    @property
    def packages_path(self) -> Path:
        return self.resolve_path(self.packages_dir)