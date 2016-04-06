# -*- coding: utf-8 -*-

import pytest

@pytest.mark.candidate('factorial')
def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(21) == 51090942171709440000
