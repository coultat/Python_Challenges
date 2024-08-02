from exercises.maths.numeros_a_texto import NumberText
from exercises.maths.par_impar_III import ParImpar
from exercises.maths.suma_basica import Calc
from exercises.maths.suma_estatistica_ii import (
    calc_sum_and_count_all_numbers_div_by_2_or_7,
)
from exercises.maths.utils.exceptions import ZeroNumberError
from schemes.maths import InputMax
import pytest


@pytest.mark.asyncio
async def test_suma_basica():
    # Given the first and second sumandos as well as the expected result
    sumando1 = InputMax(choice=5)
    sumando2 = InputMax(choice=10)
    expected_result = 4

    # When doing the basic sum
    result = await Calc(sumando1, sumando2).hacer_el_paripe()

    # Then it must match with the expected result
    assert expected_result == result


@pytest.mark.asyncio
async def test_suma_estatistica():
    # Given the first_input and the second_input values as well as the expected result
    first_input_value = InputMax(choice=10)
    expected_result = (5, 27)

    # When doing the statistic sum
    result = await calc_sum_and_count_all_numbers_div_by_2_or_7(first_input_value)

    # Then the result must match
    assert result == expected_result


@pytest.mark.asyncio
async def test_wrong_suma_estatistica():
    # Given the first_input and the second_input values as well as the expected result
    first_input_value = InputMax(choice=10)
    expected_result = (5, 28)

    # When doing the statistic sum
    with pytest.raises(AssertionError):
        result = await calc_sum_and_count_all_numbers_div_by_2_or_7(first_input_value)

        # Then the exception must be raised
        assert expected_result == result


@pytest.mark.asyncio
async def test_par_impar():
    # Given input and two expected result
    first_input = InputMax(choice=43)
    expected_is_odd = "is odd"
    expected_is_not_even = "is not even"

    # When doing the calc
    first_result = await ParImpar(first_input).is_even()
    second_input = await ParImpar(first_input).is_odd()

    # Then the result must match with the expected result
    assert expected_is_odd == second_input
    assert expected_is_not_even == first_result


@pytest.mark.asyncio
async def test_par_impar_with_zero():
    # Given input and two expected result
    first_input = InputMax(choice=0)

    with pytest.raises(ZeroNumberError):
        _ = await ParImpar(first_input).is_odd()


@pytest.mark.asyncio
async def test_numeros_a_texto():
    # Given the input and the expected result
    number_input = InputMax(choice=33)
    expected_result = "TRES TRES"

    # When converting the numbers into text
    result = await NumberText(number_input).number_as_text()

    # Then the result must match with the expected result
    assert result == expected_result
