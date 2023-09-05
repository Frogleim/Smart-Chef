from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_check_status_code():
    # Send a GET request to the /get_recipes/ endpoint with ingredients
    ingredients = "tomatoes,pasta,cheese"  # Adjust as needed
    response = client.get(f"/get_recipes/{ingredients}")

    # Check if the response status code is 200 (OK)
    assert response.status_code == 200

    # Check if the response contains the expected keys and values
    data = response.json()
    assert "Message" in data
    assert "Data" in data
    assert data["Message"] == "Success"

    # You might want to further validate the 'Data' content based on your application's logic
    # For example, check if 'Data' is a list of recommended recipes


def test_output():
    ingredients = "tomatoes,pasta,cheese"  # Adjust as needed
    response = client.get(f"/get_recipes/{ingredients}")

    data = response.json()
    assert data['Message'] == "Success"


