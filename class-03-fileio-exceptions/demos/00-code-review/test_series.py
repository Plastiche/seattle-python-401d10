from series import fibonacci
from series import lucas

def test_single_number_fib():
    """test fib function which tests by bringing in a single number
    """
    actual = 4
    expected = 3
    assert fibonacci(actual) == expected


def test_zero_number_fib():
    """test fib function which tests by bringing in a zero number
    """
    actual = 0
    expected = 0
    assert fibonacci(actual) == expected


def test_double_number_fib():
    """test fib function which tests by bringing in a double digit number
    """
    actual = 10
    expected = 55
    assert fibonacci(actual) == expected


def test_single_number_lucas():
    """test lucas function which tests by bringing in a single number
    """
    actual = 4
    expected = 5
    assert lucas(actual) == expected


def test_zero_number_lucas():
    """test lucas function which tests by bringing in a zero number
    """
    actual = 0
    expected = 1
    assert lucas(actual) == expected
