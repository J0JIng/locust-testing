# locust-testing

![image](https://github.com/user-attachments/assets/0dd8cefd-3b77-42a3-b0de-b3e5cfb1784b)


# Locust Testing with Flask-RESTX

## Overview
This project is a Flask-RESTX API with authentication, user management, and performance testing using Locust.  
It follows a **modular structure** for maintainability and scalability.

---
<details>
<summary>Project Structure</summary>
<br>

```
locust-testing/
│—— api/                  # API modules
│   ├—— v1/               # Version 1 of API
│   │   ├—— auth/         # Authentication-related routes
│   │   │   ├—— __init__.py
│   │   │   └—— login.py
│
│—— entity/               # Data entities/models
│   ├—— __init__.py
│   └—— user.py
│
│—— controllers/          # Controllers handle request parsing
│   ├—— __init__.py
│   └—— parser.py         # Defines request parsers
│
│—— services/             # Business logic layer
│   ├—— __init__.py
│   ├—— authService.py    # Handles authentication logic
│   └—— userService.py    # Handles user-related logic
│
│—— tests/                # Testing folder
│   ├—— performance/      # Performance tests (Locust)
│   └—— unit/             # Unit tests (Pytest)
│
│—— .gitignore            # Files to ignore in Git
│—— README.md             # Project documentation
│—— requirements.txt      # Python dependencies
│—— web.py                # Main Flask application
```

</details>

---

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/J0JIng/locust-testing.git
   cd locust-testing
   ```

2. **Set up a virtual environment (optional but recommended)**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Mac/Linux
   .venv\Scripts\activate     # On Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## Running the Flask App

1. **Start the Flask application**
   ```bash
   python web.py
   ```
2. **API Swagger UI** is available at:
   ```
   http://127.0.0.1:8080/swagger/
   ```

---

## Running Locust Performance Tests

1. **Start the Flask app** (if not already running)
   ```bash
   python web.py
   ```
2. **Run Locust**
   ```bash
   locust -f tests/performance/locustfile.py
   ```
3. Open **Locust Web UI**:
   ```
   http://127.0.0.1:8089
   ```
4. Enter the number of users and spawn rate, then start the test.

---

## Running Unit Tests

Run all unit tests with:
```bash
pytest tests/unit/
```
