import pytest

from my_project.exercises.basics.maths.numeros_a_texto import number_as_text


def test_numbers_as_text():
    # Given the input_number and the expected_result
    input_number = 258
    expected_result = "DOS CINCO OCHO"

    # When executing the function
    result = number_as_text(input_number)


    # Then the result must match the expected
    assert expected_result == result


def test_numbers_as_text_wrong():
    # Given the input_number and the expected_result
    input_number = 0

    # When executing the function with the wrong input
    with pytest.raises(AssertionError):
        result = number_as_text(input_number)

    # Then the result must match the expected