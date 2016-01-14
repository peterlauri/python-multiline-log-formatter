=====
Usage
=====

To use Python Multiline Log Formatter in a project::

	import multiline_formatter

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
