from secrets import choice
from typing import Dict, Union
from my_project.schemes.maths import InputMax
from fastapi import APIRouter, Query

from my_project.exercises.recursion.count_digits import count_digits
from pydantic_core._pydantic_core import ValidationError

from my_project.exercises.recursion.fibonacci import fibonacci

from my_project.exercises.recursion.ggt import calc_gcd

from my_project.exercises.recursion.reverse_str import reverse_string

from my_project.exercises.recursion.array_sum import array_sum
from my_project.exercises.recursion.calc_binary import calc_binary
from my_project.schemes.maths import InputList

from my_project.exercises.recursion.array_min import array_min

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
    except Exception as e:
        return {"error": str(e)}


@recursion_router.get("/calculadora_binaria")
async def binary_calc(
        valor: str = Query(..., title="Número para ser calculado en binario"),
) -> Dict[str, str]:
    try:
        valor = InputMax(choice=valor)
        return {'result': await calc_binary(valor.choice)}
    except ValidationError as e:
        return {'error': str(e.args)}


@recursion_router.get("/suma_array")
async def summa_array(
        valor_lista: list[int] = Query(..., title="Lista de números para que sean sumados")
) -> Dict[str, Union[int, str]]:
    try:
        valor_lista = InputList(choice=valor_lista)
        return {"result": await array_sum(valor_lista.choice)}
    except ValidationError as e:
        return {"error": str(e)}


@recursion_router.get("/array_min")
async def calc_array_min(
        valor_lista: list[int] = Query(..., title="Intruoduce una lista de números para que devuelva el valor mínimo")
):
    try:
        valor_lista = InputList(choice=valor_lista)
        return {"result": await array_min(valor_lista.choice)}
    except ValidationError as e:
        return {"error": str(e)}
