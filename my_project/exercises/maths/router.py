from typing import Dict, Set, Tuple, Union

from fastapi import APIRouter, Query
from my_project.schemes.maths import InputMax, InputRomano, Relations, SetPrimeNumbers
from pydantic import ValidationError

from .numeros_a_texto import NumberText
from .numeros_perfectos_III import PerfectNumbers
from .numeros_primos import CalcularNumerosPrimos
from .numeros_romanos import Romans
from .par_impar_III import ParImpar
from .suma_basica import Calc
from .suma_estatistica_ii import calc_sum_and_count_all_numbers_div_by_2_or_7
from .utils.exceptions import LowLimitError, NotIntError

math_router = APIRouter(prefix="/math")


@math_router.get("/number_into_text/")
async def numeros_a_texto(
    input_number: int = Query(..., description="Número que quieres convertir en texto"),
) -> Dict[str, str]:
    try:
        return {"result": await NumberText(input_number).number_as_text()}
    except NotIntError:
        return {"error": f"{NotIntError().message}"}


@math_router.get("/calc_perfect_numbers/")
async def calcular_numeros_perfectos(
    input_limit: int = Query(..., description="Número para calcular todos los perfectos"),
) -> Dict[str, Union[Set[int], str]]:
    try:
        return {"result": await PerfectNumbers(InputMax(choice=input_limit)).calc_perfect_numbers()}
    except NotIntError:
        return {"error": NotIntError().message}
    except LowLimitError:
        return {"error": f"{LowLimitError(input_number=input_limit).message}"}


@math_router.get("/calc_prime_numbers/")
async def calcular_numeros_primos(
    input_limit: int = Query(..., description="Número límite al que iterar buscando números primos "),
) -> Union[Dict[str, SetPrimeNumbers], Dict[str, str]]:
    try:
        return {"result": await CalcularNumerosPrimos(input_limit).calcular_primos()}
    except ValidationError as e:
        return {"error": str(e)}


@math_router.get("/twins_primes_sexy/")
async def calcular_primos_gemelos_primos_sexy(
    input_limit: int = Query(..., description="Número límite al que llegar calculando números primos"),
) -> Union[Dict[str, Relations], Dict[str, str]]:
    try:
        return {"result": await CalcularNumerosPrimos(input_limit).gemelo_primo_sexy_test()}
    except ValidationError as e:
        return {"error": str(e)}


@math_router.get("/numeros_enteros_a_romanos/")
async def calculador_numeros_romanos(
    input_number: int = Query(..., description="Número arábico para convertir a romano"),
) -> Dict[str, str]:
    try:
        return {"result": await Romans(input_number=input_number).int_to_roman()}
    except ValidationError as e:
        return {"error": str(e)}


@math_router.get("/numeros_romanos_a_enteros/")
async def calculador_enteros(
    input_number: str = Query(..., description="Número Romano para convertir en número entero"),
) -> Dict[str, Union[str, int]]:
    try:
        input_number = InputRomano(choice_roman=input_number)
        return {"result": await Romans(input_roman=input_number).roman_to_int()}
    except ValidationError as e:
        print(f"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n {e.args}")
        return {"error": str(e)}


@math_router.get("/es_par/")
async def es_par(
    input_number: int = Query(..., description="Inserta número para saber si es par o no"),
) -> Dict[str, str]:
    try:
        input_limit = InputMax(choice=input_number)
        return {"result": await ParImpar(input_limit).is_even()}
    except ValidationError as e:
        return {"error": str(e)}


@math_router.get("/es_impar/")
async def es_impar(
    input_number: int = Query(..., description="Inserta número para saber si es impar o no"),
) -> Dict[str, str]:
    try:
        input_limit = InputMax(choice=input_number)
        return {"result": await ParImpar(input_limit).is_odd()}
    except ValidationError as e:
        return {"error": str(e)}


@math_router.get("/calc_paripe")
async def cal_paripe(
    primer_numero: int = Query(..., title="Primer sumando"),
    segundo_numero: int = Query(..., title="Segundo sumando"),
) -> Dict[str, Union[str, int]]:
    try:
        return {"result": await Calc(primer_numero, segundo_numero).hacer_el_paripe()}
    except ValidationError as e:
        return {"error": str(e)}


@math_router.get("/suma_estatistica")
async def suma_estatistica(
    limite_max: int = Query(..., title="Número límite deseado para la query"),
) -> Dict[str, Union[str, Tuple[int, int]]]:
    try:
        return {"result": await calc_sum_and_count_all_numbers_div_by_2_or_7(limite_max)}
    except ValidationError as e:
        return {"error": str(e)}
