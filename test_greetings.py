import pytest

from greetings import greet, shout


def test_greet_returns_spanish_greeting():
    assert greet("Juan") == "Hola, Juan!"


def test_greet_raises_on_empty_name():
    with pytest.raises(ValueError):
        greet("")


def test_shout_uppercases_and_adds_exclamation():
    assert shout("hola") == "HOLA!"
