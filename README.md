# Python – Django Learning & Practice Repository

A hands-on collection of Django projects and exercises used to learn and practice Python backend development with Django and Django REST Framework (DRF).

## Repository Structure

```
Python/
├── django/                          # Core Django practice projects
│   ├── 01Django/                    # Introductory Django project
│   ├── 01Practice_Django/           # Django practice with home app
│   └── 02Django/                    # Further Django exploration
└── March_practice_folder_backend/   # Full-stack projects (March cohort)
    ├── 01_django_start/             # Stock Prediction App
    │   ├── backend-drf/             # Django REST Framework backend
    │   │   ├── accounts/            # User authentication & management
    │   │   └── api/                 # REST API endpoints
    │   └── frontend-react/          # React + Vite frontend
    └── 02_django_start/             # Additional Django backend project
```

## Projects

### 1. Stock Prediction App (`March_practice_folder_backend/01_django_start`)
A full-stack web application combining a **Django REST Framework** backend with a **React + Vite** frontend.
- **Backend**: Handles user accounts, authentication, and exposes REST API endpoints.
- **Frontend**: Built with React and Vite for a fast development experience.

### 2. Django Practice Projects (`django/`)
Standalone Django projects covering core concepts such as:
- Project setup and configuration
- URL routing and views
- Models and the Django ORM
- Template rendering

## Technologies Used

- **Python** – Primary programming language
- **Django** – Web framework
- **Django REST Framework (DRF)** – Toolkit for building REST APIs
- **React + Vite** – Frontend JavaScript library and build tool
- **SQLite** – Default development database

## Getting Started

### Backend (Django / DRF)

```bash
# Create and activate a virtual environment
python -m venv env
source env/bin/activate   # Windows: env\Scripts\activate

# Install dependencies
pip install django djangorestframework python-decouple

# Apply migrations and run the development server
python manage.py migrate
python manage.py runserver
```

### Frontend (React + Vite)

```bash
cd March_practice_folder_backend/01_django_start/frontend-react

npm install
npm run dev
```

## Purpose

This repository serves as a personal learning journal and practice ground for Python web development, covering REST API design, full-stack integration, and Django best practices.
