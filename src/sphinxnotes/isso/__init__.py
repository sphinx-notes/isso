"""
    sphinxnotes.isso
    ~~~~~~~~~~~~~~~~

    This extension is modified from sphinxcontrib-disqus.

    :copyright: Copyright 2021 Shengyu Zhang
    :copyright: Copyright 2016 Robpol86
    :license: BSD, see LICENSE for details.
"""

from __future__ import annotations
from typing import TYPE_CHECKING, Any, Tuple
import posixpath

from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.docutils import SphinxDirective
from sphinx.writers.html5 import HTML5Translator

if TYPE_CHECKING:
    from sphinx.application import Sphinx
from sphinx.util import logging

__title__= 'sphinxnotes-isso'
__license__ = 'BSD'
__version__ = '1.0'
__author__ = 'Shengyu Zhang'
__url__ = 'https://sphinx-notes.github.io/isso'
__description__ = 'Sphinx extension for embeding Isso comments in documents'
__keywords__ = 'documentation, sphinx, extension, comment, isso, disqus'

# Isso client configuration items
# https://posativ.org/isso/docs/configuration/client/
CONFIG_ITEMS = ['isso_css', 'isso_lang', 'isso_reply_to_self',
             'isso_require_author', 'isso_require_email',
             'isso_max_comments_top', 'isso_max_comments_nested',
             'isso_reveal_on_click', 'isso_avatar', 'isso_avatar_bg',
             'isso_avatar_fg', 'isso_vote', 'isso_vote_levels',
             'isso_feed']

logger = logging.getLogger(__name__)

def ext_config_to_isso_config(key:str, value:Any) -> Tuple[str,str]:
    assert key in CONFIG_ITEMS
    key = 'data-' + key.replace('_', '-')
    if isinstance(value, str):
        pass
    elif isinstance(value, bool):
        value = str(value).lower()
    else:
        value = str(value)
    return (key, value)


class IssoNode(nodes.General, nodes.Element): pass

def html_visit_isso_node(self: HTML5Translator, node):
    docname = node['docname']
    metadata = self.builder.env.metadata[docname]

    # If docinfo :nocomments: is set, won’t display a comment form for a page
    # generated from this source file.
    #
    # See: https://www.sphinx-doc.org/en/master/usage/restructuredtext/field-lists.html
    if 'nocomments' in metadata:
        raise nodes.SkipNode

    thread_id = node.get('thread-id') or \
        metadata.get('isso-id') or \
        '/' + docname
    if not thread_id.startswith('/'):
        logger.warning(f'isso thread-id {thread_id} doesn\'t start with slash', location=node)

    kwargs = {
        'data-isso-id': thread_id,
    }
    if node.get('thread-title'):
        kwargs['data-title'] = node['thread-title']
    self.body.append(self.starttag(node, 'section', '', **kwargs))


def html_depart_isso_oode(self: HTML5Translator, _):
    self.body.append('</section>')


class IssoDirective(SphinxDirective):
    """Isso ".. isso::" rst directive."""

    option_spec = {
        'id': directives.unchanged,
        'title': directives.unchanged,
    }

    def run(self):
        """Executed by Sphinx.
        :returns: Single IssoNode instance with config values passed as arguments.
        :rtype: list
        """

        node = IssoNode()
        node['ids'] = ['isso-thread']
        # Save docname for later looking up :attr:`self.env.metadata`, 
        # which is not yet available now.
        node['docname'] = self.env.docname

        if self.options.get('id'):
            node['thread-id'] = self.options.get('id')

        if self.options.get('title'):
            node['thread-title'] = self.options.get('title')
        else:
            # TODO: support section title?
            title = self.state.document.next_node(nodes.title)
            if title:
                node['thread-title'] = title.astext()

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
    # Only embed comments for documents
    if not doctree:
        return
    # We supports embed mulitple comments box in same document
    for node in doctree.traverse(IssoNode):
        kwargs = {
            'data-isso': app.config.isso_url,
        }
        for cfg in CONFIG_ITEMS:
            val = getattr(app.config, cfg)
            if val is not None: # Maybe 0, False, '' or anything
                issocfg, issoval = ext_config_to_isso_config(cfg, val)
                kwargs[issocfg] = issoval
        js_path = posixpath.join(app.config.isso_url, 'js/embed.min.js')
        app.add_js_file(js_path, **kwargs)


def setup(app:Sphinx):
    app.add_config_value('isso_url', None, '')
    for cfg in CONFIG_ITEMS:
        app.add_config_value(cfg, None, '')
    app.add_directive('isso', IssoDirective)
    app.add_node(IssoNode, html=(html_visit_isso_node, html_depart_isso_oode))
    app.connect('html-page-context', on_html_page_context)

    return {'version': __version__}
