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
        # Insert <script>
        kwargs = {
            'data-isso': self.builder.config.isso_base_url,
            'src': self.builder.config.isso_base_url + '/js/embed.min.js',
        }
        self.body.append(self.starttag(node, 'script', '', **kwargs))
        self.body.append('</script>')

        self.body.append(self.starttag(node, 'section', ''))

    @staticmethod
    def depart(self, _):
        self.body.append('</section>')


class IssoDirective(Directive):
    """Isso ".. isso::" rst directive."""

    option_spec = {
        'id': directives.unchanged,
    }

    def run(self):
        """Executed by Sphinx.
        :returns: Single IssoNode instance with config values passed as arguments.
        :rtype: list
        """
        node = IssoNode()
        node['ids'] = ['isso-thread']

        return [node]


def setup(app:Sphinx):
    app.add_config_value('isso_base_url', None, {})
    app.add_directive('isso', IssoDirective)
    app.add_node(IssoNode, html=(IssoNode.visit, IssoNode.depart))

    return {'version': __version__}
