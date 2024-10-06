import pytest
from fuel import convert, gauge

def test_convert():
    # Test valid inputs
    assert convert("3/4") == 75
    assert convert("1/4") == 25
    assert convert("1/1") == 100
    assert convert("0/1") == 0

    # Test X > Y raises ValueError
    with pytest.raises(ValueError):
        convert("3/2")

    # Test non-integer input raises ValueError
    with pytest.raises(ValueError):
        convert("3/a")

    # Test division by zero raises ZeroDivisionError
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_gauge():
    # Test edge cases
    assert gauge(1) == "E"
    assert gauge(99) == "F"

    # Test percentages in between
    assert gauge(50) == "50%"
    assert gauge(75) == "75%"
    assert gauge(0) == "E"
    assert gauge(100) == "F"
