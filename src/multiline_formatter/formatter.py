import logging
import sys


class MultilineMessagesFormatter(logging.Formatter):

    multiline_marker = '... (%(process)d:%(threadName)s)'
    multiline_fmt = multiline_marker + ' : %(message)s'

    def format(self, record):
        """
        This is mostly the same as logging.Formatter.format except for the splitlines() thing.

        This is done so (copied the code) to not make logging a bottleneck. It's not lots of code
        after all, and it's pretty straightforward.
        """
        record.message = record.getMessage()
        if self.usesTime():
            record.asctime = self.formatTime(record, self.datefmt)
        if '\n' in record.message:
            splitted = record.message.splitlines()
            output = self._fmt % dict(record.__dict__, message=splitted.pop(0))
            output += ' ' + self.multiline_marker % record.__dict__ + '\n'
            output += '\n'.join(
                self.multiline_fmt % dict(record.__dict__, message=line)
                for line in splitted
            )
        else:
            output = self._fmt % record.__dict__

        if record.exc_info:
            # Cache the traceback text to avoid converting it multiple times
            # (it's constant anyway)
            if not record.exc_text:
                record.exc_text = self.formatException(record.exc_info)
        if record.exc_text:
            output += ' ' + self.multiline_marker % record.__dict__ + '\n'
            try:
                output += '\n'.join(
                    self.multiline_fmt % dict(record.__dict__, message=line)
                    for index, line in enumerate(record.exc_text.splitlines())
                )
            except UnicodeError:
                output += '\n'.join(
                    self.multiline_fmt % dict(record.__dict__, message=line)
                    for index, line
                    in enumerate(record.exc_text.decode(sys.getfilesystemencoding(), 'replace').splitlines())
                )
        return output
