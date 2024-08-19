from random import randint

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_sumatorio():
    # Given the input value, the expected result and the url
    input_value = 3
    expected_result = 6
    url = f"/recursion/count_digits/{input_value}"

    # When running the count digits function
    response = client.get(url)

    # Then the result must match with the expected value
    assert response.json()["result"] == expected_result


def test_calcular_minimo_multiplo():
    # Given the input values, the expected value and the url
    input_numero_a = "12"
    input_numero_b = "20"
    url = f"/recursion/minimo_comun_multiplo?primer_numero={input_numero_a}&segundo_numero={input_numero_b}"
    expected_result = 4

    # When calling the endpoint
    result = client.get(url)

    # Then the result must match
    assert result.json()["result"] == expected_result


def test_calcular_fibonacci():
    # Given the input, the expected result and the url
    input_value = "10"
    expected_result = 55
    url = f"/recursion/fibonacci/?input_max={input_value}"

    # When calling the endpoint
    result = client.get(url)

    # Then the result must match with the expectation
    assert result.json()["result"] == expected_result


def test_calcular_reversed_string():
    # Given the input value, the expected result and the endpoint
    input_value = "No contaban con mi astucia"
    expected_result = "aicutsa im noc nabatnoc oN"
    endpoint = f"/recursion/reversed_string?palindrome={input_value}"

    # When getting the information throught the endpoint
    result = client.get(endpoint)

    # Then the result must match
    assert result.json()["result"] == expected_result


def test_binary_calc():
    # Given the input_value, the expected_result and the endpoint
    input_value = 10
    expected_result = "1010"
    endpoint = f"/recursion/calculadora_binaria?valor={input_value}"

    # When calling the endpoint
    result = client.get(endpoint)

    # Then the result must match
    assert result.json()["result"] == expected_result


def test_summa_array():
    # Given the input_value, the expected_result and the endpoint
    input_value = list(range(101))
    expected_result = 5050
    extension = "&".join(f"valor_lista={value}" for value in input_value[1:])
    endpoint = f"/recursion/suma_array?valor_lista={input_value[0]}&" + extension

    # When calling the endpoint
    result = client.get(endpoint)

    # Then the result must match
    assert result.json()["result"] == expected_result


def test_array_min():
    # Given the input_value, the expected_result and the endpoint
    input_value = [randint(-500, 500) for _ in range(5)]
    expected_result = min(input_value)
    extension_endpoint = "&".join(f"valor_lista={value}" for value in input_value[1:])
    endpoint = f"/recursion/array_min?valor_lista={input_value[0]}&" + extension_endpoint
    print(endpoint)
    # When calling the endpoint
    result = client.get(url=endpoint)

    # Then the result must match
    print(result.text)
    assert result.json()["result"] == expected_result


def test_wrong_endpoint():
    # Given the wrong endpoint
    endpoint = "/esto/se/va/a/descontrolar"
    expected_status_code_result = 404
    expected_result = {"detail": "Not Found"}

    # When calling the endpoint
    result = client.get(endpoint)

    # Then the exception must be raised
    assert result.json() == expected_result
    assert result.status_code == expected_status_code_result
