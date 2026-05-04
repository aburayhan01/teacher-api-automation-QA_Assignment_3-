import requests
from utils.config import BASE_URL
from utils.helper_function import create_teacher, get_all_teachers, update_teacher, delete_teacher


def test_update_teacher_email_reflects_in_list(auth_headers, teacher_payload):
    """After updating email, old email should be gone and new email should appear in list."""
    # Step 1: Create teacher
    post_response = create_teacher(BASE_URL, teacher_payload, auth_headers)
    assert post_response.status_code in [200, 201], \
        f"Teacher creation failed. Response: {post_response.text}"

    created_teacher = post_response.json()
    teacher_id = created_teacher["teacherId"]
    old_email = created_teacher["email"]

    # Step 2: Verify old email exists in list
    get_response = get_all_teachers(BASE_URL, auth_headers)
    teachers_before = get_response.json()
    emails_before = [teacher["email"] for teacher in teachers_before]

    assert old_email in emails_before, \
        f"Old email '{old_email}' not found before update"

    # Step 3: Update the teacher
    updated_email = "updated_" + old_email
    updated_payload = {
        "name": teacher_payload["name"] + " Updated",
        "email": updated_email,
        "department": "BBA",
        "designation": "Assistant Professor"
    }

    update_response = update_teacher(BASE_URL, teacher_id, updated_payload, auth_headers)
    assert update_response.status_code in [200, 201], \
        f"Update failed. Response: {update_response.text}"

    # Step 4: Verify new email in list, old email gone
    get_response_after = get_all_teachers(BASE_URL, auth_headers)
    teachers_after = get_response_after.json()
    emails_after = [teacher["email"] for teacher in teachers_after]

    assert old_email not in emails_after, \
        f"Old email '{old_email}' still exists after update"

    assert updated_email in emails_after, \
        f"Updated email '{updated_email}' not found in teacher list"

    print(f"Email updated from '{old_email}' to '{updated_email}'")

    # Cleanup
    delete_teacher(BASE_URL, teacher_id, auth_headers)


def test_update_nonexistent_teacher_returns_error(auth_headers):
    """PUT with a non-existent ID should return 404."""
    fake_id = "000000000000000000000000"

    updated_payload = {
        "name": "Ghost Teacher",
        "email": "ghost@test.com",
        "department": "CSE",
        "teacherId": 9999,
        "designation": "Lecturer"
    }

    response = update_teacher(BASE_URL, fake_id, updated_payload, auth_headers)

    assert response.status_code in [400, 404], \
        f"Expected 400/404 for non-existent ID, got {response.status_code}"

    print("Non-existent ID update correctly returned error")


def test_update_teacher_without_token(auth_headers, teacher_payload):
    """PUT without Authorization header must be rejected."""
    post_response = create_teacher(BASE_URL, teacher_payload, auth_headers)
    assert post_response.status_code in [200, 201]

    teacher_id = post_response.json()["_id"]

    response = requests.put(
        url=f"{BASE_URL}/api/teacher/{teacher_id}",
        json=teacher_payload
    )

    assert response.status_code in [401, 403], \
        f"Expected 401/403 without token, got {response.status_code}"

    print("Unauthenticated update correctly rejected")

    # Cleanup
    delete_teacher(BASE_URL, teacher_id, auth_headers)