"""
Escribir una función que halle todos los números perfectos del 1 al n.
Un número perfecto es es un número entero positivo que es igual a la suma
de sus divisores propios positivos. Dicho de otra forma, un número perfecto
es aquel que es amigo de sí mismo.

Así, 6 es un número perfecto porque sus divisores propios positivos
son 1, 2 y 3; y 6 = 1 + 2 + 3. Un divisor propio positivo de un número
es un factor positivo de ese número que no sea el propio número.
Por ejemplo, los divisores propios de 6 son 1, 2 y 3, pero no 6.
Los siguientes números perfectos son 28, 496 y 8128.
"""

def calc_perfect_numbers(input_max):
    assert isinstance(input_max, int) and input_max > 3, \
        "Número tiene que ser positivo, entero y mayor que tres"
    perfect_numbers = set()
    divisores = set()
    for i in range(2, input_max):
        for j in range(1, i):
            if i % j == 0:
                divisores.add(j)
        if sum(divisores) == i:
            perfect_numbers.add(i)
        divisores = set()

    return perfect_numbers
