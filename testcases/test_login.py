import requests
from utils.config import BASE_URL


def test_valid_login_returns_token(login_data):
    """Valid credentials should return a 200 and a token."""
    response = requests.post(url=f"{BASE_URL}/login", json=login_data)

    # Status code check
    assert response.status_code == 200, f"Login Failed. Response: {response.text}"

    # Token validation
    token = response.json().get("authToken")
    assert token is not None, "Auth token not found in response"
    assert len(token) > 10, "Token looks too short to be valid"

    print(f"Token received: {token[:20]}...")


def test_invalid_password_is_rejected():
    """Wrong password must not return a token."""
    payload = {
        "username": "admin@example.com",
        "password": "WRONG_PASSWORD_123"
    }
    response = requests.post(url=f"{BASE_URL}/login", json=payload)

    assert response.status_code in [400, 401, 403], \
        f"Expected 401 for wrong password, got {response.status_code}"

    token = response.json().get("authToken")
    assert token is None, "Token should NOT be returned for wrong password"

    print("Invalid password correctly rejected")


def test_empty_credentials_are_rejected():
    """Empty username and password must not authenticate."""
    payload = {
        "username": "",
        "password": ""
    }
    response = requests.post(url=f"{BASE_URL}/login", json=payload)

    assert response.status_code in [400, 401, 422], \
        f"Expected error for empty credentials, got {response.status_code}"

    print("Empty credentials correctly rejected")
