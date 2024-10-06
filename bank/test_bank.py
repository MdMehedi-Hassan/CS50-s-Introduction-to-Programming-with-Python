import pytest
from bank import value

def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0

def test_h_only():
    assert value("hi") == 20
    assert value("hey") == 20

def test_other_greetings():
    assert value("greetings") == 100
    assert value("welcome") == 100
