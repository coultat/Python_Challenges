import sys


def array_min(input_value: list[str]) -> int:
    return min_helper(input_value, 0, sys.maxsize)

def min_helper(values, pos, min_value):
    if pos >= len(values):
        return min_value

    value = values[pos]
    if value < min_value:
        min_value = value

    return min_helper(values, pos + 1, min_value)

