
def test_which(candidate):
    # rename `candidate` to a more readable name
    which = candidate

    assert which('sh') == '/bin/sh'
    assert which('env') == '/usr/bin/env'
