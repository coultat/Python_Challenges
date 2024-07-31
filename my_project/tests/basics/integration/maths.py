from fastapi.testclient import TestClient

from Python_Challenges.main import app


client = TestClient(app)

def test_numeros_a_texto():
    # Given the input_value, the expected result and the url
    input_value = 6
    expected_result = 'SEIS'
    url = f"/math/number_into_text/{input_value}"

    # When calling the endpoint
    response = client.get(url)

    # Then the result must match
    assert response.json()['result'] == expected_result


def test_calcular_numeros_perfectos():
    # Given the input_value, the expected result and the url
    input_limit = 37
    expected_result = [28, 6]
    url = f"/math/calc_perfect_numbers/{input_limit}"

    # When calling the endpoint
    response = client.get(url)

    # Then the result must match
    assert response.json()['result'] == expected_result


def test_calcular_numeros_primos():
    # Given the input_value, the expected result and the url
    input_limit = 30
    expected_result = {'set_prime_numbers': [{'number': 1},
                       {'number': 2},
                       {'number': 3},
                       {'number': 5},
                       {'number': 7},
                       {'number': 11},
                       {'number': 13},
                       {'number': 17},
                       {'number': 19},
                       {'number': 23},
                       {'number': 29}]}
    url = f"/math/calc_prime_numbers/{input_limit}"

    # When calling the endpoint
    response = client.get(url)

    # Then the result must match
    assert response.json()['result'] == expected_result


def test_calcular_primos_gemelos_primos_sexy():
    # Given the input_value, the expected result and the url
    input_limit = 30
    expected_result = {'gemelos': [{'parejas': [{'number': 1}, {'number': 3}]},
             {'parejas': [{'number': 3}, {'number': 5}]},
             {'parejas': [{'number': 5}, {'number': 7}]},
             {'parejas': [{'number': 11}, {'number': 13}]},
             {'parejas': [{'number': 17}, {'number': 19}]}],
 'primos': [{'parejas': [{'number': 1}, {'number': 5}]},
            {'parejas': [{'number': 3}, {'number': 7}]},
            {'parejas': [{'number': 7}, {'number': 11}]},
            {'parejas': [{'number': 13}, {'number': 17}]},
            {'parejas': [{'number': 19}, {'number': 23}]}],
 'sexy': [{'parejas': [{'number': 1}, {'number': 7}]},
          {'parejas': [{'number': 5}, {'number': 11}]},
          {'parejas': [{'number': 7}, {'number': 13}]},
          {'parejas': [{'number': 11}, {'number': 17}]},
          {'parejas': [{'number': 13}, {'number': 19}]},
          {'parejas': [{'number': 17}, {'number': 23}]},
          {'parejas': [{'number': 23}, {'number': 29}]}]}
    url = f"/math/twins_primes_sexy/{input_limit}"

    # When calling the endpoint
    response = client.get(url)

    # Then the result must match
    assert response.json()['result'] == expected_result


def test_calculador_numeros_romanos():
    # Given the input_value, the expected result and the url
    input_number = 37
    expected_result = 'XXXVII'
    url = f"/math/numeros_enteros_a_romanos/{input_number}"

    # When calling the endpoint
    response = client.get(url)

    # Then the result must match
    assert response.json()['result'] == expected_result


def test_calculador_numeros_romanos_a_enteros():
    # Given the input_value, the expected result and the url
    input_number = 'XXXVII'
    expected_result = 37
    url = f"/math/numeros_romanos_a_enteros/{input_number}"

    # When calling the endpoint
    response = client.get(url)

    # Then the result must match
    assert response.json()['result'] == expected_result


def test_es_par():
    # Given the input_value, the expected result and the url
    input_number = 37
    expected_result = 'is not even'
    url = f"/math/es_par/{input_number}"

    # When calling the endpoint
    response = client.get(url)

    # Then the result must match
    assert response.json()['result'] == expected_result


def test_es_par_right():
    # Given the input_value, the expected result and the url
    input_number = 38
    expected_result = 'is even'
    url = f"/math/es_par/{input_number}"

    # When calling the endpoint
    response = client.get(url)

    # Then the result must match
    assert response.json()['result'] == expected_result


def test_es_impar_right():
    # Given the input_value, the expected result and the url
    input_number = 37
    expected_result = 'is odd'
    url = f"/math/es_impar/{input_number}"

    # When calling the endpoint
    response = client.get(url)

    # Then the result must match
    assert response.json()['result'] == expected_result


def test_es_impar_wrong():
    # Given the input_value, the expected result and the url
    input_number = 38
    expected_result = 'is even'
    url = f"/math/es_impar/{input_number}"

    # When calling the endpoint
    response = client.get(url)

    # Then the result must match
    assert response.json()['result'] == expected_result


def test_suma_estatistica():
    # Given the input_value, the expected result and the url
    input_number = 38
    expected_result = [21, 405]
    url = f"/math/suma_estatistica?limite_max={input_number}"

    # When calling the endpoint
    response = client.get(url)

    # Then the result must match
    assert response.json()['result'] == expected_result
