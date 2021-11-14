from pathlib import Path
from typing import Optional
import fire
import shutil
import os

from pyexlatex.logic.output.api.formats import OutputFormats

from plbuilder.builder import (
    build_all,
    build_by_file_path,
)
from plbuilder.autoreloader import autobuild
from plbuilder.creator import create_template
from plbuilder.init import initialize_project
from plbuilder.paths import templates_path_func
from plbuilder.templater import DEFAULT_TEMPLATE


def build(
    file_path: Optional[str] = None, output_format: Optional[OutputFormats] = None
):
    """
    Create slides and handout PDFs from plbuilder pyexlatex templates.
    Passing no arguments will build all templates.

    :param file_path: path of template from which to build PDFs
    :param output_format: the file type of the output, currently 'pdf' and 'html' are supported.
        If not passed, will fall back to the setting of DEFAULT_OUTPUT_FORMAT in the file. If that
        is not passed, will default to 'pdf'
    :return: None
    """
    if file_path is None:
        build_all(desired_output_format=output_format)
    else:
        build_by_file_path(file_path, desired_output_format=output_format)


def create(doc_type: str, name: str):
    """
    Creates a slide template using the passed name

    :param doc_type: 'presentation', 'document', or the name of a custom template
    :param name: Display name, will be standardized to snakecase and lowercase for use in the file name
    :return:
    """
    doc_type = doc_type.lower().strip()
    create_template(doc_type, name)


def override(template_name: str):
    """
    Overrides a default template by copying it into plbuild/templates

    :param template_name: 'always_body', 'always_imports', 'author', 'document', 'document_build',
     'document_config', 'organization', 'presentation', 'presentation_build', 'presentation_config',
      or the name of a custom template
    :return:
    """
    template_file = f"{template_name}.j2"
    templates_path = Path("plbuild") / "templates"
    if not templates_path.exists():
        raise ValueError(
            "Could not find plbuild directory, navigate to project root or call init"
        )
    orig_template_path = templates_path_func(template_file)
    if os.path.exists(orig_template_path):
        print(f"Overriding {template_name} by outputting to {templates_path}")
        shutil.copy(orig_template_path, templates_path)
    else:
        # Custom template name
        print(
            f"Creating new custom document type {template_name} by outputting to {templates_path}"
        )
        (templates_path / template_file).write_text(DEFAULT_TEMPLATE)


def init():
    """
    Creates a plbuilder project in the current directory


    :return:
    """
    initialize_project()


def main():
    return fire.Fire(
        {
            "build": build,
            "create": create,
            "init": init,
            "autobuild": autobuild,
            "override": override,
        }
    )


if __name__ == "__main__":
    main()
