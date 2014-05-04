class GlobFS(object):
    """The Glob File System."""
    def __init__(self, root):
        self.root = root
        self.branches = []
