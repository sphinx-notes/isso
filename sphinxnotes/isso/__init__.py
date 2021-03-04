"""
    sphinxnotes.isso
    ~~~~~~~~~~~~~~~~

    :copyright: Copyright 2021 Shengyu Zhang
    :license: BSD, see LICENSE for details.
"""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sphinx.application import Sphinx

__title__= 'sphinxnotes-isso'
__license__ = 'BSD',
__version__ = '1.0a0'
__author__ = 'Shengyu Zhang'
__url__ = 'https://sphinx-notes.github.io/isso'
__description__ = 'Sphinx extension for embeding Isso comments in documents'
__keywords__ = 'documentation, sphinx, extension, comment, isso, disqus'

def setup(app:Sphinx) -> None:
    pass
