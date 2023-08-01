from random import randint
import pytest

from my_project.exercises.basics.maths.par_impar_III import is_odd, is_even


def test_is_even():
    # Given the input value and the expected result
    input_value = 8
    expected_result = 'is even'

    # When checking if it's even
    result = is_even(input_value)

    # Then the result must match the expected result
    assert expected_result == result


def test_is_odd():
    # Given the input value and the expected result
    input_value = 5
    expected_result = 'is odd'

    # When checking if it's even
    result = is_odd(input_value)

    # Then the result must match the expected result
    assert expected_result == result


def test_is_even_wrong():
    # Given the wrong input value
    input_value = [0, 'a'][randint(0, len([0, 'a']) - 1)]

    # When checking if it's even
    with pytest.raises(AssertionError):
        result = is_odd(input_value)

    # Then it's correct
