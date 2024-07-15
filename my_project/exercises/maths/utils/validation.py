from .exceptions import NegativeNumberError, NotIntError
import re


def transform_int_str(input_number):
    try:
        input_number = int(input_number)
    except ValueError:
        raise ValueError("The input must be a number and not str characters")

    if input_number < 0:
        raise NegativeNumberError

    return input_number


def validate_int_str(input_number, return_int: bool = False):
    if invalid := re.findall("(\D|\W|_)", input_number):
        raise NotIntError(message=f"input number has invalid characters {invalid}")
    if return_int:
        return int(input_number)
    return input_number
