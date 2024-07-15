"""
Escribir una función que convierta los números en texto. Así 7 será "siete", 55 será "cinco cinco"
"""

def number_as_text(input_number):
    assert isinstance(input_number, int) and input_number > 0, \
        "Número ha de ser positivo e int"
    input_number = list(str(input_number))
    numbers_dict = {'1': 'UNO', '2': 'DOS', '3': 'TRES', '4': 'CUATRO',
                    '5': 'CINCO', '6': 'SEIS', '7': 'SIETE', '8': 'OCHO',
                    '9': 'NUEVE', '0': 'CERO'}
    str_result = ""
    for i in input_number:
        str_result += numbers_dict[i] + ' '

    return str_result[:-1]