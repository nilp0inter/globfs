from __future__ import absolute_import
from .errors import NoBranchError

class GlobFS(object):
    """The Glob File System."""
    def __init__(self, root):
        self.root = root
        self.branches = []

    def add_branch(self, branch):
        self.branches.append(branch)

    def get_branch(self, name):
        for branch in self.branches:
            if branch.match(name):
                return branch
        raise NoBranchError('No branch found for "{}"'.format(name))
