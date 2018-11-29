from .reverse_list import reverse


def test_function_exists():
    assert reverse


def test_returns_list():
    actual = reverse([1, 2, 3])
    assert isinstance(actual, list)


def test_returns_reversed():
    actual = reverse([1, 2, 3])
    assert actual == [3, 2, 1]


def test_original_unmodified():
    original = [1, 2, 3]
    reverse(original)
    assert (original == [1, 2, 3])


def test_handles_empty_list():
    actual = reverse([])
    expected = []
    assert (actual == expected)
