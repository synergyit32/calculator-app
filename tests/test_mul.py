from calculator.operations import mul

def test_mul_positive_numbers():
    assert mul(4, 2) == 8

def test_mul_by_zero():
    assert mul(99, 0) == 0
    assert mul(0, 99) == 0

def test_mul_negative_numbers():
    assert mul(-3, -6) == 18

def test_mul_mixed_sign():
    assert mul(-3, 6) == -18
