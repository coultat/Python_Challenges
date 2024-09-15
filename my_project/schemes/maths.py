import re
from typing import List, Set, Tuple

from pydantic import BaseModel, field_validator  # type: ignore [attr-defined]
from pydantic_core import PydanticCustomError


class InputMax(BaseModel):
    choice: str | int

    @field_validator("choice")
    @classmethod
    def check_type(cls, v: str) -> int:
        if isinstance(v, str) and re.findall(r"(\D|\W|_)", v):
            invalid = re.findall(r"(\D|\W|_)", v)
            raise PydanticCustomError(
                "not_a_convertible",
                f"value can't be transformed into int. Wrong character {invalid}",
                dict(wrong_value=v),
            )
        return int(v)


class NumeroPrimo(BaseModel):
    number: int

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


class InputRomano(BaseModel):
    choice_roman: str | None = None
    choice_number: int | None = None

    @field_validator("choice_roman")
    @classmethod
    def check_type_roman(cls, v: str) -> str:
        if diff := set(v.upper()).difference({"I", "V", "X", "L", "C", "D", "M"}):
            raise ValueError(f"Invalid characters given as roman {diff}")

        return v

    @field_validator("choice_number")
    @classmethod
    def check_type(cls, v: str):
        if invalid := re.findall(r"(\D|\W|_)", v):
            raise ValueError(f"input number has invalid characters {invalid}")

        if v == "0":
            raise ValueError("Come on! You should know that romans didn't have number 0")

        return int(v)


class InputList(BaseModel):
    choice: list[int] | list[str]

    @field_validator("choice", mode="before")
    @classmethod
    def get_str_into(cls, v):
        try:
            return [int(x) for x in v]
        except ValueError as err:
            raise ValueError from err

    @field_validator("choice")
    @classmethod
    def validate_list_int(cls, v):
        if not all(isinstance(x, int) for x in v):
            raise ValueError
        return v
