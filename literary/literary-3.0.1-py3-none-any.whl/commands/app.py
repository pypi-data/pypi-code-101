"""# Literary Application
"""
from copy import deepcopy
from importlib import import_module
from inspect import getmembers
from pathlib import Path
from traitlets import List, Unicode, default
from traitlets.config import Application, Configurable, catch_config_error
from ..core.config import find_project_config, load_project_config
from ..core.trait import Path as PathTrait

class LiteraryApp(Application):
    name = 'literary'
    description = 'A Literary application'
    aliases = {**Application.aliases, 'config-file': 'LiteraryApp.project_config_file'}
    project_config_file = PathTrait(help='Literary project configuration file').tag(config=True)
    classes = List()

    @default('classes')
    def _classes_default(self):
        modules = [import_module(f'..core.{n}', __package__) for n in ('exporter', 'package', 'preprocessor', 'project', 'test', 'transformers')]
        return [cls for m in modules for (_, cls) in getmembers(m) if isinstance(cls, type) and issubclass(cls, Configurable)]

    @default('project_config_file')
    def _project_config_file_default(self):
        return find_project_config(Path.cwd())

    @catch_config_error
    def initialize(self, argv=None):
        self.parse_command_line(argv)
        argv_config = deepcopy(self.config)
        self.load_app_config_file()
        self.update_config(argv_config)

    def load_app_config_file(self):
        config = load_project_config(self.project_config_file)
        self.update_config(config)