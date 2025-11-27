# AI Study Buddy - Solution Architecture

**Version:** 1.0
**Date:** 26. november 2025
**Author:** Winston (Architect Agent)

---

## 1. Executive Summary

This document outlines the technical architecture for the **AI Study Buddy**, a web application that allows students to generate quizzes from their study notes. The architecture is designed to be a scalable and secure system, composed of a **Next.js** frontend, a **FastAPI** backend, and **Supabase** for data persistence and authentication. The FastAPI backend serves as the single authoritative API for the frontend, ensuring all business logic and data access is centralized and secure.

---

## 2. Scaffolding & Project Initialization

The project will be structured as a monorepo with two distinct packages: `/app` for the frontend and `/api` for the backend.

**To initialize the project:**

1.  **Frontend (Next.js):**
    ```bash
    npx create-next-app@latest app
    ```

2.  **Backend (FastAPI):**
    A Python project will be manually set up in the `/api` directory with a `pyproject.toml` to manage dependencies.

---

## 3. Services & Data Flow

The system follows a clear three-tier pattern where the client only interacts with the trusted backend API.

*   **Data Flow Diagram:**
    ```mermaid
    graph LR
        A[User's Browser] -- HTTPS --> B(Next.js Frontend);
        B -- API Calls --> C(FastAPI Backend);
        C -- Python Client --> D(Supabase Auth);
        C -- Python Client --> E(Supabase Database);
    ```

*   **Interaction Model:**
    1.  The **Next.js Frontend** is responsible for all UI rendering and user interaction.
    2.  The **FastAPI Backend** serves as the single authoritative API, containing all business logic, including the AI quiz generation.
    3.  **Supabase** provides the Postgres database for data persistence and handles user authentication.

---

## 4. Database Schema

The database will be hosted on Supabase Postgres and structured as follows:

**`profiles` Table**
| Column | Type | Constraints |
| :--- | :--- | :--- |
| `id` | `uuid` | Primary Key, FK to `auth.users.id` |
| `name` | `text` | |
| `created_at` | `timestamptz` | Not Null, Default `now()` |

**`courses` Table**
| Column | Type | Constraints |
| :--- | :--- | :--- |
| `id` | `uuid` | Primary Key, Default `gen_random_uuid()` |
| `user_id` | `uuid` | Not Null, FK to `profiles.id` |
| `title` | `text` | Not Null |
| `description`| `text` | Nullable |
| `created_at` | `timestamptz` | Not Null, Default `now()` |

**`notes` Table**
| Column | Type | Constraints |
| :--- | :--- | :--- |
| `id` | `uuid` | Primary Key, Default `gen_random_uuid()` |
| `course_id` | `uuid` | Not Null, FK to `courses.id` |
| `title` | `text` | Not Null |
| `content` | `text` | |
| `created_at` | `timestamptz` | Not Null, Default `now()` |
| `updated_at` | `timestamptz` | Not Null, Default `now()` |

**`quizzes` Table**
| Column | Type | Constraints |
| :--- | :--- | :--- |
| `id` | `uuid` | Primary Key, Default `gen_random_uuid()` |
| `user_id` | `uuid` | Not Null, FK to `profiles.id`|
| `note_id` | `uuid` | Nullable, FK to `notes.id` |
| `course_id` | `uuid` | Nullable, FK to `courses.id` |
| `content` | `jsonb` | Not Null |
| `created_at` | `timestamptz` | Not Null, Default `now()` |

---

## 5. API Endpoint Specification

All endpoints are prefixed with `/api/v1` and require a valid JWT for authorization.

#### **Courses (`/courses`)**
*   `GET /`: Get all courses for the user.
*   `POST /`: Create a new course.
*   `GET /{course_id}`: Get a single course.
*   `PUT /{course_id}`: Update a course.
*   `DELETE /{course_id}`: Delete a course.

#### **Notes (`/courses/{course_id}/notes`)**
*   `GET /`: Get all notes for a course.
*   `POST /`: Create a new note within the course.
*   `GET /{note_id}`: Get a single note.
*   `PUT /{note_id}`: Update a note.
*   `DELETE /{note_id}`: Delete a note.

#### **Quizzes (`/quizzes`)**
*   `GET /`: Get all quizzes for the user.
*   `GET /{quiz_id}`: Get a single quiz.
*   `DELETE /{quiz_id}`: Delete a quiz.
*   `POST /generate-from-note`: Trigger AI generation from a note.
*   `POST /generate-from-course`: Trigger AI generation from a course.

---

## 6. Project Structure & Implementation Patterns

### Frontend (`/app` - Next.js)
```
app/
├── (auth)/
│   ├── login/page.js
│   └── signup/page.js
├── (dashboard)/
│   ├── courses/
│   ├── layout.js
│   └── page.js
├── layout.js
└── page.js
components/
├── ui/
└── features/
lib/
├── api.js
├── hooks.js
└── supabase.js
styles/
└── globals.css
```

### Backend (`/api` - FastAPI)
```
api/
├── main.py
├── api/
│   └── v1/
│       ├── endpoints/
│       └── dependencies.py
├── core/
│   ├── config.py
│   └── security.py
├── db/
│   ├── models.py
│   └── session.py
└── services/
    └── quiz_generator.py
```
