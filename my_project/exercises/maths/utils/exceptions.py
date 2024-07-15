class NegativeNumberError(Exception):
    def __init__(self, message="Input number must be >= 0"):
        super().__init__(message)


class NotIntError(Exception):
    def __init__(self, message="Input number has unvalid characters"):
        self.message = message
        super().__init__(message)


class LowLimitError(Exception):
    def __init__(self, message="The input number is too low for the calculation", input_number=0):
        self.message = message
        self.input_number = input_number
        super().__init__(message)