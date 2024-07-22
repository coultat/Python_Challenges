import asyncio
from pydantic import ValidationError
from schemes.maths import InputMax, Relations, SetPrimeNumbers, InputRomano
from .numeros_a_texto import number_as_text
from .numeros_perfectos_III import calc_perfect_numbers
from .numeros_primos import CalcularNumerosPrimos
from fastapi import APIRouter, Query
from typing import Dict, Set, Union, Tuple

from .numeros_romanos import Romans
from .par_impar_III import ParImpar
from .suma_basica import Calc
from .suma_estatistica_ii import calc_sum_and_count_all_numbers_div_by_2_or_7
from .utils.exceptions import NotIntError, LowLimitError


math_router = APIRouter(prefix="/math")

@math_router.get("/number_into_text/{input_number}")
async def numeros_a_texto(input_number: str) -> Dict[str, str]:
    try:
        return await number_as_text(input_number)
    except NotIntError:
        return {'error': f'{NotIntError().message}'}


@math_router.get("/calc_perfect_numbers/{input_limit}")
async def calcular_numeros_perfectos(input_limit: str) -> Union[Dict[str, Set[int]], Dict[str, str]]:
    try:
        return await calc_perfect_numbers(input_limit)
    except NotIntError:
        return {'error': NotIntError().message}
    except LowLimitError:
        return {'error': f'{LowLimitError(input_number=input_limit).message}'}


@math_router.get("/calc_prime_numbers/{input_limit}")
async def calcular_numeros_primos(input_limit: str) -> Union[Dict[str, SetPrimeNumbers], Dict[str, str]]:
    try:
        return {'result': await CalcularNumerosPrimos(InputMax(choice=input_limit)).calcular_primos()}
    except ValidationError as e:
        return {'error': str(e)}


@math_router.get("/twins_primes_sexy/{input_limit}")
async def calcular_primos_gemelos_primos_sexy(input_limit: str) -> Union[Dict[str, Relations], Dict[str, str]]:
    try:
        input_limit = InputMax(choice=input_limit)
        return {'result': await CalcularNumerosPrimos(input_limit).gemelo_primo_sexy_test()}
    except ValidationError as e:
        return {'error': str(e)}


@math_router.get("/numeros_enteros_a_romanos/{input_number}")
async def calculador_numeros_romanos(input_number) -> Dict[str, str]:
    try:
        input_number = InputRomano(choice_number=input_number)
        return {'result': await Romans(input_number=input_number).int_to_roman()}
    except ValidationError as e:
        return {'error': str(e)}


@math_router.get("/numeros_romanos_a_enteros/{input_number}")
async def calculador_enteros(input_number) -> Dict[str, Union[str, int]]:
    try:
        input_number = InputRomano(choice_roman=input_number)
        return {'result': await Romans(input_roman=input_number).roman_to_int()}
    except ValidationError as e:
        return {'error': str(e)}


@math_router.get("/es_par/{input_number}")
async def es_par(input_number) -> Dict[str, str]:
    try:
        input_limit = InputMax(choice=input_number)
        return {'result': await ParImpar(input_limit).is_even()}
    except ValidationError as e:
        return {'error': str(e)}


@math_router.get("/es_impar/{input_number}")
async def es_impar(input_number) -> Dict[str, str]:
    try:
        input_limit = InputMax(choice=input_number)
        return {'result': await ParImpar(input_limit).is_odd()}
    except ValidationError as e:
        return {'error': str(e)}


@math_router.get("/calc_paripe")
async def es_impar(primer_numero: str = Query(..., title="Primer sumando"),
                   segundo_numero: str = Query(..., title="Segundo sumando")) \
        -> Dict[str, Union[str, int]]:
    try:
        primer_sumando = InputMax(choice=primer_numero)
        segundo_sumando = InputMax(choice=segundo_numero)
        return {'result': await Calc(primer_sumando, segundo_sumando).hacer_el_paripe()}
    except ValidationError as e:
        return {'error': str(e)}


@math_router.get("/suma_estatistica")
async def suma_estatistica(limite_max: str = Query(..., title="Número límite deseado para la query")) \
    -> Dict[str, Union[str, Tuple[int, int]]]:
    try:
        limite_max = InputMax(choice=limite_max)
        return {'result': await calc_sum_and_count_all_numbers_div_by_2_or_7(limite_max)}
    except ValidationError as e:
        return {'error': str(e)}
