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


def test_calcular_fibonacci()
    # Given the input, the expected result and the url
    assert 2 == 1