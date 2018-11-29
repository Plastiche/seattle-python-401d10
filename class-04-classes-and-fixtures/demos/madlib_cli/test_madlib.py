import madlib
import pytest

def test_welcome(capsys):

    madlib.welcome()

    captured = capsys.readouterr()

    assert captured.out == 'Welcome to the Jungle\n'

def test_read_file():

    contents = madlib.read_file('./madlib_raw.txt')

    assert contents.startswith('Make Me A Video Game!')

def test_write_file():

    contents = 'f'

    path = './foo.txt'

    madlib.write_file(path, contents)

    with open(path) as f:
        assert f.read() == contents

def test_parse():

    prompts, stripped = madlib.parse('It was a {Adjective} and {Adjective} {Noun}')

    assert prompts == ['Adjective','Adjective','Noun']

    assert stripped == 'It was a {} and {} {}'

def test_tell_story():

    # input_values = iter(['dark','stormy','night'])
    input_values = ['dark','stormy','night']
    input_values.reverse()

    # function in another function??? Sure, why not?
    # there is another way using lambdas though
    def mock_input(s):
        # return next(input_values)
        return input_values.pop()

    madlib.input = mock_input # step in front of default input method

    raw = 'It was a {Adjective} and {Adjective} {Noun}'

    story = madlib.tell_story(raw)

    assert story == 'It was a dark and stormy night'

def test_unpack():
    pass
