from twttr import shorten

def test_shorten():
    assert shorten("Twitter") == 'Twttr'
    assert shorten("AEIOU") == ''
    assert shorten("Tejesh") == 'Tjsh'
    assert shorten("India") == 'nd'