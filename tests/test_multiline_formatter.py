import re
from logging import getLogger

logger = getLogger()

multiline_mark_pattern = r'''
\.{3}       # starts with three dots
\s          # and a space
\(          # opening bracket
    \d+     # the PID
    :       # separator
    [^\)]+  # thread name
\)          # closing bracket
'''
start_with_multiline_mark_re = re.compile(r'^' + multiline_mark_pattern + r'.+', re.VERBOSE)
end_with_multiline_mark_re = re.compile('.+' + '$', re.VERBOSE)


def assert_start_with_multiline_mark(line):
    assert start_with_multiline_mark_re.match(line)


def assert_end_with_multiline_mark(line):
    assert end_with_multiline_mark_re.match(line)


def test_not_multiline(logging_stream):
    stream = logging_stream('%(asctime)s %(message)s')
    logger.error('LOGMESSAGE')
    log_string = stream.getvalue().strip()
    assert re.match('', log_string), log_string
    assert log_string.endswith('LOGMESSAGE')


def test_two_lines(logging_stream):
    """
    Running logger.error('LINE1\nLINE2') will yield something like below:

    ERROR LINE1 ... (41964:MainThread)
    ... (41964:MainThread) : LINE2
    """

    stream = logging_stream()
    logger.error('LINE1\nLINE2')
    lines = stream.getvalue().strip().splitlines()

    assert lines[0].startswith('ERROR LINE1')
    assert_end_with_multiline_mark(lines[0])

    assert lines[1].endswith('LINE2')
    assert_start_with_multiline_mark(lines[1])


def test_exception(logging_stream):
    """
    Running logger.exception('LOGGING_MESSAGE') will yield something like the below:

    ERROR LOGGING_MESSAGE ... (43042:MainThread)
    ... (43042:MainThread) : Traceback (most recent call last):
    ... (43042:MainThread) :   File "/Users/plauri/work/opensource/python-multiline-log-formatter/tests/test_multiline_formatter.py", line 108, in test_exception
    ... (43042:MainThread) :     raise Exception('EXCEPTION_MESSAGE')
    ... (43042:MainThread) : Exception: EXCEPTION_MESSAGE
    """

    stream = logging_stream()
    try:
        raise Exception('EXCEPTION_MESSAGE')
    except Exception:
        logger.exception('LOGGING_MESSAGE')
    finally:
        lines = stream.getvalue().strip().splitlines()

        assert lines[0].startswith('ERROR LOGGING_MESSAGE')
        assert_end_with_multiline_mark(lines[0])

        for line in lines[1:]:
            assert_start_with_multiline_mark(line)

        assert 'Exception' in lines[-1]
