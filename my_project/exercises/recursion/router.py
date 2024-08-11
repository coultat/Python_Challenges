from typing import Dict, Union
from my_project.schemes.maths import InputMax
from fastapi import APIRouter, Query

from my_project.exercises.recursion.count_digits import count_digits
from pydantic_core._pydantic_core import ValidationError

from my_project.exercises.recursion.fibonacci import fibonacci

from my_project.exercises.recursion.ggt import calc_gcd

from my_project.exercises.recursion.reverse_str import reverse_string

recursion_router = APIRouter(prefix="/recursion")


@recursion_router.get("/count_digits/{input_number}")
async def sumatorio(input_number: str) -> Dict[str, Union[str, int]]:
    try:
        input_number = InputMax(choice=input_number)
        return {'result': await count_digits(input_number.choice)}
    except ValidationError as e:
        return {"error": str(e)}


@recursion_router.get("/fibonacci/{input_number}")
async def calcular_fibonacci(input_max: str) -> Dict[str, Union[str, int]]:
    try:
        input_number = InputMax(choice=input_max)
        return {'result': await fibonacci(input_number.choice)}
    except ValidationError as e:
        return {"error": str(e)}


@recursion_router.get("/minimo_comun_multiplo")
async def calcular_minimo_comun_multiplo(
        primer_numero: str = Query(..., title="Primero de los números"),
        segundo_numero: str = Query(..., title="Segundo de los números")
) -> Dict[str, Union[str, int]]:
    try:
        primer_numero = InputMax(choice=primer_numero)
        segundo_numero = InputMax(choice=segundo_numero)
        return {'result': await calc_gcd(primer_numero, segundo_numero)}
    except ValidationError as e:
        return {"error": str(e)}


@recursion_router.get("/reversed_string")
async def calcular_reversed_string(
        palindrome: str = Query(..., title="String para ser invertida"),
) -> Dict[str, Union[str, int]]:
    try:
        return {'result': await reverse_string(palindrome)}
    except ValidationError as e:
        return {"error": str(e)}
