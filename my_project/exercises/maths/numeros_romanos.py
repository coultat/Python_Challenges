# Crear un programa para que nos genere números primos a partir de un int que le pasamos
# from my_project.Exceptions import WrongInput
from schemes.maths import InputRomano


class Romans:
    def __init__(self, input_roman: InputRomano = None, input_number: InputRomano = None):
        self.roman = input_roman.choice_roman if input_roman is not None else None
        self.number = input_number.choice_number if input_number is not None else None

    async def int_to_roman(self) -> str:
        result = ''
        num = [1, 4, 5, 9, 10, 40, 50, 90,
               100, 400, 500, 900, 1000]
        sym = ["I", "IV", "V", "IX", "X", "XL",
               "L", "XC", "C", "CD", "D", "CM", "M"]
        i = len(sym) - 1

        while self.number:
            div = self.number // num[i]
            self.number %= num[i]
            while div:
                result += sym[i]
                div -= 1
            i -= 1
        return result

    async def roman_to_int(self) -> int:
        rom_dict = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'XC': 90, 'C': 100, 'CD': 400,
                    'D': 500,
                    'CM': 900, 'M': 1000}
        acum = 0
        while self.roman:
            for rom in reversed(rom_dict):
                if rom in self.roman[:len(rom)]:
                    acum += rom_dict[rom]
                    self.roman = self.roman[len(rom):]
                    break
        return acum
