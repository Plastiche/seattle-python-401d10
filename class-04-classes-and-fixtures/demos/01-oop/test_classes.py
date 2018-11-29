from classes import Person, Employee
import pytest


@pytest.fixture(scope='function')  # Scope - Function, Module, Class, Session
def suzy_person():
    suzy = Person('Suzy', 14)
    suzy.set_eye_color('blue')
    return suzy


def test_person_has_name(suzy_person):
    """
    """
    assert suzy_person.name == 'Suzy'


def test_person_has_age(suzy_person):
    """
    """
    assert suzy_person.age == 14


def test_setting_eye_color(suzy_person):
    """
    """
    suzy_person.set_eye_color('green')
    assert suzy_person.eye_color == 'green'


def test_eye_color_is_blue(suzy_person):
    """
    """
    assert suzy_person.eye_color == 'blue'
