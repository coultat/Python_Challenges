import pytest

from my_project.exercises.basics.maths.suma_basica import calc


def test_calc():
    # Given the input parameters and the expected result
    input_m = 6
    input_n = 7
    expected_result = 0

    # when running the calc function
    result = calc(input_m, input_n)

    # Then the result must match with the expected result
    assert result == expected_result


def test_calc_wrong():
    # Given the wrong input parameters and the expected result
    input_m = 'a'
    input_n = '7'
    expected_result = 0

    # when running the calc function, we get a TypeError
    with pytest.raises(TypeError):
        result = calc(input_m, input_n)

        # Then the result must match with the expected result
        assert result == expected_result

