import pytest

from genai_beispiele.taschen_rechner import Taschenrechner


def test_get_memory_is_empty_after_initialization():
    rechner = Taschenrechner()

    assert rechner.get_memory() == []


def test_add_stores_result_in_memory():
    rechner = Taschenrechner()

    assert rechner.add(2, 3) == 5
    assert rechner.get_memory() == [
        {"operation": "add", "left": 2, "right": 3, "result": 5}
    ]


def test_sub_stores_result_in_memory():
    rechner = Taschenrechner()

    assert rechner.sub(10, 4) == 6
    assert rechner.get_memory() == [
        {"operation": "sub", "left": 10, "right": 4, "result": 6}
    ]


def test_mul_stores_result_in_memory():
    rechner = Taschenrechner()

    assert rechner.mul(3, 7) == 21
    assert rechner.get_memory() == [
        {"operation": "mul", "left": 3, "right": 7, "result": 21}
    ]


def test_div_stores_result_in_memory():
    rechner = Taschenrechner()

    assert rechner.div(8, 2) == 4
    assert rechner.get_memory() == [
        {"operation": "div", "left": 8, "right": 2, "result": 4.0}
    ]


def test_div_by_zero_raises_exception():
    rechner = Taschenrechner()

    with pytest.raises(ZeroDivisionError, match="Division durch 0 ist nicht erlaubt"):
        rechner.div(5, 0)


def test_memory_keeps_only_last_three_calculations():
    rechner = Taschenrechner()

    rechner.add(1, 1)
    rechner.sub(5, 2)
    rechner.mul(3, 4)
    rechner.div(10, 2)

    assert rechner.get_memory() == [
        {"operation": "sub", "left": 5, "right": 2, "result": 3},
        {"operation": "mul", "left": 3, "right": 4, "result": 12},
        {"operation": "div", "left": 10, "right": 2, "result": 5.0},
    ]


def test_memory_alias_returns_same_history_as_get_memory():
    rechner = Taschenrechner()

    rechner.add(4, 6)

    assert rechner.memory() == rechner.get_memory()