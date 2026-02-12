import os
import sys

# -- Path setup --------------------------------------------------------------

sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

project = 'My Documentation'
copyright = '2026'
author = 'Your Name'
release = '1.0'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',   # Needed for sitemap/robots support
]

templates_path = ['_templates']
exclude_patterns = []

# -- HTML output -------------------------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Enable General Index
html_use_index = True

# Add extra files like robots.txt
html_extra_path = ['robots.txt']

# -- Optional SEO Improvements ----------------------------------------------

html_show_sphinx = False
html_show_copyright = False

# -- Sitemap Configuration (Optional) ---------------------------------------

html_baseurl = 'https://infoiolo.readthedocs.io/en/latest/'

