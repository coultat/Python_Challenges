# Crear un programa para que nos genere números primos a partir de un int que le pasamos
# from my_project.Exceptions import WrongInput

def int_to_roman(number):
    if not isinstance(number, int) or number < 1:
        raise ValueError("number to convert must be positive and int")

    result = ''
    num = [1, 4, 5, 9, 10, 40, 50, 90,
           100, 400, 500, 900, 1000]
    sym = ["I", "IV", "V", "IX", "X", "XL",
           "L", "XC", "C", "CD", "D", "CM", "M"]
    i = len(sym) - 1

    while number:
        div = number // num[i]
        number %= num[i]

        while div:
            result += sym[i]
            div -= 1
        i -= 1

    return result


def roman_to_int(number):
    if not isinstance(number, str):
        raise ValueError("Input number must be a string")

    rom_dict = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'XC': 90, 'C': 100, 'CD': 400, 'D': 500,
                'CM': 900, 'M': 1000}
    acum = 0
    while number:
        for rom in reversed(rom_dict):
            if rom in number[:len(rom)]:
                acum += rom_dict[rom]
                number = number[len(rom):]
                break
    return acum