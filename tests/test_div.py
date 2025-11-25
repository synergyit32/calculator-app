import pytest
from calculator.operations import div

def test_div_normal_division():
    assert div(8, 2) == 4

def test_div_float_result():
    assert div(3, 2) == 1.5

def test_div_negative_numbers():
    assert div(-9, 3) == -3

def test_div_zero_numerator():
    assert div(0, 5) == 0

def test_div_by_zero_raises():
    with pytest.raises(ZeroDivisionError):
        div(5, 0)
