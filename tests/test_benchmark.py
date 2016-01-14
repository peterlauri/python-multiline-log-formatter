import logging

import pytest

logger = logging.getLogger()

formatter_mapping = {
    'builtin': 'logging.Formatter',
    'this': 'multiline_formatter.formatter.MultilineMessagesFormatter',
}


@pytest.mark.parametrize('formatter', [('builtin'), ('this')])
def test_singleline(benchmark, logging_stream, formatter):
    logging_stream(formatter=formatter_mapping[formatter])
    benchmark(logger.info, 'Logging message')


@pytest.mark.parametrize('formatter', [('builtin'), ('this')])
def test_multiline(benchmark, logging_stream, formatter):
    logging_stream(formatter=formatter_mapping[formatter])
    benchmark(logger.info, 'Logging message line 1\nLogging message line 2')


@pytest.mark.parametrize('formatter', [('builtin'), ('this')])
def test_exception(benchmark, logging_stream, formatter):
    logging_stream(formatter=formatter_mapping[formatter])

    try:
        raise Exception('EXCEPTION_MESSAGE')
    except Exception:
        benchmark(logger.exception, 'Logging message line')
