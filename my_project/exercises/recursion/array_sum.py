async def array_sum(calc_array: list[int]) -> int:
    """
    Calcula la suma de todos los números de una lista de forma recursiva
    :param calc_array: Lista con números
    :return: int. Suma de todos los ints de la lista
    """
    if len(calc_array) == 1:
        return calc_array[0]
    first_number = calc_array.pop()
    remaining = calc_array
    return await array_sum(remaining) + first_number
