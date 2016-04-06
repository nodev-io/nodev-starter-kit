
import pytest

@pytest.mark.candidate('filter_strings')
def test_filter_strings_basic():
    input = ['has MARK', 'does not have']
    expected_ouput = ['has MARK']
    accept_pattern = '.*MARK.*'
    assert list(filter_strings(input, accept_pattern)) == expected_ouput
