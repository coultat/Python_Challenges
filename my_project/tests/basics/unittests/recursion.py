import pytest

from exercises.recursion.array_min import array_min
from exercises.recursion.array_sum import array_sum
from exercises.recursion.calc_binary import calc_binary
from exercises.recursion.count_digits import count_digits
from exercises.recursion.fibonacci import fibonacci
from exercises.recursion.ggt import calc_gcd
from exercises.recursion.reverse_str import reverse_string


@pytest.mark.parametrize("values, expected", [([1], 1), ([1, 2, 3], 6), ([1, 2, 3, -7], -1)])
async def test_sum_rec(values, expected):
    assert await array_sum(values) == expected


@pytest.mark.parametrize("values, expected", [(11, 89), (5, 5), (10, 55)])
async def test_fibonacci(values, expected):
    assert await fibonacci(values) == expected


@pytest.mark.parametrize("values, expected", [(3, 6), (5, 15)])
async def test_count_digits(values, expected):
    assert await count_digits(values) == expected


@pytest.mark.parametrize("value1, value2, expected", [(20, 12, 4)])
async def test_recursive_ggt(value1, value2, expected):
    assert await calc_gcd(value1, value2) == expected


@pytest.mark.parametrize("values, expected", [("roma", "amor")])
async def test_reverse_str(values, expected):
    assert await reverse_string(values) == expected


@pytest.mark.parametrize("values, expected", [([1, 2, 3, 4, 5, 6, -9], -9)])
async def test_array_min(values, expected):
    assert await array_min(values) == expected


@pytest.mark.parametrize("value, expected", [(2, "10"), (5, "101")])
async def test_calc_binary(value, expected):
    assert await calc_binary(value) == expected
