# Teacher Management API Automation Framework

[![Python Version](https://img.shields.io/badge/Python-3.9%2B-1E90FF?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/Framework-Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)](https://docs.pytest.org/)
[![API Testing](https://img.shields.io/badge/API-Testing-FF6F00?style=for-the-badge&logo=fastapi&logoColor=white)](https://requests.readthedocs.io/)
[![Reporting](https://img.shields.io/badge/Allure-Report-E40046?style=for-the-badge&logo=testinglibrary&logoColor=white)](https://docs.qameta.io/allure/)
[![Automation Level](https://img.shields.io/badge/Test%20Automation-Advanced-2ECC71?style=for-the-badge)]()

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
## 📂 Project Structure

```text
teacher_api_framework/
│
├── .venv/                     # Virtual environment
│
├── teacher_api_framework/     # Main project package
│   ├── allure-results/        # Allure raw results (JSON)
│   ├── reports/               # HTML test reports output
│   │
│   ├── testcases/             # Test scripts
│   │   ├── __init__.py
│   │   ├── conftest.py        # Fixtures & global setup
│   │   ├── test_login.py
│   │   ├── test_post_teacher.py
│   │   ├── test_get_teacher.py
│   │   ├── test_update_teacher.py
│   │   └── test_delete_teacher.py
│   │
│   ├── utils/                # Helper & config layer
│   │   ├── __init__.py
│   │   ├── config.py         # Base URL & environment config
│   │   └── helper_function.py # Reusable API functions
│   │
│   ├── .env                  # Sensitive data (tokens, credentials)
│   ├── .gitignore            # Ignored files list
│   ├── pytest.ini            # Pytest configuration
│   └── requirements.txt      # Project dependencies
```
------

## How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/aburayhan01/teacher-api-automation-QA_Assignment_3-.git
cd teacher-api-automation-QA_Assignment_3-
```

### 2. Create and Activate Virtual Environment

Windows:
```bash
python -m venv .venv
.venv\Scripts\activate
```
macOS / Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment File

Create a `.env` file in the project root:
```
BASE_URL=http://54.255.195.111:5171
API_USERNAME=your_username
API_PASSWORD=your_password
```
> Note: Never commit `.env` to GitHub. It is listed in `.gitignore`.

### 5. Run All Tests
```bash
pytest -v -s
```

### 6. Run a Specific Test File
```bash
pytest testcases/test_post_teacher.py
```

### 7. Run a Specific Test Function
```bash
pytest testcases/test_delete_teacher.py::test_delete_teacher_by_id
```

## Generate & View HTML Report

The HTML report is auto-generated after every test run inside the `reports/` folder.

To generate:
```bash
pytest -v -s
```
To view on Windows:
```bash
start reports/test_report.html
```
To view on macOS:
```bash
open reports/test_report.html
```
<img width="1902" height="872" alt="Screenshot 2026-05-07 234449" src="https://github.com/user-attachments/assets/1a90daeb-e71f-47c9-bdfb-aa5e669fb052" />


---


## Generate & View Allure Report

The Allure report is generated after every test run and stored inside the `allure-results/` folder. The final report can be viewed using the Allure server.

### Generate Allure Results:
```bash
pytest -v -s --alluredir=allure-results
```
###View Allure Report:
```bash
allure serve allure-results
```
##  Allure Test Report Dashboard

### 📌 Executive Overview (Allure Summary)
This section provides a high-level snapshot of the overall test execution status, including pass/fail ratio, execution health, and stability insights.

<img width="1916" height="891" alt="Allure Overview" src="https://github.com/user-attachments/assets/e3e5fcc2-d05a-46c4-a76f-649d93bd5a44" />

---

###  Test Execution Trends & Graphical Analysis
Visual representation of test execution metrics including duration, status distribution, and performance trends across the test suite.

<img width="1919" height="1071" alt="Graphical Analysis" src="https://github.com/user-attachments/assets/26a30c39-ad84-40a4-af2b-0003f264b48e" />

---

###  Test Suite & Category Breakdown
Detailed breakdown of test cases organized by functional modules and test categories for better traceability and coverage analysis.

<img width="1120" height="1079" alt="image" src="https://github.com/user-attachments/assets/f1bf31ef-9c9e-4b09-9a6f-ea16bff46cfd" />


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
- After deletion GET by ID returns 404
- Delete non-existent teacher → Status 404
- Delete without token → Status 401/403

---

## Test Coverage Summary

| File | Tests | Result |
|------|-------|--------|
| test_login.py | 3 | ✅ Passed |
| test_post_teacher.py | 5 | ✅ Passed |
| test_get_teacher.py | 5 | ✅ Passed |
| test_update_teacher.py | 3 | ✅ Passed |
| test_delete_teacher.py | 3 | ✅ Passed |

**Total: 19 test cases — All Passed ✅**

---

## Author

Abu Rayhan
GitHub: https://github.com/aburayhan01
