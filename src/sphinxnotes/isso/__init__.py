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
from importlib.metadata import version

from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.docutils import SphinxDirective
from sphinx.writers.html5 import HTML5Translator
from sphinx.transforms import SphinxTransform
from sphinx.util.matching import patmatch


if TYPE_CHECKING:
    from sphinx.application import Sphinx
    from sphinx.environment import BuildEnvironment
from sphinx.util import logging


logger = logging.getLogger(__name__)


class IssoNode(nodes.General, nodes.Element):
    def setup(
        self,
        env: BuildEnvironment,
        docname: str,
        id_: str | None = None,
        title: str | None = None,
        rawsource: str = '',
    ):
        self['thread-id'] = id_ or env.metadata[docname].get('isso-id') or '/' + docname
        self['thread-title'] = title or env.titles.get(docname, nodes.title()).astext()
        self['rawsource'] = rawsource


def html_visit_isso_node(self: HTML5Translator, node):
    if not node['thread-id'].startswith('/'):
        logger.warning(
            f"isso thread-id {node['thread-id']} doesn't start with slash",
            location=node,
        )

    kwargs = {
        'data-isso-id': node['thread-id'],
        'data-title': node['thread-title'],
    }
    self.body.append(self.starttag(node, 'section', '', **kwargs))


def html_depart_isso_oode(self: HTML5Translator, _):
    self.body.append('</section>')


class IssoDirective(SphinxDirective):
    optional_arguments = 1  # Isso thread ID
    option_spec = {
        'title': directives.unchanged,  # Isso thread title
    }

    def run(self):
        node = IssoNode()
        node.setup(
            self.env,
            self.env.docname,
            id_=self.arguments[0] if self.arguments else None,
            title=self.options.get('title'),
            rawsource=self.block_text,
        )
        self.set_source_info(node)
        return [node]


def on_html_page_context(
    app: Sphinx, pagename: str, templatename: str, context, doctree: nodes.document
) -> None:
    """Called when the HTML builder has created a context dictionary to render a template with.

    Conditionally adding isso client script to <head /> if the directive is used in a page.

    :param sphinx.application.Sphinx app: Sphinx application object.
    :param str pagename: Name of the page being rendered (without .html or any file extension).
    :param str templatename: Page name with .html.
    :param dict context: Jinja2 HTML context.
    :param docutils.nodes.document doctree: Tree of docutils nodes.
    """
    if not doctree:
        return
    if doctree.next_node(IssoNode) is None:
        # No comment thread, skip.
        return

    kwargs = {
        'data-isso': app.config.isso_url,
        **app.config.isso_client_config,
    }
    js_path = posixpath.join(app.config.isso_url, 'js/embed.min.js')
    app.add_js_file(js_path, **kwargs)


class IssoTransform(SphinxTransform):
    """Append isso comment thread to document."""

    default_priority = 200

    def apply(self, **kwargs) -> None:
        docname = self.env.path2doc(self.document['source'])
        # Generated page has no docname, skip it.
        if docname is None:
            return

        # If docinfo :nocomments: is set, won’t display comment thread.
        # See: https://www.sphinx-doc.org/en/master/usage/restructuredtext/field-lists.html
        # TODO: support no-comments?
        metadata = self.env.metadata[docname]
        if 'nocomments' in metadata:
            return

        # Filter docname by patterns.
        exclude = [patmatch(docname, p) for p in self.config.isso_exclude_patterns]
        include = not exclude and [
            patmatch(docname, p) for p in self.config.isso_include_patterns
        ]
        if include:
            node = IssoNode()
            node.setup(self.env, docname)
            self.document += node

        all_isso_nodes = list(self.document.traverse(IssoNode))
        if len(all_isso_nodes) == 0:
            return
        if len(all_isso_nodes) > 1:
            logger.warning(f'{len(all_isso_nodes)} isso nodes found, only 1 is allowed')

        # Replace extra isso nodes (except last one) with system_message.
        for n in all_isso_nodes[:-1]:
            msg = 'Only one Isso thread is allowed in one document'
            rawsrc = nodes.literal_block(n['rawsource'], n['rawsource'])
            sm = nodes.system_message(
                msg,
                rawsrc,
                type='WARNING',
                level=2,
                backrefs=[],
                source=n.source,
                line=n.line,
            )
            n.replace_self(sm)

        # To identify comment thread.
        all_isso_nodes[-1]['ids'] = ['isso-thread']


def setup(app: Sphinx):
    app.add_config_value('isso_url', None, '')
    app.add_config_value('isso_client_config', {}, '')
    app.add_config_value('isso_include_patterns', [], '')
    app.add_config_value('isso_exclude_patterns', [], '')

    app.add_directive('isso', IssoDirective)
    app.add_node(IssoNode, html=(html_visit_isso_node, html_depart_isso_oode))
    app.add_transform(IssoTransform)

    app.connect('html-page-context', on_html_page_context)

    return {
        'version': version('sphinxnotes.isso'),
        'parallel_read_safe': True,
        "parallel_write_safe": True,
    }
