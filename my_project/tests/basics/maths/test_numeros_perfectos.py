from my_project.exercises.basics.maths.numeros_perfectos_III import calc_perfect_numbers

import pytest


def test_calc_perfect_numbers():
    # Given the input_max and the expected_result
    input_max = 10000
    expected_result = {6, 28, 496, 8128}

    # When running the program
    res = calc_perfect_numbers(input_max)

    # Then the result must match with the expected_result
    assert expected_result == res


def test_calc_perfect_numbers_wrong():
    # Given the input_max and the expected_result
    input_max = '10000'

    # When running the program

    # Then there is an assertion error
    with pytest.raises(AssertionError):
        res = calc_perfect_numbers(input_max)
