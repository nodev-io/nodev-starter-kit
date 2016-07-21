
def test_parse_bool(candidate):
    parse_bool = candidate

    assert not parse_bool('false')
    assert not parse_bool('FALSE')
    assert not parse_bool('0')

    assert parse_bool('true')
    assert parse_bool('TRUE')
    assert parse_bool('1')
