========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis|
        | |codecov|
        |
    * - package
      - |version| |downloads| |wheel| |supported-versions| |supported-implementations|

.. |docs| image:: https://readthedocs.org/projects/python-multiline-log-formatter/badge/?style=flat
    :target: https://readthedocs.org/projects/python-multiline-log-formatter
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/peterlauri/python-multiline-log-formatter.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/peterlauri/python-multiline-log-formatter

.. |codecov| image:: https://codecov.io/github/peterlauri/python-multiline-log-formatter/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/peterlauri/python-multiline-log-formatter

.. |version| image:: https://img.shields.io/pypi/v/multiline-log-formatter.svg?style=flat
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/multiline-log-formatter

.. |downloads| image:: https://img.shields.io/pypi/dm/multiline-log-formatter.svg?style=flat
    :alt: PyPI Package monthly downloads
    :target: https://pypi.python.org/pypi/multiline-log-formatter

.. |wheel| image:: https://img.shields.io/pypi/wheel/multiline-log-formatter.svg?style=flat
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/multiline-log-formatter

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/multiline-log-formatter.svg?style=flat
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/multiline-log-formatter

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/multiline-log-formatter.svg?style=flat
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/multiline-log-formatter


.. end-badges

Python logging formatter that prefix multiline log message and trackebacks. Makes the logs more readable, both for
tracebacks and for multiline log messages.

* Free software: BSD license

Benchmarking
============

Benchmark against pythons built in formatter **logging.Formatter**. The benchmark is done using **pytest-benchmark**,
and the below results is from a run on a faily new MacBook Pro, using Python 2.7.

One should note that we are using StringIO as stream output, so we should expect the results to be even closer with
more production alike setup, for example writing to disc.

.. image:: https://raw.github.com/peterlauri/python-multiline-log-formatter/master/docs/benchmark.png
    :alt: python-redis-lock flow diagram

Installation
============

.. code-block:: bash

    pip install multiline-log-formatter

Usage
=====

Add this to dictConfig:

.. code-block:: python

    'formatters': {
        'default': {
            '()': 'multiline_formatter.formatter.MultilineMessagesFormatter',
            'format': '[%(levelname)s] %(message)s'
        },
    },

And log messages will look like this:

.. code-block:: bash

    [ERROR] LOGGING_MESSAGE ... (49564:MainThread)
    ... (49564:MainThread) : Traceback (most recent call last):
    ... (49564:MainThread) :   File "/Users/plauri/work/opensource/python-multiline-log-formatter/tests/test_multiline_formatter.py", line 112, in test_exception
    ... (49564:MainThread) :     raise Exception('EXCEPTION_MESSAGE')
    ... (49564:MainThread) : Exception: EXCEPTION_MESSAGE

And if you don't like the default, you can customize it by extending **MultilineMessagesFormatter** and set
**multiline_marker**. You can also change **multiline_fmt**, but assure you include **%(message)s** in the formating
string.

Documentation
=============

https://python-multiline-log-formatter.readthedocs.org/

Development
===========

To run the all tests run::

    tox


Other
=====

This project sceleton is generated by ionelmc's pylibrary_ cookiecutter.

.. _pylibrary: https://github.com/ionelmc/cookiecutter-pylibrary

