# Story 1.3: User Registration Endpoint

Status: in-progress

## Story

As a **user**,
I want to **be able to create a new account**,
so that **I can access the application**.

## Acceptance Criteria

1.  **Given** a user provides a valid name, email, and password, **When** a POST request is sent to the `/api/v1/auth/register` endpoint, **Then** a new user account is created in the `auth.users` table in Supabase. (Source: `docs/epics.md#story-1.3`, `docs/architecture.md#4-database-schema`)
2.  **And** a corresponding entry for the user's public profile is inserted into the `profiles` table with `id` linked to `auth.users.id`, `name`, and `created_at`. (Source: `docs/epics.md#story-1.3`, `docs/architecture.md#4-database-schema`)
3.  **And** a success response with a JWT token provided by Supabase is returned to the user. (Source: `docs/epics.md#story-1.3`)
4.  **And** if the email already exists in `auth.users`, a 400 Bad Request error is returned. (Source: `docs/epics.md#story-1.3`)

## Tasks / Subtasks

- [ ] **Task 1: Implement FastAPI Registration Endpoint** (AC: 1, 2, 3, 4)
  - [ ] Create a new endpoint `POST /api/v1/auth/register` in the FastAPI application within `api/api/v1/endpoints`.
  - [ ] Define input schema for user registration (name, email, password) using Pydantic.
  - [ ] Implement logic to interact with Supabase client to create the new user in `auth.users`.
  - [ ] Handle error scenarios where Supabase reports an existing email, returning a 400 HTTP error.
  - [ ] Upon successful user creation in `auth.users`, extract the user ID and create a corresponding entry in the `profiles` table in the database.
  - [ ] Return the JWT token received from Supabase upon successful registration.
- [ ] **Task 2: Write Unit/Integration Tests for Registration Endpoint** (AC: 1, 2, 3, 4)
  - [ ] Create a new test file (e.g., `test_auth_endpoints.py`) within `api/tests/` to cover authentication-related endpoints.
  - [ ] Write a test case for successful user registration, verifying a 200/201 HTTP status code, the structure of the successful response (e.g., presence of JWT), and that a user is created in Supabase `auth.users` and `profiles` table.
  - [ ] Write a test case for attempting to register with an already existing email, verifying a 400 HTTP status code and an appropriate error message.
  - [ ] Ensure tests leverage the FastAPI TestClient for efficient endpoint testing.

## Dev Notes

### Key Implementation Guidance

-   **Monorepo Structure:** Backend implementation will be within the `/api` (FastAPI) project, aligning with the project's monorepo structure.
-   **API Design:** All API endpoints are prefixed with `/api/v1`. The registration endpoint will be `POST /api/v1/auth/register`. (Source: `docs/architecture.md#5-api-endpoint-specification`)
-   **Authentication:** Supabase's built-in authentication will be leveraged. The FastAPI backend will interact with the Supabase API to create users.
-   **User Data Storage:** User authentication details are handled by Supabase `auth.users`. Upon successful user creation, a corresponding public profile entry must be created in the `profiles` table. The schema for this table includes `id` (UUID, Primary Key, Foreign Key to `auth.users.id`), `name` (text), and `created_at` (timestamptz, Not Null, Default `now()`). (Source: `docs/architecture.md#4-database-schema`)
-   **Error Handling:** Implement robust error handling for cases such as existing email addresses, returning a 400 Bad Request error.
-   **Testing:** New tests for this endpoint should be created in the `api/tests/` directory, following existing test patterns in the project. These tests should cover both successful registration and error scenarios.

### Learnings from Previous Story (Story 1.2: User Profile Model & Database Schema)

**From Story 1.2 (Status: done)**

-   **New Files/Paths Created:**
    -   `supabase/migrations/20251201101500_create_profiles_table.sql`: This file demonstrates the standard location and naming convention for database migration scripts.
    -   `api/tests/test_migration_001_profiles.py`: This provides an example of test file placement for database-related functionality.
-   **Architectural Decisions to Reuse:** The precise schema for the `profiles` table is defined, including the foreign key relationship to `auth.users.id`. This must be adhered to when creating the profile entry post-registration. (Source: `docs/architecture.md#4-database-schema`)
-   **Technical Debt/Advisory:**
    -   **Placeholder Test Reminder:** The test for the previous database migration (`test_migration_001_profiles.py`) is a placeholder. This implies that for *this* story, integration tests should focus on the API behavior and Supabase interaction, rather than re-validating the database schema (which is assumed to be correctly migrated). A dedicated future story is still needed for comprehensive database integration testing strategy. (Source: `docs/sprint-artifacts/1-2-user-profile-model-database-schema.md#senior-developer-review-ai`)
    -   **Documentation Gap:** An outstanding item from Story 1.1 persists: "Add explicit guidance for creating and activating a Python virtual environment in `README.md`'s backend setup instructions". While not directly impacting this story's code, it's a general project documentation improvement. (Source: `docs/sprint-artifacts/1-2-user-profile-model-database-schema.md#dev-notes`)

### Project Structure Notes

-   **Alignment:** The implementation of the registration endpoint (code and tests) should continue to adhere to the established monorepo pattern, specifically within the `/api` directory. Endpoint definitions will be in `api/api/v1/endpoints`, and security utilities in `api/core/security`.

### References

-   `docs/epics.md#story-1.3-user-registration-endpoint`
-   `docs/PRD.md#fr-1`
-   `docs/architecture.md#4-database-schema`
-   `docs/architecture.md#5-api-endpoint-specification`
-   `docs/sprint-artifacts/1-2-user-profile-model-database-schema.md`

---

## Dev Agent Record

-   **Context Reference:**
    - `docs/sprint-artifacts/1-3-user-registration-endpoint.context.xml`
-   **Agent Model Used:**
-   **Debug Log References:**
-   **Completion Notes List:**
-   **File List:**

---

## Change Log

-   **2025-12-02:** Initial draft created by `sm` agent.
-   **2025-12-02:** Corrected status to `drafted` and added missing `Dev Agent Record` and `Change Log` sections based on validation feedback.
