=====
Usage
=====

.. note:: Before using the extension, you should have an Isso__ instance deployed.

The ``isso`` directive is used to insert a Isso comment box.
The docname of current document is used as Isso thread ID.

The directive supports the following options:

:id: (text)
    Specify a thread ID rather than use docname
:title: (text)
    Specify a thread title rather than use document title

The comment box can be generated via the following source:

.. code-block:: rst

   .. isso::

__ https://isso-comments.de/
