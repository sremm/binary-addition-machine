from py_addition_machine.main import add_binary

import pytest


@pytest.mark.parametrize(
    "a,b,expected_result", ([0, 0, 0], [1, 0, 1], [0, 1, 1], [1, 1, 10])
)
def test_one_bit_numbers(a, b, expected_result):
    result = add_binary(a, b)
    assert result == expected_result, f"{result=} != {expected_result=}"


@pytest.mark.parametrize(
    "a,b,expected_result", ([10, 1, 11], [10, 10, 100], [10, 11, 101], [11, 11, 110])
)
def test_two_bit_numbers(a, b, expected_result):
    result = add_binary(a, b)
    assert result == expected_result, f"{result=} != {expected_result=}"