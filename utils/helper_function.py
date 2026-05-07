import requests
import pytest


def get_token(base_url, username, password):
    login_payload = {
        "username": username,
        "password": password
    }
    response = requests.post(url=f"{base_url}/login", json=login_payload)
    token = response.json().get("authToken")
    return token


def get_headers(token):
    return {
        "Authorization": f"Bearer {token}"
    }


def create_teacher(base_url, payload, headers):
    response = requests.post(
        url=f"{base_url}/api/teacher",
        json=payload,
        headers=headers
    )
    return response


def get_all_teachers(base_url, headers):
    response = requests.get(
        url=f"{base_url}/api/teacher",
        headers=headers
    )
    return response


def get_teacher_by_id(base_url, teacher_id, headers):
    response = requests.get(
        url=f"{base_url}/api/teacher/{teacher_id}",
        headers=headers
    )
    return response


def update_teacher(base_url, teacher_id, payload, headers):
    response = requests.put(
        url=f"{base_url}/api/teacher/{teacher_id}",
        json=payload,
        headers=headers
    )
    return response


def delete_teacher(base_url, teacher_id, headers):
    response = requests.delete(
        url=f"{base_url}/api/teacher/{teacher_id}",
        headers=headers
    )
    return response