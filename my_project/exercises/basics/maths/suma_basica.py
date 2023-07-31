# Escribir una función calc(m, n) que:
#     - multiplica dos variables de tipo int
#     - luego divide a la mitad el resultado anterior
#     - muestra el resto de dividir el resultado anterior entre 7


def calc(m, n):
    return int((int(m * n) / 2) % 7)
