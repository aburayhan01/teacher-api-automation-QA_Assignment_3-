import requests
from utils.config import BASE_URL
from utils.helper_function import create_teacher, get_all_teachers, delete_teacher


def test_create_teacher(auth_headers, teacher_payload):
    """Happy path — create teacher with all valid fields."""
    response = create_teacher(BASE_URL, teacher_payload, auth_headers)

    assert response.status_code in [200, 201], \
        f"Teacher creation failed. Response: {response.text}"

    response_data = response.json()
    print("Response Data:", response_data)

    assert response_data["name"] == teacher_payload["name"]
    assert response_data["email"] == teacher_payload["email"]
    assert response_data["department"] == teacher_payload["department"]
    assert response_data["teacherId"] == teacher_payload["teacherId"]
    assert response_data["designation"] == teacher_payload["designation"]

    # Cleanup
    teacher_id = response_data.get("_id")
    if teacher_id:
        delete_teacher(BASE_URL, teacher_id, auth_headers)


def test_created_teacher_exists_in_list(auth_headers, teacher_payload):
    """After creating a teacher, their email should appear in GET /api/teacher list."""
    post_response = create_teacher(BASE_URL, teacher_payload, auth_headers)

    assert post_response.status_code in [200, 201], \
        f"Teacher creation failed. Response: {post_response.text}"

    created_email = post_response.json()["email"]
    teacher_id = post_response.json().get("_id")

    get_response = get_all_teachers(BASE_URL, auth_headers)
    assert get_response.status_code == 200, \
        f"GET all teachers failed. Response: {get_response.text}"

    teachers = get_response.json()
    emails = [teacher["email"] for teacher in teachers]

    assert created_email in emails, \
        f"Created teacher email '{created_email}' not found in teacher list"

    print(f"Teacher with email {created_email} found in the list")

    # Cleanup
    if teacher_id:
        delete_teacher(BASE_URL, teacher_id, auth_headers)


def test_create_teacher_missing_name(auth_headers, teacher_payload):
    """Missing 'name' field should return a validation error."""
    teacher_payload.pop("name")

    response = create_teacher(BASE_URL, teacher_payload, auth_headers)

    assert response.status_code in [400, 422], \
        f"Expected validation error for missing name, got {response.status_code}"

    print("Missing name correctly rejected")


def test_create_teacher_invalid_email(auth_headers, teacher_payload):
    """Invalid email format should be rejected."""
    teacher_payload["email"] = "not-a-valid-email@@bad"

    response = create_teacher(BASE_URL, teacher_payload, auth_headers)

    assert response.status_code in [400, 422], \
        f"Expected validation error for invalid email, got {response.status_code}"

    print("Invalid email correctly rejected")


def test_create_teacher_without_token(teacher_payload):
    """Request without Authorization header must be rejected."""
    response = requests.post(
        url=f"{BASE_URL}/api/teacher",
        json=teacher_payload
    )

    assert response.status_code in [401, 403], \
        f"Expected 401/403 without token, got {response.status_code}"

    print("Unauthenticated request correctly rejected")