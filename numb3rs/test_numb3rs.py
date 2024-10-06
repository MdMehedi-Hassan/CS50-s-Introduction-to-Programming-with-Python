from numb3rs import validate

def test_valid_ips():
    assert validate("192.168.0.1") == True
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True

def test_invalid_ips():
    assert validate("275.3.6.28") == False  # Invalid because 275 is out of range
    assert validate("123.456.78.90") == False  # Invalid because 456 is out of range
    assert validate("192.168.0") == False  # Invalid because it's missing one part
    assert validate("192.168.0.1.1") == False  # Invalid because it has an extra part
    assert validate("192.168.a.1") == False  # Invalid because 'a' is not a number
