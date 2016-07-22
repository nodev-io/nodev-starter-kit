
import io
import pytest
from nodev.specs.generic import FlatContainer

@pytest.mark.parametrize('text2stream', [
    lambda x: x,
    lambda x: x.splitlines(True),
    lambda x: enumerate(x.splitlines(True), 1),
    lambda x: io.StringIO(x),
])
def test_skip_comments(candidate, text2stream):
    skip_comments = candidate

    text = 'value = 1 # comment\n'
    assert 'value = 1' in FlatContainer(skip_comments(text2stream(text)))
    assert 'comment' not in FlatContainer(skip_comments(text2stream(text)))
