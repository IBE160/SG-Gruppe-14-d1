# ibe160 - Epic Breakdown

**Author:** BIP
**Date:** torsdag 27. november 2025
**Project Level:** 3
**Target Scale:** N/A (not specified in PRD)

---

## Overview

This document provides the complete epic and story breakdown for ibe160, decomposing the requirements from the [PRD](./PRD.md) into implementable stories.

**Living Document Notice:** This is the initial version. It will be updated after UX Design and Architecture workflows add interaction and technical details to stories.

## Epic Summary

The project will be broken down into three main epics, each delivering incremental user value:

*   **Epic 1: Foundation & User Onboarding:** Establishes the project foundation and allows users to create accounts and log in.
*   **Epic 2: Core Content Management:** Enables users to create, organize, and manage their courses and lecture notes.
*   **Epic 3: AI-Powered Quiz Generation & Review:** Delivers the core AI functionality, allowing users to generate and review quizzes from their notes.

---

## Functional Requirements Inventory

*   **FR-1:** Users must be able to create, log in to, and log out of their accounts, with persistent sessions automatically logging them in on return visits. (MVP)
*   **FR-2:** Users can perform full Create, Read, Update, Delete (CRUD) operations on courses (including a title and optional description) and lecture notes (title and text content) within a course. (MVP)
*   **FR-3:** The dashboard will display all user-created courses, and each course page will list its associated lecture notes. (MVP)
*   **FR-4:** Users can generate multiple-choice quizzes from a single lecture note (10 questions) or from all notes within a course (20 questions, enabled if ≥ 2 notes). A loading indicator will be shown during generation, and confirmation will be requested before overwriting existing quizzes. (MVP)
*   **FR-5:** Generated quizzes must be displayed in a clean, structured format, with each question having four options (one correct). A "Correct Answers" section will list the correct option for each question. Users can copy the entire quiz content or delete previously generated quizzes. (MVP)
*   **FR-6:** Users must be able to view a simple, single list of all their generated quizzes. (MVP)

---

## FR Coverage Map

## FR Coverage Map

This map shows how the functional requirements are distributed across the proposed epics.

*   **Epic 1: Foundation & User Onboarding**
    *   **FR-1:** User Account Management
*   **Epic 2: Core Content Management**
    *   **FR-2:** Course & Note Management (CRUD)
    *   **FR-3:** Dashboard and Note Listing
*   **Epic 3: AI-Powered Quiz Generation & Review**
    *   **FR-4:** Quiz Generation
    *   **FR-5:** Quiz Display and Interaction
    *   **FR-6:** Quiz Listing

---

## Epic 1: Foundation & User Onboarding

**Goal:** Establishes the project foundation and allows users to create accounts and log in.

### Story 1.1: Project Setup & Foundation

As a developer,
I want a standardized project structure and build system,
So that I can begin development efficiently.

**Acceptance Criteria:**

**Given** the project repository is cloned
**When** I run the project setup script
**Then** the required dependencies for the Next.js frontend and FastAPI backend are installed.
**And** the basic folder structure for frontend and backend is created.
**And** a basic CI/CD pipeline is configured to run tests on push.

**Prerequisites:** None

**Technical Notes:** This story involves setting up the initial scaffolding for the Next.js and FastAPI applications. It includes initializing `npm` and `pip`, installing core libraries (React, Next.js, FastAPI, Uvicorn, Pydantic), and creating the source code directories. A simple GitHub Actions workflow should be created to run placeholder tests.

### Story 1.2: User Profile Model & Database Schema

As a developer,
I want a database schema for user profiles,
So that user profile information can be stored securely.

**Acceptance Criteria:**

**Given** the database connection is configured
**When** the database migration is run
**Then** a `profiles` table is created with columns for `id` (UUID, Primary Key), `name` (text), and `created_at` (timestamp).
**And** the `id` column is configured with a foreign key relationship to `auth.users.id` to link profiles to the authentication schema.

