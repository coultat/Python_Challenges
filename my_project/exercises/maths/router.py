import asyncio

from schemes.maths import InputMax, Relations, SetPrimeNumbers
from .numeros_a_texto import number_as_text
from .numeros_perfectos_III import calc_perfect_numbers
from .numeros_primos import CalcularNumerosPrimos
from fastapi import APIRouter
from typing import Dict, Set, Union, Tuple

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
    except NotIntError:
        return {'error': NotIntError().message}
    except LowLimitError:
        return {'error': f'{LowLimitError(input_number=input_limit).message}'}


@math_router.get("/twins_primes_sexy/{input_limit}")
async def calcular_primos_gemelos_primos_sexy(input_limit: str) -> Union[Dict[str, Relations], Dict[str, str]]:
    try:
        return {'result': await CalcularNumerosPrimos(InputMax(choice=input_limit)).gemelo_primo_sexy_test()}
    except NotIntError:
        return {'error': NotIntError().message}
    except LowLimitError:
        return {'error': f'{LowLimitError(input_number=input_limit).message}'}
