def test_branch_exists():
    try:
        from globfs.branch import Branch
    except:
        assert False, "Branch class doesn't exists."

def test_branch_config():
    from globfs.branch import Branch
    from globfs.filter import Filter

    b1 = Branch(path='/tmp/path1', filters='*.log', ifilters='*.jpg,*.png')
    assert b1.path == '/tmp/path1'
    assert all(map(lambda x: isinstance(x, Filter), b1.filters))
