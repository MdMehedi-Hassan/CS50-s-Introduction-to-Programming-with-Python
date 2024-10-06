import pytest
from plates import is_valid

def test_length():
    # Test plates that are too short or too long
    assert is_valid("AA") == True
    assert is_valid("A") == False
    assert is_valid("TOOLONG") == False

def test_start_with_letters():
    # Test that plates start with at least two letters
    assert is_valid("AB123") == True
    assert is_valid("1A1234") == False
    assert is_valid("A1234") == False

def test_alphanumeric():
    # Test that plates are alphanumeric (no special characters)
    assert is_valid("ABC123") == True
    assert is_valid("ABC!") == False
    assert is_valid("A-B123") == False

def test_number_rules():
    # Test that numbers must appear at the end and no leading zero in numbers
    assert is_valid("ABC123") == True
    assert is_valid("AB12C") == False
    assert is_valid("ABC012") == False
    assert is_valid("AB12") == True

