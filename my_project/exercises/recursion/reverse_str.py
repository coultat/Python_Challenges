async def reverse_string(input_str: str) -> str:
    """
    Calcula de forma recursiva el inverso de una string introducida.
    OLIVER Y FELIX -> XILEF Y REVILO
    :param input_str: str que será manipulada
    :return: reverso de la str
    """
    if len(input_str) == 1:
        return input_str
    first_char = input_str[0]
    remaining = input_str[1:]
    return await reverse_string(remaining) + first_char
