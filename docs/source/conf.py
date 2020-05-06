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
from typing import Dict
from typing import List

sys.path.insert(0, os.path.abspath("../../src"))


# -- Project information -----------------------------------------------------

about: Dict[str, str] = {}
with open("../../src/arsenal/__version__.py") as f:
    exec(f.read(), about)
project = about["__title__"]
copyright = f'2020, {about["__author__"]}'
author = about["__author__"]

# The full version, including alpha/beta/rc tags
release = about["__version__"]


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "autoapi.extension",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.coverage",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
]


# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns: List[str] = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]


# -- Extension configuration -------------------------------------------------
# -- Options for intersphinx extension ---------------------------------------
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "moviepy": ("https://zulko.github.io/moviepy", None),
    "numpy": ("https://docs.scipy.org/doc/numpy", None),
    "PIL": ("https://pillow.readthedocs.io/en/stable/", None),
    "pandas": ("http://pandas.pydata.org/pandas-docs/stable/", None),
    "torch": ("https://pytorch.org/docs/stable", None),
}

# Subclasses should show parent classes docstrings if they don't override them.
autodoc_inherit_docstrings = True

# Mock out external dependencies that don't provide types present in any signature.
# Why?
# - Installing all the dependencies is very slow
# - Not all dependencies can be installed using pip along
# - Conda support is limited on RTD by the worker machines only having 512MB RAM which is insufficient
#   for loading the conda-forge channel under which many of our dependencies lie.
# If we mock out everything we don't get proper types in the docs due to sphinx-autodoc-typehints
# not being able to resolve the types... So, in order to resolve the above the best we can do is
# install numpy and torch, (Pillow is already installed on RTD) and mock the rest

autodoc_mock_imports = ["torchvision"]

# -- Options for autoapi extension ---------------------------------------
autoapi_type = "python"
autoapi_dirs = ["../../src"]
