# 🚀 FastAPI Task Manager

A simple task management API built with FastAPI — includes authentication, file upload per task, CI/CD with GitHub Actions, and Docker support.

---

## 🧩 Features

### 📝 Task Management
- Create / update / delete tasks
- Filter tasks by status, priority
- Search tasks by keyword

### 📎 File Upload
- Attach files to each task
- File validation (type, size)
- (Planned) Upload to cloud storage (e.g., Imgur)

### 🔐 Authentication
- API key-based authentication
- Middleware protection for all task routes

---

## ⚙️ Project Tooling

This project is equipped with full tooling for professional development and deployment:

- ✅ **FastAPI** – modern, async-first Python web framework
- ✅ **Pytest** – automated unit testing
- ✅ **Flake8** – linting and style check (PEP8)
- ✅ **Docker** – build and run app in containers
- ✅ **GitHub Actions** – CI pipeline for every push/PR

---

## 🔄 GitHub Actions CI/CD

Configured in `.github/workflows/ci.yml`, this pipeline runs:

- ✅ `flake8 .` – Check style and unused imports
- ✅ `pytest` – Run unit tests
- ✅ `docker build` – Ensure Dockerfile builds successfully

The CI triggers on:
- `push` to any branch
- `pull_request` to main

> Helps prevent regressions, enforce style, and ensure build stability.

---

## 📦 Installation & Usage

### 🧪 Local Development

```bash
git clone https://github.com/yourname/fastapi-task-manager.git
cd fastapi-task-manager

# Install dependencies
pip install -r requirements.txt

# Run the app
uvicorn manage:app --reload
🧪 Run Linting & Tests
bash
Copy
Edit
# Style check
flake8 .

# Run all tests
PYTHONPATH=. pytest
```

### 🐳 Docker Support
Build and run the app in Docker:

```bash
docker build -t training-fastapi .
docker run -p 8000:8000 training-fastapi
```

### 🧠 Tips
manage.py is the entry point (from manage import app)

Make sure to set PYTHONPATH=. when testing locally

You can extend the CI workflow with:

Coverage checks using pytest-cov

Deployment steps using secrets or DockerHub

### 📜 License
MIT — free to use, modify, and share.

---