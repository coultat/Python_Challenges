from my_project.exercises.basics.maths.numeros_romanos import int_to_roman, roman_to_int

import pytest


def test_int_to_roman():
    # Given the input value and the expected result
    input_value = 158
    expected_result = 'CLVIII'

    # When turning the int into roman number
    result = int_to_roman(input_value)

    # Then the result must match
    assert expected_result == result