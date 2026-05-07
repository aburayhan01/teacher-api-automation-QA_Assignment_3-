import requests
from utils.config import BASE_URL
from utils.helper_function import create_teacher, get_teacher_by_id, delete_teacher


def test_delete_teacher_by_id(auth_headers, teacher_payload):

    # Step 1: Create a teacher
    post_response = create_teacher(BASE_URL, teacher_payload, auth_headers)
    assert post_response.status_code in [200, 201], \
        f"Teacher creation failed. Response: {post_response.text}"

    teacher_id = post_response.json()["teacherId"]  # numeric teacherId
    print(f"Created teacher with teacherId: {teacher_id}")

    # Step 2: Delete the teacher
    delete_response = delete_teacher(BASE_URL, teacher_id, auth_headers)
    assert delete_response.status_code in [200, 204], \
        f"Delete failed. Response: {delete_response.text}"

    print(f"Teacher with teacherId {teacher_id} deleted")

    # Step 3: Verify teacher no longer exists
    get_response = get_teacher_by_id(BASE_URL, teacher_id, auth_headers)
    assert get_response.status_code in [400, 404], \
        f"Deleted teacher still exists! Status: {get_response.status_code}"

    print(f"Verified: teacher {teacher_id} no longer exists")


def test_delete_nonexistent_teacher(auth_headers):

    fake_id = 999999999

    response = delete_teacher(BASE_URL, fake_id, auth_headers)

    assert response.status_code == 404, \
        f"Expected 404 for non-existent ID, got {response.status_code}"

    print("Non-existent teacher delete correctly returned 404")


def test_delete_teacher_without_token(auth_headers, teacher_payload):

    post_response = create_teacher(BASE_URL, teacher_payload, auth_headers)
    assert post_response.status_code in [200, 201]

    teacher_id = post_response.json()["teacherId"]  # numeric teacherId

    response = requests.delete(url=f"{BASE_URL}/api/teacher/{teacher_id}")

    assert response.status_code in [401, 403], \
        f"Expected 401/403 without token, got {response.status_code}"

    print("Unauthenticated delete correctly rejected")


    delete_teacher(BASE_URL, teacher_id, auth_headers)