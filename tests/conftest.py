from logging.config import dictConfig

import pytest

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

@pytest.yield_fixture
def logging_stream():
    stream = StringIO()

    def _logging_stream(log_format='%(levelname)s %(message)s',
                        formatter='multiline_formatter.formatter.MultilineMessagesFormatter'):
        dictConfig({
            'version': 1,
            'disable_existing_loggers': False,
            'formatters': {
                'default': {
                    '()': formatter,
                    'format': log_format,
                },
            },
            'handlers': {
                'streamhandler': {
                    'level': 'DEBUG',
                    'class': 'logging.StreamHandler',
                    'formatter': 'default',
                    'stream': stream,
                },
            },
            'loggers': {
                '': {
                    'handlers': ['streamhandler'],
                    'level': 'DEBUG',
                }
            }
        })
        return stream

    yield _logging_stream
    stream.close()
