def test_branch_exists():
    try:
        from globfs.branch import Branch
    except:
        assert False, "Branch class doesn't exists."
