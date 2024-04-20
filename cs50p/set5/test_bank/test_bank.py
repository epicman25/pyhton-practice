from bank import value

def test_value():
    assert value("hello tejesh") == 0
    assert value("HELLO TEJESH") == 0
    assert value("hi5 world") == 20
    assert value("HI WORLD") == 20
    assert value("5432 world") == 100
    assert value("good morning") == 100
