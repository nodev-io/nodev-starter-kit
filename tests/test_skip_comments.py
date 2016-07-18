
# import pytest

from nodev.specs.generic import FlatContainer

#
# possible evolution of a ``skip_comments`` function
#
def skip_comments_v0(stream):
    return [line.partition('#')[0] for line in stream]


def skip_comments_v1(stream):
    for line in stream:
        yield line.partition('#')[0]


def skip_comments_v2(stream):
    for index, line in enumerate(stream):
        value = line.partition('#')[0]
        if value:
            yield index, value


def skip_comments_v3(stream):
    for index, line in enumerate(stream):
        value, sep, comment = line.partition('#')
        if value:
            yield index, value, sep + comment


skip_comments = skip_comments_v0


def test_skip_comments_will_break_soon():
    assert skip_comments(['# comment']) == ['']
    assert skip_comments(['value # comment']) == ['value ']
    assert skip_comments(['value 1', '', 'value 2']) == ['value 1', '', 'value 2']


def test_skip_comments_will_break_eventually():
    assert 'value ' in skip_comments(['value # comment'])
    assert 'value 1' in skip_comments(['value 1', '', 'value 2'])
    assert 'value 2' in skip_comments(['value 1', '', 'value 2'])


# @pytest.mark.candidate('skip_comments')
def test_skip_comments_will_not_break():
    assert 'value ' in FlatContainer(skip_comments(['value # comment']))
    assert 'value 1' in FlatContainer(skip_comments(['value 1', '', 'value 2']))
    assert 'value 2' in FlatContainer(skip_comments(['value 1', '', 'value 2']))
