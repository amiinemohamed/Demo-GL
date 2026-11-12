from calculator.operations import add
import pytest


def test_add_invalid_type():
    with pytest.raises(TypeError):
        add("2", 3)


def test_add_positive():
    assert add(2, 3) == 5


def test_add_negative():
    assert add(-1, -1) == -2


def test_add_zero():
    assert add(0, 5) == 5
