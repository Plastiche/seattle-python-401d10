from .file_io import read_file, read_file_lines, write_file, read_file_binary
# , read_file_lines, read_file_binary, write_file
import struct
import pytest

def test_read_file_exists():
    assert read_file

def test_read_file_returns_contents():
    actual = read_file('./file_io/one_line.txt')
    expected = 'just one line\n'
    assert actual == expected


def test_read_multi_lines():
    expected = 3
    lines = read_file_lines('./file_io/three_line.txt')
    actual = len(lines)
    assert actual == expected
    assert isinstance(lines, list)
    assert type(lines) == list


def test_fail_with_bad_path():
    with pytest.raises(FileNotFoundError):
        read_file('./road/to/nowhere')

def test_read_forbidden():
    with pytest.raises(Exception) as exc:
        read_file('./forbidden')

    assert str(exc.value) == 'Forbidden'


def test_write_file():
    path = './file_io/foo.txt'
    contents = 'foo bar baz'
    write_file(path, contents)
    actual = read_file(path)
    expected = contents
    assert actual == expected

def test_read_binary():

    contents = read_file_binary('./file_io/baldy.bmp')
    image_type = contents[:2].decode()
    assert image_type == 'BM'
    image_size = struct.unpack('I', contents[2:6])
    assert image_size == (15146,)
    mv = memoryview(contents)
    assert mv.shape == (15146,)

# def test_append():
#     path = './file_io/foo.txt'
#     contents = 'and so it begins'
#     append(path, contents)
#     # What now?
