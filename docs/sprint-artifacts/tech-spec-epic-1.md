# Epic Technical Specification: Foundation & User Onboarding

Date: 2025-11-28
Author: BIP
Epic ID: 1
Status: Draft

---

## Overview

This Technical Specification details the implementation for **Epic 1: Foundation & User Onboarding** of the AI Study Buddy application. This epic establishes the core project infrastructure and enables secure user account creation, login, and session management, as defined in the Product Requirements Document (PRD - FR-1) and elaborated in `epics.md`.

## Objectives and Scope

**In-Scope:**
*   Project scaffolding and build system setup for both frontend (Next.js) and backend (FastAPI).
*   User profile database schema (Supabase).
*   Backend API endpoints for user registration and login.
*   Frontend pages for user registration and login.
*   Secure handling of user sessions.
*   Basic CI/CD setup for testing.

**Out-of-Scope:**
*   Any functionality beyond user registration, login, and session management (e.g., note management, quiz generation).
*   Advanced user profile features (e.g., password reset, profile editing).
*   Comprehensive error handling beyond basic success/failure messages at this stage.

## System Architecture Alignment

This epic aligns directly with the established three-tier architecture outlined in `architecture.md`:
*   **Next.js Frontend (`/app`):** Responsible for UI rendering and user interaction (registration/login pages).
*   **FastAPI Backend (`/api`):** Serves as the authoritative API, handling business logic for authentication and interacting with Supabase.
*   **Supabase:** Provides PostgreSQL for data persistence (user profiles) and handles secure user authentication (`auth.users` table).

All interactions between frontend and backend will occur via secure API calls, and Supabase will manage the core authentication process.

## Detailed Design

### Services and Modules

*   **Frontend (Next.js /app):**
    *   `/app/(auth)/login/page.js`: User login UI.
    *   `/app/(auth)/signup/page.js`: User registration UI.
    *   `lib/api.js`: Handles API calls to the FastAPI backend.
    *   `lib/supabase.js`: Initializes Supabase client for potential direct client-side interactions (e.g., session management).
*   **Backend (FastAPI /api):**
    *   `api/main.py`: Main FastAPI application entry point.
    *   `api/v1/endpoints/auth.py`: Contains registration (`/api/v1/auth/register`) and login (`/api/v1/auth/login`) API routes.
    *   `core/security.py`: Handles JWT generation/validation (if not fully delegated to Supabase tokens) and password hashing.
    *   `db/models.py`: Defines Pydantic models for user profiles and authentication requests/responses.
    *   `db/session.py`: Manages database sessions and connections to Supabase.

### Data Models and Contracts

*   **Supabase `profiles` Table (from `architecture.md` and `epics.md` Story 1.2):**
    | Column | Type | Constraints |
    | :--- | :--- | :--- |
    | `id` | `uuid` | Primary Key, FK to `auth.users.id` |
    | `name` | `text` | |
    | `created_at` | `timestamptz` | Not Null, Default `now()` |
*   **FastAPI Request/Response Models (Pydantic):**
    *   `UserRegisterRequest`: `name`, `email`, `password`.
    *   `UserLoginRequest`: `email`, `password`.
    *   `AuthResponse`: `access_token`, `token_type`.

### APIs and Interfaces

*   **Backend API Endpoints (from `architecture.md` and `epics.md` Story 1.3, 1.4):**
    *   `POST /api/v1/auth/register`:
        *   **Request:** JSON body `UserRegisterRequest`.
        *   **Response:** 200 OK with `AuthResponse` (JWT token) on success; 400 Bad Request if email exists.
    *   `POST /api/v1/auth/login`:
        *   **Request:** JSON body `UserLoginRequest`.
        *   **Response:** 200 OK with `AuthResponse` (JWT token) on success; 401 Unauthorized for invalid credentials.

### Workflows and Sequencing

1.  **User Registration Flow:**
    *   User navigates to `/signup` on Next.js frontend.
    *   User enters details, submits form.
    *   Frontend sends `POST /api/v1/auth/register` request.
    *   FastAPI backend interacts with Supabase to create `auth.users` entry and `profiles` table entry.
    *   Supabase returns JWT. FastAPI passes JWT to frontend.
    *   Frontend stores JWT securely (HttpOnly cookie) and redirects to dashboard.
2.  **User Login Flow:**
    *   User navigates to `/login` on Next.js frontend.
    *   User enters credentials, submits form.
    *   Frontend sends `POST /api/v1/auth/login` request.
    *   FastAPI backend authenticates via Supabase.
    *   Supabase returns JWT. FastAPI passes JWT to frontend.
    *   Frontend stores JWT securely and redirects to dashboard.
3.  **Session Management:**
    *   On subsequent visits, frontend checks for valid JWT. If present and valid, user is automatically logged in. If expired, user is prompted to re-login.

## Non-Functional Requirements

*   **Performance (NFR-1):** API response times for registration/login should be minimized (e.g., <500ms). Frontend rendering of auth pages should be fast.
*   **Security (NFR-2):**
    *   User data (emails, passwords) handled securely; passwords hashed and salted by Supabase.
    *   Encryption in transit (TLS/HTTPS) for all API communication.
    *   JWTs used for authorization and stored securely (e.g., HttpOnly cookies on frontend).
    *   Authorization checks to ensure users only access their own profile data (though minimal for this epic).
