from my_project.exercises.basics.maths.numeros_primos import calc_primes_up_to

import pytest


def test_calc_primes_up_to():
    # Given the input_max and the expected_result
    input_max = 30
    expected_result = {1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29}

    # When calculating the prime numbers till 30
    result = calc_primes_up_to(input_max)

    # Then the result must match with the expected_result
    assert expected_result == result


def test_calc_primes_up_to_wrong_string_input():
    # Given the wrong input_max
    input_max = '30'
    expected_result = {1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29}

    # When looking for the TypeError error
    with pytest.raises(TypeError):
        result = calc_primes_up_to(input_max)

    # Then it's correct