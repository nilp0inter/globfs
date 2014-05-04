def test_filter_exists():
    try:
        from globfs.filter import Filter
    except:
        assert False, "Filter class doesn't exists."

def test_filter_basic():
    from globfs.filter import Filter
    filter1 = Filter('*.jpg')

    assert filter1.match('sasha.jpg')
    assert not filter1.match('sunny.png')

    filter2 = Filter('???.*.log')
    assert filter2.match('523.apache.log')
    assert not filter2.match('x523.apache.log')

def test_filter_caseinsensitive():
    from globfs.filter import Filter
    filter1 = Filter('*.jpG', insensitive=True)

    assert filter1.match('sAsHa.jPg')
    assert not filter1.match('SUnnY.PnG')

    filter2 = Filter('???.*.lOg', insensitive=True)
    assert filter2.match('523.aPaCHe.Log')
    assert not filter2.match('x523.apaChE.LOg')
