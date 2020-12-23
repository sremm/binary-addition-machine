from __future__ import annotations

from typing import List, Tuple


def carry_component(a: bool, b: bool) -> bool:
    """ the carry component is just AND """
    return a and b


def sum_component(a: bool, b: bool) -> bool:
    """ the sum component is XOR """
    return a != b


def half_adder(a: bool, b: bool) -> Tuple[bool, bool]:
    return sum_component(a, b), carry_component(a, b)


def full_adder(a: bool, b: bool, carry_in: bool) -> Tuple[bool, bool]:
    sum_out_1, carry_out_1 = half_adder(a, b)
    sum_out_2, carry_out_2 = half_adder(carry_in, sum_out_1)
    sum_out = sum_out_2
    carry_out = carry_out_1 or carry_out_2
    return sum_out, carry_out


def digit_to_bool(digit: str) -> bool:
    if digit == "1":
        return True
    if digit == "0":
        return False
    raise ValueError(f"Digit can only be '0' or '1', but got {digit=}")


def bool_to_digit(a: bool) -> str:
    return "1" if a else "0"


class BinaryNumber:
    def __init__(self, number: str) -> None:
        self._number: str = number
        self._binary_digits: List[bool] = [digit_to_bool(x) for x in number]

    def __add__(self, other: BinaryNumber) -> BinaryNumber:
        """ implements addition for BinaryNumber """
        out_str = ""
        cur_carry: bool = False
        len_1, len_2 = len(self._binary_digits), len(other._binary_digits)
        longer_number = (
            self._binary_digits if len_1 >= len_2 else other._binary_digits
        )[::-1]
        shorter_number = (
            self._binary_digits if len_1 < len_2 else other._binary_digits
        )[::-1]
        for idx, digit_1 in enumerate(longer_number):
            digit_2 = shorter_number[idx] if idx < len(shorter_number) else False
            sum_out, carry_out = full_adder(digit_1, digit_2, cur_carry)
            out_str += bool_to_digit(sum_out)
            cur_carry = carry_out
        if cur_carry == True:
            out_str += "1"
        # reversed output
        out_str = out_str[::-1]
        return BinaryNumber(out_str)

    def __str__(self) -> str:
        return self._number

    def __repr__(self) -> str:
        return self._number


def add_binary_boolean(*args: str) -> str:
    """ homegrown implementation using boolean logic"""
    # convert all arguments to binary number class
    binary_numbers: List[BinaryNumber] = [BinaryNumber(x) for x in args]
    binary_summed = sum(binary_numbers, BinaryNumber("0"))
    return str(binary_summed)


def add_binary_builtin(*args: str) -> str:
    """ implementation using pythons built in functions """
    integer_sum = sum([int(x, 2) for x in args])
    return bin(integer_sum)[2:]
