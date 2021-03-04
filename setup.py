# -*- coding: utf-8 -*-

import sys
import os
sys.path.insert(0, os.path.abspath('./sphinxnotes'))
from setuptools import setup, find_namespace_packages
import isso as proj

with open('README.rst') as f:
    long_desc = f.read()

setup(
    name=proj.__title__,
    version=proj.__version__,
    url=proj.__url__,
    license=proj.__license__,
    author=proj.__author__,
    description=proj.__description__,
    long_description=long_desc,
    long_description_content_type = 'text/x-rst',
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Environment :: Plugins',
        'Framework :: Sphinx',
        'Framework :: Sphinx :: Extension',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Documentation',
        'Topic :: Documentation :: Sphinx',
        'Topic :: Text Processing :: Markup :: reStructuredText',
    ],
    keywords=proj.__keywords__,
    platforms='any',
    python_requires='>=3',
    packages=find_namespace_packages(include=['sphinxnotes.*'],
                                     exclude=['sphinxnotes.snippet.tests']),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'snippet=sphinxnotes.snippet.cli:main',
        ],
    },
    install_requires= [
        'Sphinx',
    ],
    namespace_packages=['sphinxnotes'],
)
