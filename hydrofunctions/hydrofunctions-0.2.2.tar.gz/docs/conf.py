#!/usr/bin/env python
# -*- coding: utf-8 -*-
#


#####################################
#
#   This section was suggested by ReadTheDocs here:
#   http://read-the-docs.readthedocs.io/en/latest/faq.html#i-get-import-errors-on-libraries-that-depend-on-c-modules
#
#    Apparently, they try to do a complete build of your project, but they
#    choke when they try to import and build numpy and pandas, due to these
#    relying extensively on C modules. So I need to mock these out.
#
#    Update 2018-02-15: Importing MagicMock during by docs build using
#    'make html' is leading to a RecursionError:
#    'maximum recursion depth exceeded while calling a Python object'.
#    I was able to avoid the RecursionError during 'make html' by commenting out
#    the following block, which imports MagicMock.
#    Now we need to see if the original
#    error during the ReadTheDocs build still occurs.
#
####################Added Stuff Below ################################
#
#
# import sys
# from unittest.mock import MagicMock
#
# class Mock(MagicMock):
#    @classmethod
#    def __getattr__(cls, name):
#            return Mock()
#
# MOCK_MODULES = ['pygtk', 'gtk', 'gobject', 'argparse', 'numpy', 'pandas']
# sys.modules.update((mod_name, Mock()) for mod_name in MOCK_MODULES)
#
################ Added Stuff Above ###################################

# hydrofunctions documentation build configuration file, created by
# sphinx-quickstart on Tue Jul  9 22:26:36 2013.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os

# If extensions (or modules to document with autodoc) are in another
# directory, add these directories to sys.path here. If the directory is
# relative to the documentation root, use os.path.abspath to make it
# absolute, like shown here.
sys.path.insert(0, os.path.abspath("."))

# Get the project root dir, which is the parent dir of this
cwd = os.getcwd()
project_root = os.path.dirname(cwd)

# Insert the project root dir as the first element in the PYTHONPATH.
# This lets us ensure that the source package is imported, and that its
# version is used.
sys.path.insert(0, project_root)

import hydrofunctions

# -- General configuration ---------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.autosectionlabel",
    #'sphinxcontrib.napoleon',
    "sphinx.ext.napoleon",
    "nbsphinx",
    "sphinx.ext.mathjax",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix of source filenames.
source_suffix = ".rst"

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = "index"

# Renames internal refs so that they include page #.
# See http://www.sphinx-doc.org/en/stable/ext/autosectionlabel.html#confval-autosectionlabel_prefix_document
autosectionlabel_prefix_document = True

# General information about the project.
project = "Hydrofunctions"
copyright = "Copyright 2016-2021, Martin Roberge and Hydrofunctions contributors"

# The version info for the project you're documenting, acts as replacement
# for |version| and |release|, also used in various other places throughout
# the built documents.
#
# The short X.Y version.
version = hydrofunctions.__version__
# The full version, including alpha/beta/rc tags.
release = hydrofunctions.__version__

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
# language = None

# There are two options for replacing |today|: either, you set today to
# some non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = [
    "_build",
    "**.ipynb_checkpoints",
]

# The reST default role (used for this markup: `text`) to use for all
# documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

highlight_language = "python"
# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built
# documents.
keep_warnings = True


# -- Options for HTML output -------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
# The new default is alabaster.
# The old default is now 'classic'.
# more themes: http://www.sphinx-doc.org/en/stable/theming.html
# html_theme = 'bizstyle'
html_theme = "alabaster"

html_theme_options = {
    "github_user": "mroberge",
    "github_repo": "hydrofunctions",
    "description": "Python tools for hydrology",
    "logo": "hf-logo.svg",
    "logo_name": True,
    "github_button": True,
    "github_type": "watch",
    "github_count": True,
    "github_banner": True,
    "fixed_sidebar": False,
    "sidebar_width": "230px",
    "show_related": True,
    "analytics_id": "UA-73178522-4",
    "head_font_family": "Roboto, Tahoma, Verdana, Segoe, sans-serif",
    "font_family": "Tahoma, Verdana, Segoe, sans-serif",
    "code_font_family": "Lucida Console, Lucida Sans Typewriter, monospace",
    "show_relbars": True,
    "show_powered_by": False,
    #'prev_next_buttons_location': 'bottom'
}
# Theme options are theme-specific and customize the look and feel of a
# theme further.  For a list of options available for each theme, see the
# documentation.

# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
# html_title = 'Hydrofunctions'

# A shorter title for the navigation bar.  Default is the same as
# html_title.
# html_short_title = None

# The name of an image file (relative to this directory) to place at the
# top of the sidebar.
html_logo = "_static/hf-logo.svg"

# The name of an image file (within the static path) to use as favicon
# of the docs.  This file should be a Windows icon file (.ico) being
# 16x16 or 32x32 pixels large.
html_favicon = "_static/favicon.ico"

# Add any paths that contain custom static files (such as style sheets)
# here, relative to this directory. They are copied after the builtin
# static files, so a file named "default.css" will overwrite the builtin
# "default.css".
html_static_path = ["_static"]

# If not '', a 'Last updated on:' timestamp is inserted at every page
# bottom, using the given strftime format.
html_last_updated_fmt = "%b %d, %Y"

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {}

# This will add links to all of the documents in the sidebar.
html_sidebars = {
    "**": ["globaltoc.html", "relations.html", "sourcelink.html", "searchbox.html",],
}

# Additional templates that should be rendered to pages, maps page names
# to template names.
# html_additional_pages = {}

# If false, no module index is generated.
# html_domain_indices = True

# If false, no index is generated.
# html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, "Created using Sphinx" is shown in the HTML footer.
# Default is True.
html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer.
# Default is True.
html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages
# will contain a <link> tag referring to it.  The value of this option
# must be the base URL from which the finished HTML is served.
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = "hydrofunctionsdoc"


# -- Options for LaTeX output ------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    #'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    #'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass
# [howto/manual]).
latex_documents = [
    (
        "index",
        "hydrofunctions.tex",
        u"HydroFunctions Documentation",
        u"Martin Roberge",
        "manual",
    ),
]

# The name of an image file (relative to this directory) to place at
# the top of the title page.
# latex_logo = None

# For "manual" documents, if this is true, then toplevel headings
# are parts, not chapters.
# latex_use_parts = False

# If true, show page references after internal links.
# latex_show_pagerefs = False

# If true, show URL addresses after external links.
# latex_show_urls = False

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
# latex_domain_indices = True


# -- Options for manual page output ------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ("index", "hydrofunctions", u"HydroFunctions User's Guide", [u"Martin Roberge"], 1)
]

# If true, show URL addresses after external links.
# man_show_urls = False


# -- Options for Texinfo output ----------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        "index",
        "hydrofunctions",
        u"HydroFunctions User's Guide",
        u"Martin Roberge",
        "hydrofunctions",
        "A set of convenience functions for exploring water data.",
        "Miscellaneous",
    ),
]

# Documents to append as an appendix to all manuals.
# texinfo_appendices = []

# If false, no module index is generated.
# texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
# texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
# texinfo_no_detailmenu = False
