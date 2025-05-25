import pytest

from task1.solution import strict


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


@strict
def multiply(a: float, b: float) -> float:
    return a * b


@strict
def is_equal(a: bool, b: bool) -> bool:
    return a == b


def test_correct_int():
    assert sum_two(1, 2) == 3


def test_correct_float():
    assert multiply(1.5, 2.0) == 3.0


def test_correct_bool():
    assert is_equal(True, True) is True


def test_incorrect_int():
    with pytest.raises(TypeError):
        sum_two(1.0, 2)


def test_incorrect_float():
    with pytest.raises(TypeError):
        multiply(1, 2.0)


def test_incorrect_bool():
    with pytest.raises(TypeError):
        is_equal(1, True)


def test_kwargs():
    @strict
    def kwfunc(a: int, b: float) -> float:
        return a + b

    assert kwfunc(a=1, b=2.0) == 3.0
    with pytest.raises(TypeError):
        kwfunc(a=1.0, b=2.0)
