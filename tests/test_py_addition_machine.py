from py_addition_machine.main import add_binary_boolean, add_binary_builtin

import pytest


one_bit_combinations = (
    ["0", "0", "0"],
    ["1", "0", "1"],
    ["0", "1", "1"],
    ["1", "1", "10"],
)
two_bit_combinations = (
    ["10", "1", "11"],
    ["10", "10", "100"],
    ["10", "11", "101"],
    ["11", "11", "110"],
)


class TestBoolean:
    @pytest.mark.parametrize(
        "a,b,expected_result",
        one_bit_combinations,
    )
    def test_one_bit_numbers(self, a, b, expected_result):
        result = add_binary_boolean(a, b)
        assert result == expected_result, f"{result=} != {expected_result=}"

    @pytest.mark.parametrize(
        "a,b,expected_result",
        two_bit_combinations,
    )
    def test_two_bit_numbers(self, a, b, expected_result):
        result = add_binary_boolean(a, b)
        assert result == expected_result, f"{result=} != {expected_result=}"


class TestBuiltIn:
    @pytest.mark.parametrize(
        "a,b,expected_result",
        one_bit_combinations,
    )
    def test_one_bit_numbers(self, a, b, expected_result):
        result = add_binary_builtin(a, b)
        assert result == expected_result, f"{result=} != {expected_result=}"

    @pytest.mark.parametrize(
        "a,b,expected_result",
        two_bit_combinations,
    )
    def test_two_bit_numbers(self, a, b, expected_result):
        result = add_binary_builtin(a, b)
        assert result == expected_result, f"{result=} != {expected_result=}"
