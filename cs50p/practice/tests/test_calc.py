from calc import square
import pytest

def test_square_positive():
    assert square(2)==4
    assert square(3)==9

def test_square_negative():
    assert square(-3) == 9
    assert square(-4) == 16
    
def test_square_zero():
    assert square(0) == 0

def test_square_str():
    with pytest.raises(TypeError):
        square("asdgs")