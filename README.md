# Teacher API Automation Framework (Pytest)

## Project Overview

This project demonstrates API automation testing for a Teacher Management API using Pytest and Requests library.
The framework performs full CRUD operations (Create, Read, Update, Delete) and validates responses using proper assertions.
pytest-html is used to generate an HTML test report after every test execution.

---

## Tools & Technologies

- Python
- Pytest
- Requests
- python-dotenv
- Faker
- pytest-html
- GitHub

---

## Project Structure

<img width="374" height="730" alt="image" src="https://github.com/user-attachments/assets/f216e40c-b528-4762-93e6-0ae4f3df15e0" />


## How to Run the Project

### 1. Clone the Repository

git clone https://github.com/aburayhan01/teacher-api-automation-QA_Assignment_3-.git
cd teacher-api-automation-QA_Assignment_3-

### 2. Create and Activate Virtual Environment

Windows:
python -m venv .venv
.venv\Scripts\activate

macOS / Linux:
python3 -m venv .venv
source .venv/bin/activate

### 3. Install Dependencies

pip install -r requirements.txt

### 4. Set Up Environment File

Create a .env file in the project root:

BASE_URL=http://54.255.195.111:5171
API_USERNAME=your_username
API_PASSWORD=your_password

Note: Never commit .env to GitHub. It is listed in .gitignore.

### 5. Run All Tests

pytest -v -s

### 6. Run a Specific Test File

pytest testcases/test_post_teacher.py

### 7. Run a Specific Test Function

pytest testcases/test_delete_teacher.py::test_delete_teacher_by_id

---

## Generate & View HTML Report

The HTML report is auto-generated after every test run inside the reports/ folder.

To generate:
pytest -v -s

To view on Windows:
start reports/test_report.html

To view on macOS:
open reports/test_report.html

---

## Test Cases

### Authentication
- Login with valid credentials → Status 200, token returned
- Login with wrong password → Status 401, token not returned
- Login with empty credentials → Status 400/401

### Create Teacher (POST)
- Create teacher with all valid fields → Status 200/201, response matches request
- Created teacher exists in list → Email found in GET all response
- Create teacher with missing name → Status 400/422
- Create teacher with invalid email → Status 400/422
- Create without token → Status 401/403

### Get Teacher (GET)
- Get all teachers → Status 200, schema validated
- Get teacher by valid teacherId → Status 200, correct data returned
- Get teacher by non-existent ID → Status 404
- Get teacher by name filter → Status 200, matching teacher returned
- Get all without token → Status 401/403

### Update Teacher (PUT)
- Update teacher email → Status 200, new email in list, old email gone
- Update non-existent teacher → Status 400/404
- Update without token → Status 401/403

### Delete Teacher (DELETE)
- Delete existing teacher → Status 200/204
- After deletion GET by ID returns 404
- Delete non-existent teacher → Status 404
- Delete same teacher twice → Second attempt returns 404
- Delete without token → Status 401/403

---

## Test Coverage Summary

File                       Tests    Result
test_login.py                3      Passed
test_post_teacher.py         5      Passed
test_get_teacher.py          5      Passed
test_update_teacher.py       3      Passed
test_delete_teacher.py       4      Passed

Total: 20 test cases - All Passed

---

## Author

Abu Rayhan
GitHub: https://github.com/aburayhan01