**Prerequisites:** Story 1.1

**Technical Notes:** This will be implemented using Supabase. Supabase's built-in `auth.users` table will handle authentication details. This `profiles` table stores public user data. The schema will be defined and managed through Supabase's dashboard or migration scripts.

### Story 1.3: User Registration Endpoint

As a user,
I want to be able to create a new account,
So that I can access the application.

**Acceptance Criteria:**

**Given** a user provides a valid name, email, and password
**When** a POST request is sent to the `/api/v1/auth/register` endpoint
**Then** a new user account is created in the database with a hashed password.
**And** a success response with a JWT token is returned.
**And** if the email already exists, a 400 error is returned.

**Prerequisites:** Story 1.2

**Technical Notes:** This FastAPI endpoint will handle user registration by interacting with the Supabase authentication API. It will create the user in `auth.users` and, upon successful creation, insert a corresponding entry into the public `profiles` table. Upon success, it will return the JWT token provided by Supabase.

### Story 1.4: User Login Endpoint

As a user,
I want to be able to log in to my account,
So that I can access my study materials.

**Acceptance Criteria:**

**Given** a user provides a valid email and password
**When** a POST request is sent to the `/api/v1/auth/login` endpoint
**Then** the system verifies the credentials against the database.
**And** upon success, a JWT token is returned.
**And** if the credentials are invalid, a 401 error is returned.

**Prerequisites:** Story 1.2

**Technical Notes:** This FastAPI endpoint will authenticate users by proxying credentials to the Supabase authentication API. It will not directly access password hashes. On successful authentication with Supabase, it will issue a JWT token.

### Story 1.5: Frontend Registration Page

As a new user,
I want a registration page,
So that I can sign up for the service.

**Acceptance Criteria:**

**Given** I am on the registration page
**When** I fill in my name, email, and password and click "Sign Up"
**Then** the application sends a request to the registration endpoint.
**And** on success, I am redirected to the dashboard and logged in.
**And** if there is an error (e.g., email already taken), an error message is displayed.

**Prerequisites:** Story 1.3

**Technical Notes:** This will be a Next.js page with a form to collect user registration details. It will use `fetch` or `axios` to call the backend API. State management will be used to handle loading and error states.

### Story 1.6: Frontend Login Page & Session Management

As an existing user,
I want a login page and persistent sessions,
So that I can access my account easily.

**Acceptance Criteria:**

**Given** I am on the login page
**When** I enter my email and password and click "Log In"
**Then** the application sends a request to the login endpoint.
**And** on success, I am redirected to the dashboard.
**And** the JWT token is stored securely in the browser (e.g., in an HttpOnly cookie).
**And** when I revisit the site, I am automatically logged in if my session is still valid.

**Prerequisites:** Story 1.4

**Technical Notes:** This Next.js page will handle user login. Upon successful login, the JWT token should be stored securely. A mechanism to check for the token on app load should be implemented to provide persistent sessions.

---

## Epic 2: Core Content Management

**Goal:** Enables users to create, organize, and manage their courses and lecture notes.

### Story 2.1: Course & Note Database Schema

As a developer,
I want a database schema for courses and notes,
So that I can store and relate content for each user.

**Acceptance Criteria:**

**Given** the database connection is configured
**When** the database migration is run
**Then** a `courses` table is created with columns for `id`, `user_id` (foreign key to profiles), `title`, `description`, and timestamps.
**And** a `notes` table is created with columns for `id`, `course_id` (foreign key to courses), `title`, `content`, and timestamps.

**Prerequisites:** Story 1.2

**Technical Notes:** The `user_id` and `course_id` foreign keys will enforce data integrity. The `description` in courses will be optional.

### Story 2.2: Course Management API Endpoints

As a developer,
I want API endpoints for course management,
So that the frontend can perform CRUD operations on courses.

**Acceptance Criteria:**

