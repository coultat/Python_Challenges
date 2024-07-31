# Escribir una función calc(m, n) que:
#     - multiplica dos variables de tipo int
#     - luego divide a la mitad el resultado anterior
#     - muestra el resto de dividir el resultado anterior entre 7
from my_project.schemes.maths import InputMax


class Calc:
    def __init__(self, m: InputMax, n: InputMax):
        self.m = m.choice
        self.n = n.choice

    async def hacer_el_paripe(self) -> int:
        return int((int(self.m * self.n) / 2) % 7)
