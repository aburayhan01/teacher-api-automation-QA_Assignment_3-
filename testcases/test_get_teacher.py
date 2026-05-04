import requests
from utils.config import BASE_URL
from utils.helper_function import create_teacher, get_all_teachers, get_teacher_by_id, delete_teacher


def test_get_all_teachers_status_and_schema(auth_headers, teacher_schema):
    """GET /api/teacher should return 200 and each teacher must match the schema."""
    response = get_all_teachers(BASE_URL, auth_headers)

    assert response.status_code == 200, \
        f"GET all teachers failed. Response: {response.text}"

    teachers = response.json()
    assert isinstance(teachers, list), "Response should be a list"

    for teacher in teachers:
        for key, expected_type in teacher_schema.items():
            assert key in teacher, f"Key '{key}' missing in teacher object"
            assert type(teacher[key]) == expected_type, \
                f"Key '{key}' expected type {expected_type}, got {type(teacher[key])}"

    print(f"Total teachers found: {len(teachers)}")


def test_get_teacher_by_valid_id(auth_headers, teacher_payload):
    """GET /api/teacher/{teacherId} should return the correct teacher."""
    post_response = create_teacher(BASE_URL, teacher_payload, auth_headers)
    assert post_response.status_code in [200, 201], \
        f"Teacher creation failed. Response: {post_response.text}"

    teacher_id = post_response.json()["teacherId"]  # numeric teacherId
    mongo_id = post_response.json()["_id"]

    get_response = get_teacher_by_id(BASE_URL, teacher_id, auth_headers)

    assert get_response.status_code == 200, \
        f"GET teacher by ID failed. Response: {get_response.text}"

    teacher = get_response.json()
    assert teacher["teacherId"] == teacher_id
    assert teacher["name"] == teacher_payload["name"]
    assert teacher["email"] == teacher_payload["email"]

    print(f"Teacher with teacherId {teacher_id} retrieved successfully")

    # Cleanup
    delete_teacher(BASE_URL, teacher_id, auth_headers)


def test_get_teacher_by_nonexistent_id(auth_headers):
    """GET /api/teacher/{teacherId} with a fake ID should return 404."""
    fake_id = 999999999

    response = get_teacher_by_id(BASE_URL, fake_id, auth_headers)

    assert response.status_code == 404, \
        f"Expected 404 for non-existent ID, got {response.status_code}"

    print("Non-existent ID correctly returned 404")


def test_get_teacher_by_name(auth_headers, teacher_payload):
    """GET /api/teacher?name=<name> should return the matching teacher."""
    post_response = create_teacher(BASE_URL, teacher_payload, auth_headers)
    assert post_response.status_code in [200, 201], \
        f"Teacher creation failed. Response: {post_response.text}"

    teacher_id = post_response.json()["teacherId"]
    name_to_search = teacher_payload["name"]

    response = requests.get(
        url=f"{BASE_URL}/api/teacher?name={name_to_search}",
        headers=auth_headers
    )

    assert response.status_code == 200, f"GET by name failed"

    data = response.json()
    assert len(data) > 0, "No teacher returned for given name"

    for teacher in data:
        assert teacher["name"] == name_to_search, \
            f"Expected name '{name_to_search}', got '{teacher['name']}'"

    print(f"Teacher with name '{name_to_search}' found successfully")

    # Cleanup
    delete_teacher(BASE_URL, teacher_id, auth_headers)


def test_get_all_teachers_without_token():
    """GET /api/teacher without token should be rejected."""
    response = requests.get(url=f"{BASE_URL}/api/teacher")

    assert response.status_code in [401, 403], \
        f"Expected 401/403 without token, got {response.status_code}"

    print("Unauthenticated GET correctly rejected")