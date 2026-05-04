# Teacher API Automation Framework

A Pytest-based API automation framework for Teacher APIs, built following the same style and structure as the Student API project.

---

## Project Structure

```
teacher_api_framework/
│
├── utils/
│   ├── config.py            # Loads BASE_URL, USERNAME, PASSWORD from .env
│   └── helper_function.py   # All reusable functions (login, CRUD helpers)
│
├── testcases/
│   ├── conftest.py          # Shared fixtures (auth_headers, teacher_payload, schema)
│   ├── test_login.py        # Login tests (valid, invalid, empty credentials)
│   ├── test_post_teacher.py # Create teacher tests
│   ├── test_get_teacher.py  # Get teacher tests (all, by ID, by name)
│   ├── test_update_teacher.py # Update teacher tests
│   └── test_delete_teacher.py # Delete teacher tests
│
├── reports/                 # HTML reports generated here (auto-created)
├── .env                     # Your credentials — never commit this!
├── .env.example             # Template for .env
├── pytest.ini               # Pytest configuration
├── requirements.txt         # Python dependencies
└── README.md
```

---

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/teacher-api-automation.git
cd teacher-api-automation
```

### 2. Create and activate virtual environment
```bash
# macOS / Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment file
```bash
cp .env.example .env
```

Open `.env` and fill in your values:
```
BASE_URL=http://54.255.195.111:5171
API_USERNAME=your_email@example.com
API_PASSWORD=your_password
```

> ⚠️ Never commit `.env` to GitHub. It is listed in `.gitignore`.

---

## How to Run Tests

### Run all tests
```bash
pytest
```

### Run a specific test file
```bash
pytest testcases/test_post_teacher.py
```

### Run a specific test function
```bash
pytest testcases/test_delete_teacher.py::test_delete_teacher_by_id
```

### Run with detailed output
```bash
pytest -v
```

---

## Test Report

HTML report is auto-generated after every run:

```
reports/test_report.html
```

Open it in your browser:
```bash
# macOS
open reports/test_report.html

# Windows
start reports/test_report.html
```

---

## Test Coverage

| File | Tests | What is covered |
|------|-------|-----------------|
| `test_login.py` | 3 | Valid login, wrong password, empty credentials |
| `test_post_teacher.py` | 5 | Create valid, check in list, missing name, invalid email, no token |
| `test_get_teacher.py` | 5 | Get all + schema check, by ID, 404, by name, no token |
| `test_update_teacher.py` | 3 | Email update + list check, non-existent ID, no token |
| `test_delete_teacher.py` | 4 | Delete + verify gone, non-existent, double delete, no token |

**Total: 20 test cases**

---

## API Source

http://54.255.195.111:5171/api-docs/#/
