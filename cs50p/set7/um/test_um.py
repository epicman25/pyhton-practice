import pytest
from um import count


def test_input():
    assert count("Um, THis is so randum") == 1
    assert count("um") == 1
    assert count("Um, this is also random, um...") == 2
    assert count("Um?") == 1