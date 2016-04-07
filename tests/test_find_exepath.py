# -*- coding: utf-8 -*-

import pytest

@pytest.mark.candidate('find_exepath')
def test_find_exepath():
    assert find_exepath('echo') == '/bin/echo'
    assert find_exepath('mount') == '/sbin/mount'
    assert find_exepath('grep') == '/usr/bin/grep'
