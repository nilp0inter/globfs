def test_filter_exists():
    try:
        from globfs.filter import Filter
    except:
        assert False, "Filter class doesn't exists."


def test_filter_basic(filter1, filter2):
    assert filter1.match('sasha.jpg')
    assert not filter1.match('sunny.png')

    assert filter2.match('523.apache.log')
    assert not filter2.match('x523.apache.log')


def test_filter_caseinsensitive(ifilter1, ifilter2):
    from globfs.filter import Filter

    assert ifilter1.match('sAsHa.jPg')
    assert not ifilter1.match('SUnnY.PnG')

    assert ifilter2.match('523.aPaCHe.Log')
    assert not ifilter2.match('x523.apaChE.LOg')