*   **Scalability (NFR-3):** Initial design of FastAPI and Next.js should support future scaling by leveraging stateless authentication with JWTs and Supabase's managed scaling.
*   **Accessibility & Usability (NFR-4, NFR-5):** Registration and login pages will be responsive across devices and implement foundational WCAG 2.1 Level AA standards (e.g., keyboard navigation, ARIA labels for screen readers).

## Dependencies and Integrations

*   **Next.js (Frontend):** For UI and client-side logic.
*   **FastAPI (Backend):** For API services and business logic.
*   **Supabase:**
    *   Authentication service (`auth.users`).
    *   PostgreSQL database (for `profiles` table).
*   **Python `requests` / `httpx` (Backend):** For inter-service communication (e.g., FastAPI to Supabase API if direct calls are needed).
*   **NPM / Yarn:** Frontend package management.
*   **Pip / Poetry:** Backend package management.
*   **GitHub Actions:** For basic CI/CD pipeline.

## Acceptance Criteria (Authoritative)

The acceptance criteria for the stories within Epic 1 are directly taken from `epics.md`:

### Story 1.1: Project Setup & Foundation
*   **Given** the project repository is cloned
*   **When** I run the project setup script
*   **Then** the required dependencies for the Next.js frontend and FastAPI backend are installed.
*   **And** the basic folder structure for frontend and backend is created.
*   **And** a basic CI/CD pipeline is configured to run tests on push.

### Story 1.2: User Profile Model & Database Schema
*   **Given** the database connection is configured (Supabase)
*   **When** the database migration is run
*   **Then** a `profiles` table is created with columns for `id` (UUID, Primary Key), `name` (text), and `created_at` (timestamp).
*   **And** the `id` column is configured with a foreign key relationship to `auth.users.id` to link profiles to the authentication schema.

### Story 1.3: User Registration Endpoint
*   **Given** a user provides a valid name, email, and password
*   **When** a POST request is sent to the `/api/v1/auth/register` endpoint
*   **Then** a new user account is created in the database with a hashed password via Supabase.
*   **And** a success response with a JWT token is returned.
*   **And** if the email already exists, a 400 error is returned.

### Story 1.4: User Login Endpoint
*   **Given** a user provides a valid email and password
*   **When** a POST request is sent to the `/api/v1/auth/login` endpoint
*   **Then** the system verifies the credentials against Supabase.
*   **And** upon success, a JWT token is returned.
*   **And** if the credentials are invalid, a 401 error is returned.

### Story 1.5: Frontend Registration Page
*   **Given** I am on the registration page (`/signup`)
*   **When** I fill in my name, email, and password and click "Sign Up"
*   **Then** the application sends a request to the registration endpoint.
*   **And** on success, I am redirected to the dashboard and logged in.
*   **And** if there is an error (e.g., email already taken), an error message is displayed.

### Story 1.6: Frontend Login Page & Session Management
*   **Given** I am on the login page (`/login`)
*   **When** I enter my email and password and click "Log In"
*   **Then** the application sends a request to the login endpoint.
*   **And** on success, I am redirected to the dashboard.
*   **And** the JWT token is stored securely in the browser (e.g., in an HttpOnly cookie).
*   **And** when I revisit the site, I am automatically logged in if my session is still valid.

## Traceability Mapping

| Acceptance Criterion | Spec Section(s)             | Component(s)/API(s)                  | Test Idea                                    |
| :------------------- | :-------------------------- | :----------------------------------- | :------------------------------------------- |
| Story 1.1 AC 1-4     | Project Scaffolding         | `.bmad`, `/app`, `/api`, `.github/workflows` | Run setup script, check file structure, run CI. |
| Story 1.2 AC 1-3     | Data Models                 | Supabase, `db/models.py`             | Database migration test, check table schema. |
| Story 1.3 AC 1-4     | APIs, Services/Modules      | `auth.py`, Supabase                  | Integration test: POST `/register` success/fail. |
| Story 1.4 AC 1-3     | APIs, Services/Modules      | `auth.py`, Supabase                  | Integration test: POST `/login` success/fail. |
| Story 1.5 AC 1-4     | Frontend, Workflows         | `signup/page.js`                     | E2E test: User registration via UI.           |
| Story 1.6 AC 1-4     | Frontend, Workflows, Security | `login/page.js`                      | E2E test: User login, session persistence.    |

## Risks, Assumptions, Open Questions

*   **Risk:** Over-reliance on Supabase for Auth logic may limit customization.
    *   **Mitigation:** Document Supabase capabilities and limitations early. Plan for potential migration if needed.
*   **Assumption:** Supabase free tier is sufficient for initial development and testing.
*   **Question:** Specific JWT storage mechanism (e.g., HttpOnly cookies vs. local storage) needs final confirmation for frontend. Initial plan is HttpOnly cookies for better security.

## Test Strategy Summary

*   **Unit Tests:** For individual functions/modules in FastAPI (e.g., `core/security.py`) and Next.js utility functions.
*   **Integration Tests:** For FastAPI endpoints (e.g., testing `/register` and `/login` with Supabase mocks or test instance).
*   **End-to-End (E2E) Tests:** Using Playwright or Cypress for full user flows (registration, login, session persistence) in the Next.js application.
*   **CI/CD:** Basic GitHub Actions workflow to run unit and integration tests on push to ensure code quality and prevent regressions. Coverage target: >= 80%.
