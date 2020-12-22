class BinaryNumber:
    def __init__(self, number) -> None:
        self._number = number


def add_binary_boolean(a: str, b: str) -> str:
    """ homegrown implementation using boolean logic"""

    return "0"


def add_binary_builtin(*args: str) -> str:
    """ implementation using pythons built in functions """
    integer_sum = sum([int(x, 2) for x in args])
    return bin(integer_sum)[2:]