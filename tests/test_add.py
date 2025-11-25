from calculator.operations import add

def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-2, -5) == -7

def test_add_mixed_sign_numbers():
    assert add(-2, 5) == 3

def test_add_floats():
    result = add(2.5, 0.1)
    assert abs(result - 2.6) < 0.0001
