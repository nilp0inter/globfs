def test_branch_exists():
    try:
        from globfs.branch import Branch
    except:
        assert False, "Branch class doesn't exists."


def test_branch_config(branch1):
    from globfs.filter import Filter
    assert branch1.path == '/tmp/path1'
    assert all(map(lambda x: isinstance(x, Filter), branch1.filters))


def test_branch_match(branch2):
    assert branch2.match('sasha.jpg')
    assert branch2.match('sasha21.jpg')
    assert branch2.match('sunny.png')
    assert not branch2.match('rocco.gif')
    assert not branch2.match('otherguy.PNG')
