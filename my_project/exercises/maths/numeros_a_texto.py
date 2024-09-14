"""
Escribir una función que convierta los números en texto. Así 7 será "siete", 55 será "cinco cinco"
"""



class NumberText:
    def __init__(self, input_number: int):
        self.input_number = str(input_number)

    async def number_as_text(self) -> str:
        numbers_dict = {
            "1": "UNO",
            "2": "DOS",
            "3": "TRES",
            "4": "CUATRO",
            "5": "CINCO",
            "6": "SEIS",
            "7": "SIETE",
            "8": "OCHO",
            "9": "NUEVE",
            "0": "CERO",
        }
        str_result = ""
        for i in self.input_number:
            str_result += numbers_dict[i] + " "

        return str_result[:-1]
