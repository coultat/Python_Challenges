import pytest

from my_project.exercises.basics.maths.suma_estatistica_ii import (
    calc_sum_and_count_all_numbers_div_by_2_or_7 as calc)


def test_calc_sum_and_count_all_numbers_div_by_2_or_7():
    # Given the input_max and the expected_results
    input_max = 8
    cantidad_esperada = 4
    suma_esperada = 19

    # When calculating the calc_sum_and_count_all_numbers_div_by_2_or_7
    result_cantidad, result_suma = calc(input_max)

    assert result_suma == suma_esperada
    assert cantidad_esperada == result_cantidad


def test_calc_sum_and_count_all_numbers_div_by_2_or_7_wrong():
    # Given the wrong input_max and the expected_results
    input_max = '8'

    # When calculating the calc_sum_and_count_all_numbers_div_by_2_or_7
    with pytest.raises(AssertionError):
        calc(input_max)
