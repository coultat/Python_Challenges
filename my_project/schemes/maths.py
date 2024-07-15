from pydantic import BaseModel, field_validator
import re
from typing import Set, List, Tuple
from exercises.maths.utils.exceptions import NotIntError


class InputMax(BaseModel):
    choice: str | int

    @field_validator('choice')
    @classmethod
    def check_type(cls, v: str) -> int:
        if isinstance(v, str) and re.findall("(\D|\W|_)", v):
            invalid = re.findall('(\D|\W|_)', v)
            raise NotIntError(message=f"input number has invalid characters {invalid}")
        return int(v)


class NumeroPrimo(BaseModel):
    number: str | int

    def __hash__(self):
        return hash(self.number)


class SetPrimeNumbers(BaseModel):
    set_prime_numbers: Set[NumeroPrimo]


class ParejaPrimos(BaseModel):
    parejas: Tuple[NumeroPrimo, NumeroPrimo]


class Relations(BaseModel):
    gemelos: List[ParejaPrimos]
    primos: List[ParejaPrimos]
    sexy: List[ParejaPrimos]