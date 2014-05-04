import pytest


@pytest.fixture
def filter1():
    from globfs.filter import Filter
    return Filter('*.jpg')


@pytest.fixture
def filter2():
    from globfs.filter import Filter
    return Filter('???.*.log')


@pytest.fixture
def ifilter1():
    from globfs.filter import Filter
    return Filter('*.jpG', insensitive=True)


@pytest.fixture
def ifilter2():
    from globfs.filter import Filter
    return Filter('???.*.lOg', insensitive=True)


@pytest.fixture
def branch1():
    from globfs.branch import Branch
    return Branch(path='/tmp/path1', filters='*.log', ifilters='*.jpg,*.png')


@pytest.fixture
def branch2():
    from globfs.branch import Branch

    return Branch(path='/tmp/my_sasha_photos',
                  filters='*.png',
                  ifilters='*sasha*.???')


@pytest.fixture
def globfs1():
    from globfs import GlobFS
    return GlobFS(root='/tmp/test')
