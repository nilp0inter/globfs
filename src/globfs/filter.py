import fnmatch
import re


class Filter(object):
    """Glob based filter."""
    def __init__(self, expression, insensitive=False):
        """
        :arg expression: glob expression
        """
        if insensitive:
            self._re = re.compile(fnmatch.translate(expression), re.IGNORECASE)
        else:
            self._re = re.compile(fnmatch.translate(expression))

    def match(self, name):
        return self._re.match(name)