**Given** a user is authenticated
**When** requests are sent to the `/api/v1/courses` endpoints
**Then** the following endpoints are available:
- `GET /courses`: List all courses for the authenticated user.
- `POST /courses`: Create a new course.
- `GET /courses/{course_id}`: Get a single course by ID.
- `PUT /courses/{course_id}`: Update a course.
- `DELETE /courses/{course_id}`: Delete a course.
**And** only the owner of the course can access or modify it.

**Prerequisites:** Story 1.4, Story 2.1

**Technical Notes:** These FastAPI endpoints will handle all CRUD operations for courses. Authorization logic must be implemented to ensure users can only access their own data.

### Story 2.3: Note Management API Endpoints

As a developer,
I want API endpoints for note management,
So that the frontend can perform CRUD operations on notes within a course.

**Acceptance Criteria:**

**Given** a user is authenticated
**When** requests are sent to the `/api/v1/courses/{course_id}/notes` endpoints
**Then** the following nested endpoints are available:
- `GET /`: List all notes for the specified course.
- `POST /`: Create a new note in the course.
- `GET /{note_id}`: Get a single note by ID.
- `PUT /{note_id}`: Update a note.
- `DELETE /{note_id}`: Delete a note.
**And** only the owner of the course can manage its notes.

**Prerequisites:** Story 2.2

**Technical Notes:** These nested FastAPI endpoints will manage notes within the context of a course. Authorization will be inherited from the course ownership.

### Story 2.4: Frontend Dashboard for Course Listing

As a user,
I want a dashboard where I can see all my courses,
So that I can easily navigate to my study materials.

**Acceptance Criteria:**

**Given** I am logged in
**When** I visit the dashboard
**Then** all my courses are displayed in a list.
**And** each course card shows the title and number of notes.
**And** there is a button to create a new course.
**And** if I have no courses, a message is displayed prompting me to create one.

**Prerequisites:** Story 1.6, Story 2.2

**Technical Notes:** This Next.js page will fetch the list of courses from the API and display them. It will handle the empty state and provide a way to initiate the creation of a new course.

### Story 2.5: Frontend Course Page for Note Listing

As a user,
I want to see all the lecture notes for a specific course,
So that I can manage them.

**Acceptance Criteria:**

**Given** I am on the dashboard
**When** I click on a course
**Then** I am taken to the course page.
**And** the course title and description are displayed.
**And** all notes for that course are listed.
**And** there are options to add, edit, or delete notes.
**And** there is an option to edit or delete the course.

**Prerequisites:** Story 2.3, Story 2.4

**Technical Notes:** This dynamic Next.js page will fetch and display the details for a specific course, including its list of notes. It will provide the UI for all CRUD operations on the course and its notes.

---

## Epic 3: AI-Powered Quiz Generation & Review

**Goal:** Delivers the core AI functionality, allowing users to generate and review quizzes from their notes.

### Story 3.1: Quiz Database Schema

As a developer,
I want a database schema for quizzes,
So that I can store generated quizzes and their content.

**Acceptance Criteria:**

**Given** the database connection is configured
**When** the database migration is run
**Then** a `quizzes` table is created with columns for `id`, `note_id` (foreign key to notes), `course_id` (foreign key to courses, nullable), `content` (JSONB to store questions and answers), and timestamps.

**Prerequisites:** Story 2.1

**Technical Notes:** The `content` column will store the quiz questions, options, and correct answers in a structured JSON format. A quiz can be linked to either a note or a course.

### Story 3.2: AI Quiz Generation Service

As a developer,
I want a service that integrates with the Gemini API to generate quizzes from text,
So that I can create quizzes from user notes.

**Acceptance Criteria:**

**Given** a text input (from a note or concatenation of notes)
**When** the quiz generation service is called
**Then** it sends a formatted prompt to the Gemini API.
**And** it receives a JSON response containing a list of multiple-choice questions.
**And** the response is validated to ensure it matches the expected format (question, options, correct answer index).

