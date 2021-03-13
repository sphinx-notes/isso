================
sphinxnotes-isso
================

--------------------------------------------------------
Sphinx extension for embeding Isso comments in documents
--------------------------------------------------------

.. image:: https://img.shields.io/github/stars/sphinx-notes/isso.svg?style=social&label=Star&maxAge=2592000
   :target: https://github.com/sphinx-notes/isso

:version: |version|
:copyright: Copyright ©2021 by Shengyu Zhang.
:license: BSD, see LICENSE for details.

.. contents::
   :local:
   :backlinks: none

Installation
============

Download it from official Python Package Index:

.. code-block:: console

   $ pip install sphinxnotes-isso

Add extension to :file:`conf.py` in your sphinx project:

.. code-block:: python

    extensions = [
              # …
              'sphinxnotes.isso',
              # …
              ]

Configuration
=============

:isso_url: HTTP URL points to your Isso server

The following configuration items are corresponding to `Isso Client Configuration`_ ,
please use Python's boolean, numeric value instead of string formatted value.

- isso_css
- isso_lang
- isso_reply_to_self
- isso_require_author
- isso_require_email
- isso_max_comments_top
- isso_max_comments_nested
- isso_reveal_on_click
- isso_avatar
- isso_avatar_bg
- isso_avatar_fg
- isso_vote
- isso_vote_levels
- isso_feed

.. _Isso Client Configuration: https://posativ.org/isso/docs/configuration/client/

Functionalities
===============

The ``isso`` directive is used to insert a isso comment box.
The docname of current document is used as Isso thread ID.

The directive supports the following options:

:id: (text)
    Specify a thread ID rather than use docname

The comment box at the bottom is generated via the following source:

.. code-block:: rst

   .. isso::

Change Log
==========

2021-03-13 1.0a1
----------------

.. sectionauthor:: Shengyu Zhang

The first version is out, enjoy~

--------------------------------------------------------------------------------

.. isso::
