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


def test_branch_match():
    from globfs.branch import Branch

    b1 = Branch(path='/tmp/my_sasha_photos',
                filters='*.png',
                ifilters='*sasha*.???')

    assert b1.match('sasha.jpg')
    assert b1.match('sasha21.jpg')
    assert b1.match('sunny.png')
    assert not b1.match('rocco.gif')
    assert not b1.match('otherguy.PNG')
