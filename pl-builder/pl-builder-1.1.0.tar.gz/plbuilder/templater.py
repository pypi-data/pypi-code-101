import os
from functools import lru_cache
from pathlib import Path
from typing import Optional, Union
from typing_extensions import TypedDict

import jinja2

DEFAULT_TEMPLATE = """
{% include "always_imports.j2" %}

{% include "author.j2" %}

{% include "always_body.j2" %}
"""


class TemplateData(TypedDict):
    title: str


def get_environment(
    local_path: Optional[Union[str, Path]] = None
) -> jinja2.Environment:
    path = Path(local_path or os.getcwd())
    plbuild_loader = jinja2.FileSystemLoader(path / "plbuild" / "templates")
    local_loader = jinja2.FileSystemLoader(path / "templates")
    default_loader = jinja2.PackageLoader("plbuilder")
    choice_loader = jinja2.ChoiceLoader([plbuild_loader, local_loader, default_loader])
    return jinja2.Environment(loader=choice_loader)


def render_template(name: str, data: TemplateData) -> str:
    env = get_environment()
    template = env.get_template(name)
    return template.render(**data)


def output_template(name: str, data: TemplateData, path: Union[str, Path]):
    output = render_template(name, data)
    Path(path).write_text(output)
