from typing import Callable
from py_addition_machine.main import add_binary_boolean, add_binary_builtin
from hypothesis import given
import hypothesis.strategies as s
import pytest


@given(s.integers(min_value=0), s.integers(min_value=0))
def test_binary_and_built_in_implementation_return_same_values(integer1, integer2):
    binary1, binary2 = bin(integer1)[2:], bin(integer2)[2:]
    assert add_binary_boolean(binary1, binary2) == add_binary_builtin(binary1, binary2)


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


three_bit_combinations = (
    ["1001", "101", "1110"],
    ["1110", "1001", "10111"],
    ["10", "1101", "1111"],
    ["1", "1000", "1001"],
)


@pytest.mark.parametrize(
    "a,b,expected_result",
    three_bit_combinations,
)
def test_three_bit_numbers(implementation_func, a, b, expected_result):
    result = implementation_func(a, b)
    assert result == expected_result, f"{result=} != {expected_result=}"


many_bit_combinations = (
    ["010010011001", "1110001001011", "10000011100100"],
    [
        "010010011001100101011101100101",
        "111000100101100001111000011",
        "11001011110010001101100101000",
    ],
)


@pytest.mark.parametrize(
    "a,b,expected_result",
    three_bit_combinations,
)
def test_many_bit_numbers(implementation_func, a, b, expected_result):
    result = implementation_func(a, b)
    assert result == expected_result, f"{result=} != {expected_result=}"