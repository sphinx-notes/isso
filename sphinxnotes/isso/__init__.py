"""
    sphinxnotes.isso
    ~~~~~~~~~~~~~~~~

    This extension is modified from sphinxcontrib-disqus.

    :copyright: Copyright 2021 Shengyu Zhang
    :copyright: Copyright 2016 Robpol86
    :license: BSD, see LICENSE for details.
"""

from __future__ import annotations
from typing import TYPE_CHECKING
import posixpath

from docutils import nodes
from docutils.parsers.rst import directives, Directive

if TYPE_CHECKING:
    from sphinx.application import Sphinx

__title__= 'sphinxnotes-isso'
__license__ = 'BSD',
__version__ = '1.0a0'
__author__ = 'Shengyu Zhang'
__url__ = 'https://sphinx-notes.github.io/isso'
__description__ = 'Sphinx extension for embeding Isso comments in documents'
__keywords__ = 'documentation, sphinx, extension, comment, isso, disqus'

class IssoNode(nodes.General, nodes.Element):

    @staticmethod
    def visit(self, node):
        self.body.append(self.starttag(node, 'section', ''))

    @staticmethod
    def depart(self, _):
        self.body.append('</section>')


class IssoDirective(Directive):
    """Isso ".. isso::" rst directive."""

    def run(self):
        """Executed by Sphinx.
        :returns: Single IssoNode instance with config values passed as arguments.
        :rtype: list
        """

        node = IssoNode()
        node['ids'] = ['isso-thread']

        return [node]

def on_html_page_context(app:Sphinx, pagename:str, templatename:str, context,
                         doctree:nodes.document) -> None:
    """Called when the HTML builder has created a context dictionary to render a template with.

    Conditionally adding isso client script to <head /> if the directive is used in a page.

    :param sphinx.application.Sphinx app: Sphinx application object.
    :param str pagename: Name of the page being rendered (without .html or any file extension).
    :param str templatename: Page name with .html.
    :param dict context: Jinja2 HTML context.
    :param docutils.nodes.document doctree: Tree of docutils nodes.
    """
    if not doctree or not doctree.next_node(IssoNode):
        # Only add for document which contains isso node
        return
    kwargs = {
        'data-isso': app.config.isso_base_url,
    }
    app.add_js_file(posixpath.join(app.config.isso_base_url, 'js/embed.min.js'),
                    **kwargs)


def setup(app:Sphinx):
    app.add_config_value('isso_base_url', None, {})
    app.add_directive('isso', IssoDirective)
    app.add_node(IssoNode, html=(IssoNode.visit, IssoNode.depart))
    app.connect('html-page-context', on_html_page_context)

    return {'version': __version__}
