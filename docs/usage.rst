=====
Usage
=====

The ``isso`` directive is used to insert a Isso comment box.
Each comment thread is distinguished by Isso Thread ID (``data-isso-id``),
which can be specified via the ``id`` option (see below) or via ``:isso-id``
docinfo. If no thread ID given, ``/{docname}`` will be used.

The directive supports the following options:

:id: (text)
    Specify a thread ID, optional
:title: (text)
    Specify a thread title rather than use document title

Enable comments for all documents
=================================

Use Sphinx's ``rst_epilog`` confval to append the ``isso`` directive at the
end of every source file. For example:

.. code:: python

   rst_epilog = """
   .. isso::
   """

Disable comments for specified document
---------------------------------------

This extension respects the ``:nocomments`` docinfo__:

   If set, the web application won’t display a comment form for a page generated
   from this source file.

__ https://www.sphinx-doc.org/en/master/usage/restructuredtext/field-lists.html#file-wide-metadata
