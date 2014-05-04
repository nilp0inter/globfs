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
