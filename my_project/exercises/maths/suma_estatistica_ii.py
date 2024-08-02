"""
Crear una función llamada calc_sum_and_count_all-numbers_div_by_2_or_7 que
 - vaya de 1 a un número máximo definido
 - sea capaz de mostrar la cantidad de números entre 0
 y el max que sean divisibles por 2 o 7
 - mostrar también la suma de esos números
 ejemplo
    número 15: tiene los siguientes divisibles por 2: 2, 4, 6, 8, 10, 12, 14
                tiene los siguientes divisibles por 7: 7, 14
                En total tiene la siguiente cantidad de números (2, 4, 6, 8,
                10, 12, 14, 7)
                Esa cantidad de números suma 63
"""

from typing import Tuple

from my_project.schemes.maths import InputMax


async def calc_sum_and_count_all_numbers_div_by_2_or_7(
    input_max: InputMax,
) -> Tuple[int, int]:
    counter = 1
    divisible = set()
    while counter < input_max.choice:
        if counter % 7 == 0 or counter % 2 == 0:
            divisible.add(counter)
        counter += 1
    return len(divisible), sum(divisible)
