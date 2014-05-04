import pytest


def test_globfs_exists():
    try:
        from globfs import GlobFS
    except:
        assert False, "GlobFS class doesn't exists."


def test_globfs_config(globfs1):
    from globfs import GlobFS
    g1 = GlobFS(root='/tmp/test')

    assert g1.root == '/tmp/test'
    assert isinstance(g1.branches, list)


def test_globfs_add_branch(globfs1, branch1):
    globfs1.add_branch(branch1)
    assert branch1 in globfs1.branches


def test_globfs_selectbranch(globfs1, branch1, branch2):
    from globfs.errors import NoBranchError

    # The order is important
    globfs1.add_branch(branch2)
    globfs1.add_branch(branch1)

    assert globfs1.get_branch('something.jpg') == branch1
    assert globfs1.get_branch('something.png') == branch2

    with pytest.raises(NoBranchError):
        globfs1.get_branch('other.txt')
