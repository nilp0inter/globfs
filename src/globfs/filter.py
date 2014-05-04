import fnmatch
import re


class Filter(object):
    """Glob based filter."""
    def __init__(self, expression, insensitive=False):
        """
        :arg expression: Glob expression.
        :arg insensitive: Case insensitive expression or not.

        """
        if insensitive:
            self._re = re.compile(fnmatch.translate(expression),
                                  re.IGNORECASE)
        else:
            self._re = re.compile(fnmatch.translate(expression))

    def match(self, name):
        """Return `True` if expression match."""
        return self._re.match(name)
