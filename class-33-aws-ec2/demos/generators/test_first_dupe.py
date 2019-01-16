from .tale_of_two_cities import find_first_dupe

def test_find_first_dupe():
    txt = 'it was the best of times, it was the worst of times'
    dupe = find_first_dupe(txt)
    assert dupe == 'it'
