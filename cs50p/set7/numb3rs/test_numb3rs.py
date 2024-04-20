from numb3rs import validate  # Assuming validate is defined elsewhere

def test_validate():
    """Test cases for the validate function, ensuring comprehensive validation."""

    # Valid IPv4 addresses with various ranges:
    assert validate("0.0.0.0") == True
    assert validate("192.168.1.1") == True
    assert validate("255.255.255.255") == True

    # Invalid IPv4 addresses:
    assert validate("300.0.0.1") == False  # Out of range (first octet)
    assert validate("1.2.3") == False        # Missing octets
    assert validate("1.2.3.4.5") == False     # Too many octets
    assert validate("127.0.0.1.1") == False  # Extra dot
    assert validate("hello") == False        # Non-numeric characters
    assert validate("123.456") == False       # Missing dots
    assert validate("-1.2.3.4") == False     # Negative numbers
    assert validate("  1.2.3.4  ") == False  # Leading/trailing whitespace

    # Edge cases:
    assert validate("0.255.255.255") == True   # Valid with all 255s
    assert validate("1000.0.0.0") == False    # Leading zero (potentially reserved)
    from numb3rs import validate  # Assuming validate is defined elsewhere

def test_validate():
    """Test cases for the validate function, ensuring comprehensive validation."""

    # Valid IPv4 addresses with various ranges:
    assert validate("0.0.0.0") == True
    assert validate("192.168.1.1") == True
    assert validate("255.255.255.255") == True

    # Invalid IPv4 addresses:
    assert validate("300.0.0.1") == False  # Out of range (first octet)
    assert validate("1.2.3") == False        # Missing octets
    assert validate("1.2.3.4.5") == False     # Too many octets
    assert validate("127.0.0.1.1") == False  # Extra dot
    assert validate("hello") == False        # Non-numeric characters
    assert validate("123.456") == False       # Missing dots
    assert validate("-1.2.3.4") == False     # Negative numbers
    assert validate("  1.2.3.4  ") == False  # Leading/trailing whitespace

    # Edge cases:
    assert validate("0.255.255.255") == True   # Valid with all 255s
    assert validate("1000.0.0.0") == False    # Leading zero (potentially reserved)
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("cat") == False
    assert validate("1.2.3.4") == True
    assert validate("11.99.22.88") == True
    assert validate("199.911.288.882") == False
    assert validate("249.249.249.249") == True





