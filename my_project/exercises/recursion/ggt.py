"escribir una función gcd(a, b) que halle el máximo común divisor de los dos números de forma recursiva"
"""
Todos los divisores comunes elevados a la menor de las potencias posibles
"""

async def calc_gcd(a, b):
    """
    Halla todos el mínimo común múltiplo de dos números. No veo mucho sentido práctico en hacerlo asíncrono, pero y lo
    que mola rizar el rizo?
    :param a: Primer número
    :param b: Segundo número
    :return: Mínimo Común Múltiplo
    """
    if b == 0:
        return a
    return await calc_gcd(b, a % b)
