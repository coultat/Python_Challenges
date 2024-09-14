import pytest

from pydantic_core._pydantic_core import ValidationError

from my_project.schemes.maths import InputMax

from schemes.maths import NumeroPrimo


def test_inputmax():
    # Given the input and the expected result
    int_input = 1
    expected_result = 1

    # When creating the InputMax object
    result = InputMax(choice=int_input)

    # Then the result must match the expected one
    assert result.choice == expected_result


def test_str_inputmax():
    # Given the input and the expected result
    int_input = "1"
    expected_result = 1

    # When creating the InputMax object
    result = InputMax(choice=int_input)

    # Then the result must match the expected one
    assert result.choice == expected_result


def test_input_max_wrong_input():
    # Given the input and the expected result
    int_input = "-1"

    # When creating the InputMax object

    # Then the exception is raised
    with pytest.raises(ValueError):
        _ = InputMax(choice=int_input)


def test_numero_primo():
    # Given the input number and the expected result
    input_number = 3
    expected_result = 3

    # When creating a prime number object
    result = NumeroPrimo(number=input_number)

    # Then must match with the expected_result
    assert result.number == expected_result


def test_wrong_numero_primo():
    # Given the input number and the expected result
    input_number = ["a"]

    # When creating a prime number object

    # Then the exception is raised
    with pytest.raises(ValidationError):
        _ = NumeroPrimo(number=input_number)


def test_set_prime_numbers():
    ...
    # Given

    # When
    # Then
