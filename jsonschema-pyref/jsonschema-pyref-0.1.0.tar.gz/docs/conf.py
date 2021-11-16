# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('..'))

# -- Project information -----------------------------------------------------

project = 'jsonschema-pyref'
copyright = '2021, E. Madison Bray'
author = 'E. Madison Bray'

# The full version, including alpha/beta/rc tags
import jsonschema_pyref
release = jsonschema_pyref.__version__


# -- General configuration ---------------------------------------------------

import warnings
# Silence some Numpy compatibility warnings; this can happen in some cases
# if modules like scipy or cython were compiled against a different numpy
# version; normally this shouldn't happen but it does with some particular
# combinations of conda packages
warnings.filterwarnings("ignore", message="numpy.ufunc size changed")


# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.intersphinx',
    # for supporting numpydoc-style docstrings, but less opinionated about
    # the rest of document structure than the original numpydoc module
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',

    'sphinx_rtd_theme',
    'sphinxcontrib.spelling',

    'm2r2'  # for markdown support
]

# Assume text marked up `like_this` is a reference to a Python object by
# default
default_role = 'py:obj'

nitpicky = os.environ.get('SPHINX_NITPICKY', '0') != '0'

## Setup extensions ##########################################################


### autosectionlabel configuration

autosectionlabel_prefix_document = True
autosectionlabel_maxdepth = 2


### napoleon configuration

napoleon_google_docstring = False  # use numpydoc instead

# Custom section headings for Networks
napoleon_custom_sections = [
    'Publication',
    'Task',
    ('Constraints', 'params_style')
]

# monkey-patch napoleon to better handle optional parameters in numpydoc
# docstrings; see https://github.com/sphinx-doc/sphinx/issues/6861

def _fixup_napoleon_numpydoc():
    from sphinx.locale import _
    from sphinx.ext.napoleon import NumpyDocstring

    def _process_optional_params(self, fields):
        """
        Split a fields list into separate lists of positional parameters and
        keyword parameters.

        Possibly moves some fields out of their original documented order,
        though in practice, in most cases, optional/keyword parameters should
        always be listed after positional parameters.

        For Numpydoc, a parameter is treated as a keyword parameter if its type
        list ends with the keyword "optional".  In this case, the "optional" is
        removed from its type list, and instead the text "(optional)" is
        prepended to the field description.
        """

        positional = []
        keyword = []

        for name, type_, desc in fields:
            types = [t.strip() for t in type_.split(',')]
            optional = types and types[-1].lower() == 'optional'
            if optional:
                type_ = ', '.join(types[:-1])

                if not desc:
                    desc = ['']
                desc[0] = ('*(optional)* – ' + desc[0]).rstrip()

            if optional or name.startswith(r'\*\*'):
                keyword.append((name, type_, desc))
            else:
                positional.append((name, type_, desc))

        return positional, keyword

    def _parse_parameters_section(self, section):
        fields = self._consume_fields()
        pos_fields, kw_fields = self._process_optional_params(fields)
        if self._config.napoleon_use_param:
            lines = self._format_docutils_params(pos_fields)
        else:
            lines = self._format_fields(_('Parameters'), pos_fields)

        if self._config.napoleon_use_keyword:
            if self._config.napoleon_use_param:
                lines = lines[:-1]
            lines.extend(self._format_docutils_params(
                kw_fields, field_role='keyword', type_role='kwtype'))
        else:
            lines.extend(self._format_fields(
                _('Keyword Arguments'), kw_fields))

        return lines

    def _parse_other_parameters_section(self, section):
        fields = self._consume_fields()
        pos_fields, kw_fields = self._process_optional_params(fields)
        return self._format_fields(
                _('Other Parameters'), pos_fields + kw_fields)

    NumpyDocstring._process_optional_params = _process_optional_params
    NumpyDocstring._parse_parameters_section = _parse_parameters_section
    NumpyDocstring._parse_other_parameters_section = \
            _parse_other_parameters_section


_fixup_napoleon_numpydoc()


### autodoc configuration

autodoc_default_options = {
    'members': True,
    'show-inheritance': True
}


##############################################################################

# When including verbatim reStructuredText code blocks, don't highlight nested
# code blocks in the examples (this ruins the surprise!)
highlight_options = {
    'rst': {'handlecodeblocks': False}
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Intersphinx mappings for API docs from other packages
intersphinx_mapping = {
    'jsonschema': ('https://python-jsonschema.readthedocs.io/en/stable/', None),
    'python': ('https://docs.python.org/3/', None),
}

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
