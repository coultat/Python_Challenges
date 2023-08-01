"""
Crear dos funciones:
    - is_even te dice si un número es par
    - is_odd te dice si un número es impar
Nota: este fue el primer programa que tuve que hacer en las primeras clases de programación.
Me dolía la cabeza de tanto pensar cuando lo terminé (y me dijeron la respuesta)
"""


def is_even(number):
    assert isinstance(number, int) and number != 0
    return "is even" if number % 2 == 0 else "is not even"


def is_odd(number):
    assert isinstance(number, int) and number != 0
    return "is odd" if number % 2 != 0 else "is even"
