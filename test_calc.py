import pytest

from simpleapp import *



def test_sum():
    assert sum(2, 3) == 5
    assert sum(-1, 1) == 0
    assert sum(0, 0) == 0

def test_subtract():
    assert subtract(2, 3) == -1
    assert subtract(-1, 1) == -2
    assert subtract(0, 0) == 0

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 1) == -1
    assert multiply(0, 0) == 0

def test_div():
    assert div(6, 3) == 2
    assert div(-6, 3) == -2
    assert div(0, 1) == 0

    with pytest.raises(ZeroDivisionError):
        div(1, 0)