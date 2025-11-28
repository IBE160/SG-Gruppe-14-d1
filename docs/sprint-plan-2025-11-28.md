# Sprint Plan - AI Study Buddy

**Sprint Goal:** Establish the foundational user authentication system and project scaffolding, enabling users to register, log in, and manage their sessions securely.

**Sprint Duration:** 1 Week (standard sprint length, can be adjusted based on team velocity)

**Sprint Start Date:** 2025-11-28
**Sprint End Date:** 2025-12-4

---

## Stories for Sprint 1

Based on the `epics.md` and `PRD.md` documents, the following stories from **Epic 1: Foundation & User Onboarding** are selected for Sprint 1. This ensures a complete, end-to-end user authentication flow is delivered.

### Story 1.1: Project Setup & Foundation

**Description:** As a developer, I want a standardized project structure and build system, so that I can begin development efficiently.
**Acceptance Criteria:**
*   **Given** the project repository is cloned
*   **When** I run the project setup script
*   **Then** the required dependencies for the Next.js frontend and FastAPI backend are installed.
*   **And** the basic folder structure for frontend (`/app`) and backend (`/api`) is created.
*   **And** a basic CI/CD pipeline is configured to run tests on push.
**Dependencies:** None
**Technical Notes:** This involves `npx create-next-app@latest app` for frontend and manual setup for FastAPI backend. Initial `pyproject.toml` and `package.json` configurations. Basic GitHub Actions setup.

### Story 1.2: User Profile Model & Database Schema

**Description:** As a developer, I want a database schema for user profiles, so that user profile information can be stored securely.
**Acceptance Criteria:**
*   **Given** the database connection is configured (Supabase)
*   **When** the database migration is run
*   **Then** a `profiles` table is created with columns for `id` (UUID, Primary Key), `name` (text), and `created_at` (timestamp).
*   **And** the `id` column is configured with a foreign key relationship to `auth.users.id` to link profiles to the authentication schema.
**Dependencies:** Story 1.1 (Project Setup)
**Technical Notes:** Supabase will be used for the database.

### Story 1.3: User Registration Endpoint

**Description:** As a user, I want to be able to create a new account, so that I can access the application.
**Acceptance Criteria:**
*   **Given** a user provides a valid name, email, and password
*   **When** a POST request is sent to the `/api/v1/auth/register` endpoint
*   **Then** a new user account is created in the database with a hashed password via Supabase.
*   **And** a success response with a JWT token is returned.
*   **And** if the email already exists, a 400 error is returned.
**Dependencies:** Story 1.2 (User Profile DB Schema)
**Technical Notes:** FastAPI endpoint interacting with Supabase authentication.

### Story 1.4: User Login Endpoint

**Description:** As a user, I want to be able to log in to my account, so that I can access my study materials.
**Acceptance Criteria:**
*   **Given** a user provides a valid email and password
*   **When** a POST request is sent to the `/api/v1/auth/login` endpoint
*   **Then** the system verifies the credentials against Supabase.
*   **And** upon success, a JWT token is returned.
*   **And** if the credentials are invalid, a 401 error is returned.
**Dependencies:** Story 1.2 (User Profile DB Schema)
**Technical Notes:** FastAPI endpoint proxying to Supabase authentication.

### Story 1.5: Frontend Registration Page

**Description:** As a new user, I want a registration page, so that I can sign up for the service.
**Acceptance Criteria:**
*   **Given** I am on the registration page (`/signup`)
*   **When** I fill in my name, email, and password and click "Sign Up"
*   **Then** the application sends a request to the registration endpoint.
*   **And** on success, I am redirected to the dashboard and logged in.
*   **And** if there is an error (e.g., email already taken), an error message is displayed.
**Dependencies:** Story 1.3 (User Registration Endpoint)
**Technical Notes:** Next.js page with form, basic validation, and API integration.

### Story 1.6: Frontend Login Page & Session Management

**Description:** As an existing user, I want a login page and persistent sessions, so that I can access my account easily.
**Acceptance Criteria:**
*   **Given** I am on the login page (`/login`)
*   **When** I enter my email and password and click "Log In"
*   **Then** the application sends a request to the login endpoint.
*   **And** on success, I am redirected to the dashboard.
*   **And** the JWT token is stored securely in the browser (e.g., in an HttpOnly cookie).
*   **And** when I revisit the site, I am automatically logged in if my session is still valid.
**Dependencies:** Story 1.4 (User Login Endpoint)
**Technical Notes:** Next.js page with form, API integration, and secure JWT storage/retrieval.

---

## Technical Considerations for Sprint 1

*   **Repository Structure:** Monorepo with `/app` for Next.js and `/api` for FastAPI.
*   **Database:** Supabase for PostgreSQL and authentication.
*   **Authentication:** Supabase's built-in authentication for users, JWTs for session management.
*   **CI/CD:** Initial setup for basic testing on push.

---

## Definition of Done (DoD) for Stories

*   Code implemented and reviewed.
*   Unit tests written and passing (coverage >= 80%).
*   Integration tests written and passing for API endpoints and UI flows.
*   Documentation updated (if applicable).
*   Feature deployed to development environment.
*   Verified by QA (manual or automated).

---

**Next Steps:**
Team Refinement and Estimation of Sprint 1 Stories.
Ready for Sprint Planning Meeting.
