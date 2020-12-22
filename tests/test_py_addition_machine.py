from typing import Callable
from py_addition_machine.main import add_binary_boolean, add_binary_builtin

import pytest


implementations = [add_binary_builtin, add_binary_boolean]


@pytest.fixture(params=implementations)
def implementation_func(request) -> Callable:
    return request.param


one_bit_combinations = (
    ["0", "0", "0"],
    ["1", "0", "1"],
    ["0", "1", "1"],
    ["1", "1", "10"],
)


@pytest.mark.parametrize(
    "a,b,expected_result",
    one_bit_combinations,
)
def test_one_bit_numbers(implementation_func, a, b, expected_result):
    result = implementation_func(a, b)
    assert result == expected_result, f"{result=} != {expected_result=}"


two_bit_combinations = (
    ["10", "1", "11"],
    ["10", "10", "100"],
    ["10", "11", "101"],
    ["11", "11", "110"],
)


@pytest.mark.parametrize(
    "a,b,expected_result",
    two_bit_combinations,
)
def test_two_bit_numbers(implementation_func, a, b, expected_result):
    result = implementation_func(a, b)
    assert result == expected_result, f"{result=} != {expected_result=}"
