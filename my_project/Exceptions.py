class ArgError(Exception):
    message: str


class WrongInput(ArgError):
    message = "this is not the format you are supposed to use in this function"


class LowerError(ArgError):
    message = "You are supposed to use capital letters"
