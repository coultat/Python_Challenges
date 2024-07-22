"""
Crear dos funciones:
    - is_even te dice si un número es par
    - is_odd te dice si un número es impar
Nota: este fue el primer programa que tuve que hacer en las primeras clases de programación.
Me dolía la cabeza de tanto pensar cuando lo terminé (y me dijeron la respuesta)
"""
from schemes.maths import InputMax


class ParImpar:
    def __init__(self, choice: InputMax):
        self.choice = choice.choice

    async def is_even(self) -> str:
        return "is even" if self.choice % 2 == 0 else "is not even"

    async def is_odd(self) -> str:
        return "is odd" if self.choice % 2 != 0 else "is even"
