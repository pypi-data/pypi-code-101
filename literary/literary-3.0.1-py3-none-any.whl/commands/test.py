"""# Test Package Command
"""
import logging
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path
from traitlets import Int, List, Unicode, default
from ..core.test import ProjectTester
from .app import LiteraryApp

class LiteraryTestApp(LiteraryApp):
    description = 'Test literary notebooks in parallel'
    aliases = {**LiteraryApp.aliases, 'ignore': 'ProjectTester.ignore_patterns', 'jobs': 'ProjectTester.jobs', 'packages': 'ProjectTester.packages_dir', 'extras': 'ProjectTester.extra_sources'}
    source = List(trait=Unicode(help='source directory or notebooks to run')).tag(config=True)
    jobs = Int(allow_none=True, default_value=None, help='number of parallel jobs to run').tag(config=True)
    ignore = List(help='glob pattern to ignore during recursion', trait=Unicode()).tag(config=True)

    def start(self):
        tester = ProjectTester(parent=self)
        tester.run()