**Prerequisites:** None

**Technical Notes:** This service will be a Python module using Pydantic AI to interact with the Gemini API. It will handle prompt engineering, API calls, and response parsing/validation. Error handling for API failures or invalid JSON is crucial.

### Story 3.3: Quiz Generation API Endpoints

As a developer,
I want API endpoints to trigger quiz generation,
So that the frontend can request quizzes for notes or courses.

**Acceptance Criteria:**

**Given** a user is authenticated
**When** a POST request is sent to `/api/v1/notes/{note_id}/generate-quiz` or `/api/v1/courses/{course_id}/generate-quiz`
**Then** the backend retrieves the note/course content.
**And** it calls the AI Quiz Generation Service.
**And** it saves the generated quiz to the database, linked to the note/course.
**And** it returns the newly created quiz.

**Prerequisites:** Story 3.1, Story 3.2

**Technical Notes:** These FastAPI endpoints will orchestrate the quiz generation process. For course-level quizzes, the content of all notes in the course will be concatenated. The endpoints will show a loading indicator and handle overwriting existing quizzes as per FR-4.

### Story 3.4: Frontend Quiz Generation & Display

As a user,
I want to be able to generate a quiz from my notes and see the result,
So that I can start studying.

**Acceptance Criteria:**

**Given** I am on a note or course page
**When** I click the "Generate Quiz" button
**Then** a loading indicator is displayed while the quiz is being generated.
**And** once complete, the generated quiz is displayed in a clean, readable format.
**And** the quiz shows the questions, multiple-choice options, and a separate section for correct answers.
**And** I have options to copy the quiz content or delete the quiz.

**Prerequisites:** Story 3.3

**Technical Notes:** The frontend will call the quiz generation API and handle the loading state. The quiz will be displayed on a new page or in a modal. The layout should be clean and easy to read, as specified in FR-5.

### Story 3.5: Frontend Quiz Listing Page

As a user,
I want a page where I can see all the quizzes I've generated,
So that I can easily access them.

**Acceptance Criteria:**

**Given** I am logged in
**When** I navigate to the "My Quizzes" page
**Then** a list of all my quizzes is displayed.
**And** each item in the list shows the quiz source (note or course title) and the date it was generated.
**And** clicking on a quiz takes me to the quiz display page.

**Prerequisites:** Story 3.3

**Technical Notes:** This will be a new page in the Next.js app that fetches and lists all quizzes for the user.

---

---

## FR Coverage Matrix

| FR | Description | Covered by Story(s) |
| :--- | :--- | :--- |
| FR-1 | User Account Management | 1.3, 1.4, 1.5, 1.6 |
| FR-2 | Course & Note Management (CRUD) | 2.2, 2.3, 2.5 |
| FR-3 | Dashboard and Note Listing | 2.4, 2.5 |
| FR-4 | Quiz Generation | 3.3, 3.4 |
| FR-5 | Quiz Display and Interaction | 3.4 |
| FR-6 | Quiz Listing | 3.5 |

---

## Summary

This document outlines the epic and story breakdown for the AI Study Buddy application. The work is organized into three value-driven epics:

1.  **Foundation & User Onboarding:** Sets up the project and builds the complete user authentication system.
2.  **Core Content Management:** Provides users with the tools to create and manage their courses and notes.
3.  **AI-Powered Quiz Generation & Review:** Implements the core AI feature, allowing users to generate and review quizzes.

This breakdown covers all MVP functional requirements, with each story representing a small, implementable unit of work. The structure ensures that value is delivered incrementally, starting with the most fundamental features and building up to the application's core AI capabilities.

---

_For implementation: Use the `create-story` workflow to generate individual story implementation plans from this epic breakdown._

_This document will be updated after UX Design and Architecture workflows to incorporate interaction details and technical decisions._
