.. This file is generated from sphinx-notes/cookiecutter.
   You need to consider modifying the TEMPLATE or modifying THIS FILE.

================
sphinxnotes-isso
================

.. |docs| image:: https://img.shields.io/github/deployments/sphinx-notes/isso/github-pages
   :target: https://sphinx.silverrainz.me/isso
   :alt: Documentation Status

.. |license| image:: https://img.shields.io/github/license/sphinx-notes/isso
   :target: https://github.com/sphinx-notes/isso/blob/master/LICENSE
   :alt: Open Source License

.. |pypi| image:: https://img.shields.io/pypi/v/sphinxnotes-isso.svg
   :target: https://pypi.python.org/pypi/sphinxnotes-isso
   :alt: PyPI Package

.. |download| image:: https://img.shields.io/pypi/dm/sphinxnotes-isso
   :target: https://pypi.python.org/pypi/sphinxnotes-isso
   :alt: PyPI Package Downloads

|docs| |license| |pypi| |download|

Introduction
============

.. INTRODUCTION START

The extension allows your embedding Isso_ comments in your Sphinx documentation:

.. _Isso: https://isso-comments.de/

.. INTRODUCTION END

Getting Started
===============

.. note::

   We assume you already have a Sphinx documentation,
   if not, see `Getting Started with Sphinx`_.

First, downloading extension from PyPI:

.. code-block:: console

   $ pip install sphinxnotes-isso

Then, add the extension name to ``extensions`` configuration item in your
:parsed_literal:`conf.py_`:

.. code-block:: python

   extensions = [
             # …
             'sphinxnotes.isso',
             # …
             ]

.. _Getting Started with Sphinx: https://www.sphinx-doc.org/en/master/usage/quickstart.html
.. _conf.py: https://www.sphinx-doc.org/en/master/usage/configuration.html

.. ADDITIONAL CONTENT START

Set :confval:`isso_url` to the URL of your Isso server.

.. code-block:: python

   isso_url = 'https://HOST:PORT'

And then you can use directive ``isso`` to insert a Isso comment box, see
:doc:`usage` for more details.

.. example::

   .. isso::

Feel free to comment~

.. ADDITIONAL CONTENT END

Contents
========

.. toctree::
   :caption: Contents

   usage
   conf
   changelog

The Sphinx Notes Project
========================

The project is developed by `Shengyu Zhang`__,
as part of **The Sphinx Notes Project**.

.. toctree::
   :caption: The Sphinx Notes Project

   Home <https://sphinx.silverrainz.me/>
   Blog <https://silverrainz.me/blog/category/sphinx.html>
   PyPI <https://pypi.org/search/?q=sphinxnotes>

__ https://github.com/SilverRainZ
