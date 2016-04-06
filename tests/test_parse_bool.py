
import pytest

@pytest.mark.candidate('parse_bool')
def test_parse_bool():

    assert not parse_bool('false')
    assert not parse_bool('FALSE')
    assert not parse_bool('0')

    assert parse_bool('true')
    assert parse_bool('TRUE')
    assert parse_bool('1')
