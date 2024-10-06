import pytest
from um import count

def test_single_um():
    assert count("um") == 1
    assert count("Um, hello there.") == 1

def test_multiple_ums():
    assert count("um, um, um") == 3
    assert count("Um, I was just, um, thinking.") == 2

def test_no_um():
    assert count("hello, world") == 0
    assert count("yummy food") == 0

def test_case_insensitivity():
    assert count("UM, um, Um") == 3
    assert count("UM") == 1
