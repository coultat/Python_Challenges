from fastapi.testclient import TestClient

from Python_Challenges.main import app


client = TestClient(app)


def test_sumatorio():
     # Given the input value, the expected result and the url
    input_value = 3
    expected_result = 6
    url = f"/recursion/count_digits/{input_value}"

    # When running the count digits function
    response = client.get(url)

    # Then the result must match with the expected value
    assert response.json()['result'] == expected_result


def test_calcular_minimo_multiplo():
    # Given the input values, the expected value and the url
    input_numero_a = '12'
    input_numero_b = '20'
    url = f"/recursion/minimo_comun_multiplo?primer_numero={input_numero_a}&segundo_numero={input_numero_b}"
    expected_result = 4

    # When calling the endpoint
    result = client.get(url)

    # Then the result must match
    assert result.json()['result'] == expected_result

def test_calcular_fibonacci():
    # Given the input, the expected result and the url
    input_value = '10'
    expected_result = 55
    url = f"/recursion/fibonacci/{input_value}"

    # When calling the endpoint
    result = client.get(url)

    # Then the result must match with the expectation
    assert result.json()['result'] == expected_result