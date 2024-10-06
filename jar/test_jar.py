import pytest
from jar import Jar

def test_jar_initialization():
    jar = Jar(10)
    assert jar.capacity == 10
    assert jar.size == 0

def test_jar_initialization_invalid_capacity():
    with pytest.raises(ValueError):
        Jar(-1)
    with pytest.raises(ValueError):
        Jar("a string")

def test_jar_deposit():
    jar = Jar(10)
    jar.deposit(5)
    assert jar.size == 5
    assert str(jar) == "🍪🍪🍪🍪🍪"

def test_jar_deposit_exceeds_capacity():
    jar = Jar(5)
    jar.deposit(5)
    with pytest.raises(ValueError):
        jar.deposit(1)

def test_jar_withdraw():
    jar = Jar(10)
    jar.deposit(5)
    jar.withdraw(2)
    assert jar.size == 3
    assert str(jar) == "🍪🍪🍪"

def test_jar_withdraw_not_enough_cookies():
    jar = Jar(10)
    jar.deposit(3)
    with pytest.raises(ValueError):
        jar.withdraw(4)
