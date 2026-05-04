import pytest
from faker import Faker
from utils.config import BASE_URL, USERNAME, PASSWORD
from utils.helper_function import get_token, get_headers

fake = Faker()


@pytest.fixture
def login_data():
    return {
        "username": USERNAME,
        "password": PASSWORD
    }


@pytest.fixture
def auth_headers(login_data):
    token = get_token(BASE_URL, login_data["username"], login_data["password"])
    return get_headers(token)


@pytest.fixture
def teacher_payload():
    return {
        "name": fake.name(),
        "email": fake.unique.email(),
        "department": "CSE",
        "teacherId": fake.random_int(min=1000, max=9999),
        "designation": "Lecturer"
    }


@pytest.fixture
def teacher_schema():
    return {
        "_id": str,
        "name": str,
        "email": str,
        "department": str,
        "teacherId": int,
        "designation": str
    }