import sys


async def array_min(input_value: list[str]) -> int:
    return await min_helper(input_value, 0, sys.maxsize)

async def min_helper(values, pos, min_value):
    if pos >= len(values):
        return min_value

    value = values[pos]
    if value < min_value:
        min_value = value

    return await min_helper(values, pos + 1, min_value)

