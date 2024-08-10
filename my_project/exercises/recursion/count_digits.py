async def count_digits(n) -> int:
    """
    Cuenta recursivamente todos los números desde el 0 hasta el n
    Ejemplo: 7: 7 + 6 + 5 + 4 + 3 + 2 + 1
    :param n:
    :return: int
    """
    if n == 1:
        return n
    return n + await count_digits(n - 1)
