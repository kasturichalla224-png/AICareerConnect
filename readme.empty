# AI Career Connect — Full Project Documentation

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![Flask Version](https://img.shields.io/badge/flask-3.1.1-green.svg)](https://flask.palletsprojects.org/)
[![Mistral AI](https://img.shields.io/badge/AI-Mistral_1.6.0-orange.svg)](https://mistral.ai/)
[![License](https://img.shields.io/badge/license-MIT-purple.svg)]()

---

## 📌 Project Overview

**AI Career Connect** is a modern, full-stack, AI-powered career counseling platform built with **Flask** and powered by **Mistral AI**. The platform delivers personalized career guidance, skill gap analysis, speech interaction capabilities (Speech-to-Text and Text-to-Speech), user session histories, and a dynamic real-time analytics dashboard powered by Chart.js.

Designed following senior software engineering best practices, the application utilizes the **Application Factory pattern**, **Blueprint-based modular routing**, a **decoupled Service Layer**, and a clean **Dark-Mode Glassmorphism Design System**.

---

## ✨ Key Features

1. **AI Career Counseling**
   - Interactive chat interface powered by **Mistral AI** (`mistral-large-latest`).
   - Context-aware prompts tailored for personalized career roadmap generation, skill assessment, and industry advice.
   - Best-effort JSON extraction for key metadata (e.g., target career fields, confidence scores).

2. **Voice & Speech Integration**
   - **Speech-to-Text (STT):** Browser-native Web Speech API on the client side, plus server-side audio file transcription using `SpeechRecognition`.
   - **Text-to-Speech (TTS):** Audio synthesis powered by `gTTS` (Google Text-to-Speech) and `pyttsx3` for listening to AI career advice.

3. **Analytics & Metrics Dashboard**
   - Real-time visualizations powered by **Chart.js**.
   - Doughnut chart displaying career field breakdowns and distributions.
   - Bar chart showing user interactions, speech logs, and platform metrics.
   - Backend JSON API endpoints (`/dashboard/api/stats`, `/dashboard/api/metrics`).

4. **Session Management & History**
   - Complete tracking of user Q&A interactions stored in SQLite via **SQLAlchemy**.
   - Historical view (`/career/history`) allowing users to review past counseling sessions.

5. **User Authentication & Security**
   - User registration, login, and session persistence managed by **Flask-Login**.
   - Password hashing utilizing **Werkzeug** security utilities.
   - Protected routes guarded with `@login_required`.

6. **Modern Dark-Mode UI/UX**
   - Custom CSS Design System using CSS Custom Properties (Tokens).
   - Glassmorphism navbar, gradient hero elements, smooth chat bubbles, and responsive layouts.

---

## 🛠️ Technology Stack

| Layer | Technology / Library | Description |
|---|---|---|
| **Core Framework** | Flask `3.1.1` | WSGI web application framework |
| **Database & ORM** | SQLAlchemy `2.0.36`, Flask-SQLAlchemy `3.1.1` | Object-Relational Mapping & DB management |
| **Migrations** | Flask-Migrate `4.1.0` | Alembic-powered database schema migrations |
| **Authentication** | Flask-Login `0.6.3`, Werkzeug `3.1.3` | User session management & password hashing |
| **Form & CORS** | Flask-WTF `1.2.2`, Flask-CORS `5.0.1` | Form validation & Cross-Origin Resource Sharing |
| **AI Integration** | Mistral AI SDK `1.6.0` | Conversational intelligence & career advice |
| **Speech Processing**| SpeechRecognition `3.14.1`, gTTS `2.5.4`, pyttsx3 `2.98` | Audio transcription & text-to-speech synthesis |
| **Frontend** | HTML5, CSS3, Vanilla JS (ES6+), Chart.js | Modern UI with responsive grid & interactive charts |
| **Environment** | python-dotenv `1.1.0` | Environment variable management |
| **Testing** | pytest | Automated test framework |

---

## 📁 Directory Structure & Explanation

```
AICareerConnect/
│
├── run.py                        ← Application entry point (boots dev server / WSGI)
├── config.py                     ← Centralized configuration (Dev/Test/Prod classes)
├── requirements.txt              ← Pinned Python dependencies
├── .env.example                  ← Environment variable template (git-safe)
├── .gitignore                    ← Files and folders excluded from Git control
├── readme.empty                  ← Complete project documentation file
│
├── app/                          ← Main Application Package
│   ├── __init__.py               ← Application Factory (create_app)
│   ├── models.py                 ← SQLAlchemy Database Models (User, CareerSession, etc.)
│   │
│   ├── routes/                   ← Blueprint Route Handlers
│   │   ├── __init__.py
│   │   ├── main.py               ← Public routes (Landing Page, About)
│   │   ├── auth.py               ← User authentication (Register, Login, Logout)
│   │   ├── career.py             ← Career chat & session history routes
│   │   ├── dashboard.py          ← Analytics dashboard & JSON stats API
│   │   └── speech.py             ← Speech-to-Text & Text-to-Speech endpoints
│   │
│   ├── services/                 ← Business Logic Layer
│   │   ├── __init__.py
│   │   ├── mistral_service.py    ← Mistral AI API interaction & metadata parser
│   │   └── speech_service.py     ← Speech transcription & audio synthesis engines
│   │
│   ├── utils/                    ← Cross-Cutting Utilities
│   │   ├── __init__.py
│   │   ├── helpers.py            ← Reusable helper functions (date format, text truncate)
│   │   └── error_handlers.py     ← Centralized 404 & 500 error handlers (HTML/JSON)
│   │
│   ├── templates/                ← Jinja2 HTML Templates
│   │   ├── base.html             ← Master layout (navbar, flash alerts, footer, scripts)
│   │   ├── index.html            ← Landing hero page
│   │   ├── auth/                 ← login.html, register.html
│   │   ├── career/               ← chat.html, history.html
│   │   ├── dashboard/            ← overview.html (stat cards & charts)
│   │   └── errors/               ← 404.html, 500.html
│   │
│   └── static/                   ← Static Assets
│       ├── css/
│       │   └── style.css         ← Complete CSS dark-mode glassmorphism design system
│       └── js/
│           ├── app.js            ← Shared app JS (flash message dismissals)
│           ├── chat.js           ← Career chat logic & Web Speech API integration
│           └── dashboard.js      ← Chart.js initialization & dynamic API fetch logic
│
├── tests/                        ← Automated Test Suite
│   ├── __init__.py
│   ├── conftest.py               ← Pytest fixtures & in-memory test app setup
│   └── test_routes.py            ← Smoke tests verifying core route status codes
│
├── instance/                     ← Auto-created runtime SQLite database (`aicareer.db`)
├── uploads/                      ← Auto-created file upload storage
└── temp_audio/                   ← Auto-created temporary audio files for TTS/STT
```

---

## 📐 Architecture & Design Principles

1. **Application Factory (`create_app`)**
   - Prevents circular imports and avoids global state.
   - Enables instantiation of isolated app instances per unit test with in-memory databases.

2. **Blueprint-Based Modular Routing**
   - Splits application features into logical sub-modules (`main`, `auth`, `career`, `dashboard`, `speech`).
   - Maintains clean separation of concerns and distinct URL prefixes.

3. **Separation of Business Logic (Service Layer)**
   - Routes remain lightweight controller endpoints.
   - Heavy tasks (calling external AI APIs, speech recognition engines) reside in `app/services/`.
   - Allows switching AI providers (e.g., Mistral to OpenAI) without changing route implementations.

4. **Centralized Configuration (`config.py`)**
   - Manages environment settings (`DevelopmentConfig`, `TestingConfig`, `ProductionConfig`).
   - Ensures sensitive secrets (API keys, database URLs) are loaded securely from `.env`.

---

## 🚀 Setup & Installation Guide

### Prerequisites
- Python 3.10 or higher
- `pip` (Python package manager)

### 1. Clone & Set Up Virtual Environment

```bash
# Navigate to project directory
cd AICareerConnect

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows (PowerShell):
venv\Scripts\Activate.ps1
# Windows (CMD):
venv\Scripts\activate.bat
# Linux/macOS:
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Environment Variables

Copy the `.env.example` file to `.env`:

```bash
cp .env.example .env
```

Edit `.env` and set your credentials:

```env
SECRET_KEY=your-super-secret-key
MISTRAL_API_KEY=your-mistral-api-key
MISTRAL_MODEL=mistral-large-latest
DATABASE_URL=sqlite:///instance/aicareer.db
```

### 4. Run the Application

```bash
python run.py
```

The application will start on `http://127.0.0.1:5000/`.

---

## 🧪 Running Tests

Execute the automated test suite with pytest:

```bash
pytest tests/ -v
```

---

## 📡 API Endpoints Overview

| Blueprint | Method | Endpoint | Description | Auth Required |
|---|---|---|---|---|
| `main` | `GET` | `/` | Landing page | No |
| `auth` | `GET`, `POST` | `/auth/login` | User login form & action | No |
| `auth` | `GET`, `POST` | `/auth/register` | User registration | No |
| `auth` | `GET` | `/auth/logout` | End user session | Yes |
| `career` | `GET` | `/career/chat` | AI Career Counseling chat page | Yes |
| `career` | `POST` | `/career/ask` | Send query to Mistral AI service | Yes |
| `career` | `GET` | `/career/history` | View user's past career sessions | Yes |
| `dashboard`| `GET` | `/dashboard/` | Analytics overview page | Yes |
| `dashboard`| `GET` | `/dashboard/api/stats` | JSON endpoint for career field distribution | Yes |
| `dashboard`| `GET` | `/dashboard/api/metrics`| JSON endpoint for platform usage stats | Yes |
| `speech` | `POST` | `/speech/transcribe` | Upload audio and get transcribed text | Yes |
| `speech` | `POST` | `/speech/synthesize` | Convert text query into audio output | Yes |

---

## 📄 License

Distributed under the **MIT License**. See `LICENSE` for details.
