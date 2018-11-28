from .words import get_words, get_non_exists, say_hi, get_exception
import pytest


def test_get_words():
    get_words()
    with open('./assets/words.txt', 'r') as fd:
        for line in fd:
            assert len(line) > 3


def test_say_hi(capsys):
    say_hi()
    captured = capsys.readouterr()
    assert (captured.out == 'hola\n')


def test_get_non_exists():
    with pytest.raises(FileNotFoundError):
        get_exception()
