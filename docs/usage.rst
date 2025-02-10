=====
Usage
=====

.. note::

   Isso only supports rendering **one comment thread on the same page**.
   If you insert multiple comment threads on the same page, the extra threads
   will display error messages.

There are two ways to insert comment thread:

Manual insert (at a specific location)
--------------------------------------

.. rst:directive:: .. isso:: [id]

   Insert a Isso comment thread at a specific location.

   Threads are distinguished by unique Isso Thread ID (``data-isso-id``),
   If no thread ID given, ``/{docname}`` (a slash-prefixed document name)
   will be used.

   .. rst:directive:option:: title: title
      :type: text

      Indicate thread title rather than use original document title.

Batch insert (at the end of the document)
-----------------------------------------

If document's docname is matched by :confval:`isso_include_patterns` and
not matched by :confval:`isso_exclude_patterns`, a comment thread will be
automaticlly inserted at the end.

For example:

.. code-block:: python
   :caption: Enable commenting for all documents

   isso_include_patterns = ['**']
   isso_exclude_patterns = []

.. code-block:: python
   :caption: Enable commenting for only blog posts

   isso_include_patterns = ['blog/**']

.. code-block:: python
   :caption: Enable commenting for all documents (except blog posts)

   isso_include_patterns = ['**']
   isso_exclude_patterns = ['blog/**']

DocInfos
~~~~~~~~

Users can configure the batched inserted comment thread by setting docinfo_:

:``:isso-id``:
   Indicate the Isso thread ID, similar to :rst:dir:`isso` directive's argument.

:``:nocomments``:
   This extension respects the standard ``:nocomments`` docinfo:

      If set, the web application won’t display a comment form for a page generated
      from this source file.

.. _docinfo: https://www.sphinx-doc.org/en/master/usage/restructuredtext/field-lists.html#file-wide-metadata
