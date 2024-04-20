from plates import is_valid


def test_is_valid_lenght():
    assert is_valid("CS5000") == True
    assert is_valid("CS") == True
    assert is_valid("CS500000") == False 
    
def test_is_valid_beginwith2letters():
    assert is_valid("CS5000") == True
    assert is_valid("50") == False
    assert is_valid("CS") == True
    assert is_valid("C") == False
    assert is_valid("5") == False
    
def test_is_valid_num():
    assert is_valid("CS5000") == True
    assert is_valid("CS500") == True
    assert is_valid("CS500F") == False
    
def test_is_valid_punct():
    assert is_valid("CS50!") == False