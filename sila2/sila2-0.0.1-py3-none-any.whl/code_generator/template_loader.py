import os

from jinja2 import FileSystemLoader

from sila2 import resource_dir


class TemplateLoader(FileSystemLoader):
    def __init__(self):
        super().__init__(searchpath=os.path.join(resource_dir, "code_generator_templates"), encoding="utf-8")

    def get_source(self, environment, template: str):
        return super().get_source(environment, f"{template}.jinja2")
