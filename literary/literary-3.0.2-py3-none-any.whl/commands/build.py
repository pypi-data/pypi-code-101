"""# Build Package Command
"""
from pathlib import Path
from traitlets import List, Unicode, default
from ..core.package import PackageBuilder
from .app import LiteraryApp

class LiteraryBuildApp(LiteraryApp):
    description = 'Build a pure-Python package from a set of Jupyter notebooks'
    aliases = {**LiteraryApp.aliases, 'ignore': 'PackageBuilder.ignore_patterns', 'output': 'PackageBuilder.generated_dir', 'packages': 'PackageBuilder.packages_dir'}
    flags = {'clear': ({'PackageBuilder': {'clear_generated': True}}, 'Clear generated directory before building.')}

    def start(self):
        builder = PackageBuilder(parent=self)
        builder.build()