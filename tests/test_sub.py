from calculator.operations import sub

def test_sub_positive_numbers():
    assert sub(10, 4) == 6

def test_sub_result_negative():
    assert sub(3, 10) == -7

def test_sub_with_zero():
    assert sub(5, 0) == 5

def test_sub_floats():
    result = sub(5.5, 2.2)
    assert abs(result - 3.3) < 0.0001
