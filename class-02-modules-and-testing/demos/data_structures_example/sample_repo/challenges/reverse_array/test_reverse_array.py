from .reverse_array import array_reverse
import pytest


def test_assert_true():
    """test function which asserts that the True object is the actual True object
    """
    assert True is True


def test_module_exists():
    from .reverse_array import array_reverse
    assert array_reverse


def test_list_import():
    from sample_repo.data_structures.list.list import fancy_list
    assert 2 in fancy_list
    assert 6 in fancy_list


    # from sample_repo.data_structures.list import list
    # assert 2 in list.fancy_list
    # assert 6 in list.fancy_list


def test_package_import():
    import pytest
    assert pytest


def test_reverse_list():
    actual = [1, 2, 3, 4]
    expected = [4, 3, 2, 1]
    assert array_reverse(actual) == expected


def test_another_reverse_list():
    actual = [1, 2, 3, 4, 5]
    expected = [5, 4, 3, 2, 1]
    assert array_reverse(actual) == expected


def test_list_of_same_values():
    actual = [1, 1, 1, 1, 1]
    expected = [1, 1, 1, 1, 1]
    assert array_reverse(actual) == expected


def test_empty_list():
    actual = []
    expected = []
    assert array_reverse(actual) == expected


def test_array_reverse_validates_lists():
    actual = {}
    with pytest.raises(TypeError):
        array_reverse(actual)
