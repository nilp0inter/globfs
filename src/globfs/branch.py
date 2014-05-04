from __future__ import absolute_import
from .filter import Filter

class Branch(object):
    """A filesystem path. We'll write here depending on filters."""
    def __init__(self, path, filters=tuple(), ifilters=tuple()):
        self.path = path
        self.filters = ([ Filter(exp) for exp in filters.split(',') ] +
                        [ Filter(exp, insensitive=True)
                          for exp in ifilters.split(',') ] )

    def match(self, name):
        """Return `True` if any filter match name."""
        return any(f.match(name) for f in self.filters)
