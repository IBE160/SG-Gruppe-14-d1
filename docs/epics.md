# AI Study Buddy - Epic Breakdown

**Author:** BIP
**Date:** 20. november 2025
**Project Level:** Medium
**Target Scale:** N/A (not specified in PRD)

---

## Overview

This document provides the complete epic and story breakdown for AI Study Buddy, decomposing the requirements from the [PRD](./PRD.md) into implementable stories.

### Epics Summary

*   **Epic 1: User Account & Core Infrastructure**
    *   **Goal:** Establish secure user accounts and the foundational application infrastructure to support all subsequent features.
    *   **Scope:** User registration, login, logout, persistent sessions, basic application setup, and core dependencies. This epic also lays the groundwork for NFR-2 (Security) for user data handling.
    *   **Rationale:** This epic addresses the fundamental need for user management and ensures a stable, secure base for the entire application, directly covering FR-1.

*   **Epic 2: Course & Note Management**
    *   **Goal:** Enable users to effectively create, organize, and manage their study materials through courses and lecture notes.
    *   **Scope:** Full CRUD operations for courses and lecture notes (title and text content), dashboard display of all user-created courses, and listing associated lecture notes within each course page.
    *   **Rationale:** This epic directly implements FR-2 and FR-3, providing users with the essential tools to input and structure their study content.

*   **Epic 3: Quiz Generation & Basic Listing**
    *   **Goal:** Deliver the core functionality allowing users to generate AI-powered multiple-choice quizzes and access them easily.
    *   **Scope:** Generating 10-question quizzes from single notes or 20-question quizzes from courses (if ≥ 2 notes), displaying quizzes in a clean format with correct answers, options to copy or delete quiz content, and a simple, single list view of all generated quizzes.
    *   **Rationale:** This epic directly fulfills FR-4, FR-5, and FR-6, representing the primary value proposition of the AI Study Buddy.

*   **Epic 4: Enhanced Quiz Interaction (Growth Feature)**
    *   **Goal:** Elevate the quiz experience by providing an interactive interface with immediate feedback and progress tracking.
    *   **Scope:** Development of a dedicated quiz-taking interface, functionality for users to submit answers, instant feedback on correctness, and mechanisms to track progress and scores within each quiz.
    *   **Rationale:** This epic addresses FR-7, enhancing user engagement and providing a more robust learning tool as a post-MVP growth feature.

*   **Epic 5: Non-Functional Requirements & System Polish**
    *   **Goal:** Ensure the AI Study Buddy meets crucial non-functional standards for performance, comprehensive security, scalability, full responsiveness, and accessibility.
    *   **Scope:** Implementing NFR-1 (Responsive Performance), NFR-2 (Secure Data Handling beyond basic account security), NFR-3 (Scalable Backend Architecture), NFR-4 (Full Responsiveness across devices), and NFR-5 (WCAG 2.1 Level AA Compliance, including keyboard navigation and screen reader compatibility). This includes integrating these concerns throughout the application.
    *   **Rationale:** Achieving these NFRs is vital for the application's stability, reliability, user trust, and overall quality, ensuring a professional and inclusive user experience.

---

## Epic 1: User Account & Core Infrastructure

**Goal:** Establish secure user accounts and the foundational application infrastructure to support all subsequent features.

### Story 1.1: Project Initialization and Basic Setup

As a developer,
I want the project to be initialized with core dependencies and a basic structure,
So that I can begin developing features on a stable foundation.

**Acceptance Criteria:**

**Given** a new project environment,
**When** the project setup is completed,
**Then** a Next.js frontend and FastAPI backend are scaffolded.
**And** basic routing and dependency management are configured.
**And** a local development environment is operational.

**Prerequisites:** None

**Technical Notes:** Set up Next.js (TypeScript) and FastAPI (Python) projects, configure `package.json`, `requirements.txt`, basic `tsconfig.json`, `tailwind.config.js`. Implement a simple "Hello World" endpoint and corresponding frontend page.

### Story 1.2: User Registration

As a new user,
I want to create an account,
So that I can access the AI Study Buddy features.

**Acceptance Criteria:**

**Given** I am on the registration page,
**When** I provide a unique email and password and submit,
**Then** my account is created securely.
**And** I am automatically logged in.
**And** I receive a confirmation message.

**Prerequisites:** Story 1.1

**Covers:** FR-1

**Technical Notes:** Implement user registration endpoint in FastAPI (Supabase integration for user storage, password hashing). Create registration form in Next.js.

### Story 1.3: User Login and Session Management

As a registered user,
I want to log in and maintain a persistent session,
So that I can access my study materials across visits without re-authenticating constantly.

**Acceptance Criteria:**

**Given** I am on the login page,
**When** I provide my registered email and password and submit,
**Then** I am successfully logged in.
**And** a secure token-based session is established.
**And** my session persists automatically on subsequent visits until I explicitly log out.
**Given** I am logged in,
**When** I close and reopen the browser,
**Then** I am automatically logged into my account.

**Prerequisites:** Story 1.1, Story 1.2

**Covers:** FR-1

**Technical Notes:** Implement login endpoint in FastAPI (token generation, validation). Integrate with Next.js for secure cookie/local storage of tokens and session rehydration.

### Story 1.4: User Logout

As a logged-in user,
I want to securely log out of my account,
So that my session is terminated and my data is protected.

**Acceptance Criteria:**

**Given** I am logged in,
**When** I click the "Logout" button,
**Then** my session is terminated on the server.
**And** my authentication token is cleared from the client.
**And** I am redirected to the login page.

**Prerequisites:** Story 1.3

**Covers:** FR-1

**Technical Notes:** Implement logout endpoint in FastAPI (token invalidation). Update Next.js client to clear token and redirect.

---

## Epic 2: Course & Note Management

**Goal:** Enable users to effectively create, organize, and manage their study materials through courses and lecture notes.

### Story 2.1: Create Course

As a logged-in user,
I want to create a new course with a title and an optional description,
So that I can organize my study materials.

**Acceptance Criteria:**

**Given** I am logged in,
**When** I provide a course title and an optional description,
**Then** a new course is created and associated with my account.
**And** the new course appears on my dashboard.

**Prerequisites:** Story 1.3

**Covers:** FR-2

**Technical Notes:** Implement FastAPI endpoint for course creation. Create a form in Next.js for users to input course details.

### Story 2.2: View All Courses (Dashboard)

As a logged-in user,
I want to see all my created courses,
So that I can easily navigate to my study materials.

**Acceptance Criteria:**

**Given** I am logged in,
**When** I access my dashboard,
**Then** a list of all my courses is displayed, showing at least the title of each course.

**Prerequisites:** Story 2.1

**Covers:** FR-3

**Technical Notes:** Implement FastAPI endpoint to retrieve all courses for a user. Develop a dashboard component in Next.js to display the list of courses.

### Story 2.3: View Notes Within a Course

As a logged-in user,
I want to see all lecture notes associated with a specific course,
So that I can manage and access the content for that course.

**Acceptance Criteria:**

**Given** I am viewing a specific course page,
**When** I access that course,
**Then** a list of all lecture notes belonging to that course is displayed.

**Prerequisites:** Story 2.1

**Covers:** FR-3

**Technical Notes:** Implement FastAPI endpoint to retrieve notes for a given course ID. Develop a course detail page in Next.js to display the notes.

### Story 2.4: Create Lecture Note

As a logged-in user,
I want to create a new lecture note with a title and text content within an existing course,
So that I can add my study material.

**Acceptance Criteria:**

**Given** I am viewing a specific course page,
**When** I provide a note title and text content,
**Then** a new lecture note is created and associated with that course.
**And** the new note appears in the list of notes for that course.

**Prerequisites:** Story 2.3

**Covers:** FR-2

**Technical Notes:** Implement FastAPI endpoint for lecture note creation (associated with a course). Create a form in Next.js for users to input note details.

### Story 2.5: Edit Course Details

As a logged-in user,
I want to update the title or description of an existing course,
So that I can keep my course organization current.

**Acceptance Criteria:**

**Given** I am viewing a course,
**When** I edit its title or description and save,
**Then** the course details are updated.
**And** the changes are reflected on the dashboard and course page.

**Prerequisites:** Story 2.2

**Covers:** FR-2

**Technical Notes:** Implement FastAPI endpoint for updating course details. Create an edit functionality in Next.js.

### Story 2.6: Edit Lecture Note Details

As a logged-in user,
I want to update the title or text content of an existing lecture note,
So that I can refine my study materials.

**Acceptance Criteria:**

**Given** I am viewing a lecture note within a course,
**When** I edit its title or text content and save,
**Then** the lecture note details are updated.
**And** the changes are reflected on the course page.

**Prerequisites:** Story 2.4

**Covers:** FR-2

**Technical Notes:** Implement FastAPI endpoint for updating lecture note details. Create an edit functionality in Next.js.

### Story 2.7: Delete Course

As a logged-in user,
I want to delete an entire course,
So that I can remove outdated or irrelevant study materials.

**Acceptance Criteria:**

**Given** I am viewing a course,
**When** I initiate a delete action and confirm,
**Then** the course and all its associated lecture notes and quizzes are permanently removed from my account.
**And** the course no longer appears on my dashboard.

**Prerequisites:** Story 2.2

**Covers:** FR-2

**Technical Notes:** Implement FastAPI endpoint for deleting a course (with cascading delete for notes and quizzes). Implement delete functionality in Next.js with a confirmation step.

### Story 2.8: Delete Lecture Note

As a logged-in user,
I want to delete a specific lecture note,
So that I can remove individual outdated or irrelevant pieces of study material.

**Acceptance Criteria:**

**Given** I am viewing a lecture note within a course,
**When** I initiate a delete action and confirm,
**Then** the lecture note and any quizzes generated directly from it are permanently removed.
**And** the note no longer appears in the course's note list.

**Prerequisites:** Story 2.4

**Covers:** FR-2

**Technical Notes:** Implement FastAPI endpoint for deleting a lecture note. Implement delete functionality in Next.js with a confirmation step.

---

## Epic 3: Quiz Generation & Basic Listing

**Goal:** Deliver the core functionality allowing users to generate AI-powered multiple-choice quizzes and access them easily.

### Story 3.1: Generate Quiz from Single Lecture Note

As a logged-in user,
I want to generate a 10-question multiple-choice quiz from a single lecture note,
So that I can test my knowledge on specific content.

**Acceptance Criteria:**

**Given** I am viewing a lecture note,
**When** I initiate quiz generation,
**Then** a loading indicator is displayed.
**And** a 10-question multiple-choice quiz is generated by the AI from the note's content.
**And** the generated quiz is saved and associated with the note.
**And** I am presented with the quiz for review.

**Prerequisites:** Story 2.4

**Covers:** FR-4

**Technical Notes:** Implement FastAPI endpoint to send note content to Gemini 2.5 Pro API for quiz generation, receive and parse response, save quiz to database. Create UI in Next.js to trigger generation and display loading state.

### Story 3.2: Generate Quiz from All Notes in a Course

As a logged-in user,
I want to generate a 20-question multiple-choice quiz from all notes within a course (if ≥ 2 notes),
So that I can review a broader range of material for that course.

**Acceptance Criteria:**

**Given** I am viewing a course with at least two lecture notes,
**When** I initiate quiz generation for the course,
**Then** a loading indicator is displayed.
**And** a 20-question multiple-choice quiz is generated by the AI from the combined content of all course notes.
**And** the generated quiz is saved and associated with the course.
**And** I am presented with the quiz for review.

**Prerequisites:** Story 2.3, Story 2.4

**Covers:** FR-4

**Technical Notes:** Implement FastAPI endpoint to combine note content from a course, send to Gemini 2.5 Pro API for quiz generation, receive and parse response, save quiz to database. Create UI in Next.js to trigger generation and display loading state.

### Story 3.3: Confirmation Before Overwriting Existing Quiz

As a user,
I want to be prompted for confirmation before overwriting an existing quiz,
So that I do not accidentally lose a previously generated quiz.

**Acceptance Criteria:**

**Given** an existing quiz is associated with a note or course,
**When** I attempt to generate a new quiz for that same note or course,
**Then** a confirmation dialog appears asking if I want to overwrite the existing quiz.
**And** if I confirm, the new quiz replaces the old one.
**And** if I cancel, the existing quiz remains.

**Prerequisites:** Story 3.1, Story 3.2

**Covers:** FR-4

**Technical Notes:** Implement logic in FastAPI to check for existing quizzes and return a flag. Next.js UI displays a confirmation modal based on this flag.

### Story 3.4: Display Generated Quiz Content

As a logged-in user,
I want to view my generated quizzes in a clean, structured format,
So that I can easily read and use them for study.

**Acceptance Criteria:**

**Given** I have generated a quiz,
**When** I view the quiz,
**Then** each question is displayed with four options, one of which is marked as correct.
**And** a "Correct Answers" section clearly lists the correct option for each question.

**Prerequisites:** Story 3.1, Story 3.2

**Covers:** FR-5

**Technical Notes:** Develop a display component in Next.js to render the quiz data (questions, options, correct answer) from the FastAPI endpoint.

### Story 3.5: Copy Quiz Content

As a logged-in user,
I want to copy the entire content of a generated quiz,
So that I can easily share or use it in other applications.

**Acceptance Criteria:**

**Given** I am viewing a generated quiz,
**When** I click a "Copy Quiz" button,
**Then** the entire quiz content (questions, options, and correct answers section) is copied to my clipboard.
**And** a confirmation message indicates the content has been copied.

**Prerequisites:** Story 3.4

**Covers:** FR-5

**Technical Notes:** Implement client-side JavaScript functionality in Next.js to copy the rendered quiz content to the clipboard.

### Story 3.6: Delete Quiz

As a logged-in user,
I want to delete a previously generated quiz,
So that I can remove outdated or unwanted study materials.

**Acceptance Criteria:**

**Given** I am viewing a quiz or a list of quizzes,
**When** I initiate a delete action for a specific quiz and confirm,
**Then** the quiz is permanently removed from my account.

**Prerequisites:** Story 3.4

**Covers:** FR-5

**Technical Notes:** Implement FastAPI endpoint for deleting a quiz. Implement delete functionality in Next.js with a confirmation step.

### Story 3.7: View List of All Quizzes

As a logged-in user,
I want to view a simple, single list of all my generated quizzes,
So that I can easily find and manage them.

**Acceptance Criteria:**

**Given** I am logged in,
**When** I navigate to the "My Quizzes" section (or equivalent),
**Then** a list of all quizzes I have generated is displayed, showing at least the title or source note/course.

**Prerequisites:** Story 3.1, Story 3.2, Story 3.6

**Covers:** FR-6

**Technical Notes:** Implement FastAPI endpoint to retrieve all quizzes for a user. Develop a dedicated page or component in Next.js to display this list.

---

## Epic 4: Enhanced Quiz Interaction (Growth Feature)

**Goal:** Elevate the quiz experience by providing an interactive interface with immediate feedback and progress tracking.

### Story 4.1: Dedicated Quiz-Taking Interface

As a logged-in user,
I want to access a dedicated interface for taking quizzes,
So that I can focus on answering questions without distractions.

**Acceptance Criteria:**

**Given** I am viewing a generated quiz,
**When** I choose to "Start Quiz" (or equivalent),
**Then** a clean, focused interface displays one question at a time.
**And** navigation controls (e.g., "Next Question", "Previous Question") are available.

**Prerequisites:** Story 3.4

**Covers:** FR-7

**Technical Notes:** Develop a new Next.js route/component for interactive quiz taking. Implement state management for current question, user's answer, and navigation.

### Story 4.2: Submit Answers and Receive Immediate Feedback

As a logged-in user taking a quiz,
I want to submit my answer for each question and receive immediate feedback,
So that I can learn from my mistakes in real-time.

**Acceptance Criteria:**

**Given** I am on a question in the quiz-taking interface,
**When** I select an answer option and submit,
**Then** the interface indicates whether my answer was correct or incorrect.
**And** the correct answer is highlighted.
**And** I cannot change my answer after submission for that question.

**Prerequisites:** Story 4.1

**Covers:** FR-7

**Technical Notes:** Implement client-side logic in Next.js to compare selected answer with the correct answer. Display visual feedback. Store user's selected answer and correctness.

### Story 4.3: Track Quiz Progress

As a logged-in user taking a quiz,
I want to see my progress through the quiz,
So that I know how many questions I have completed and how many are remaining.

**Acceptance Criteria:**

**Given** I am in the quiz-taking interface,
**When** I answer questions,
**Then** a progress indicator (e.g., "Question X of Y") or progress bar updates accordingly.

**Prerequisites:** Story 4.1

**Covers:** FR-7

**Technical Notes:** Implement state tracking in Next.js for current question index and total questions. Display this information in the UI.

### Story 4.4: View Quiz Score at Completion

As a logged-in user,
I want to see my final score and performance summary after completing a quiz,
So that I can evaluate my understanding of the material.

**Acceptance Criteria:**

**Given** I have answered all questions in a quiz,
**When** I complete the quiz (e.g., by clicking a "Finish Quiz" button),
**Then** my total score (e.g., X out of Y correct) is displayed.
**And** a summary of my performance (e.g., number of correct/incorrect answers) is presented.
**And** the score is saved with the quiz history.

**Prerequisites:** Story 4.2, Story 4.3

**Covers:** FR-7

**Technical Notes:** Implement logic in Next.js to calculate final score based on stored correctness. Display results. Implement FastAPI endpoint to save quiz attempt results to the database.

---

## Epic 5: Non-Functional Requirements & System Polish

**Goal:** Ensure the AI Study Buddy meets crucial non-functional standards for performance, comprehensive security, scalability, full responsiveness, and accessibility.

### Story 5.1: API Performance Optimization

As a user,
I want core actions (e.g., note creation, quiz generation) to be fast and responsive,
So that I don't experience frustrating wait times and my study flow is uninterrupted.

**Acceptance Criteria:**

**Given** typical user load,
**When** performing core API actions (e.g., POST /notes, POST /quizzes),
**Then** API response times are consistently below 500ms (NFR-1).
**And** loading indicators are present for longer operations.

**Prerequisites:** All API endpoints for core features (Epics 1, 2, 3)

**Covers:** NFR-1

**Technical Notes:** Implement database indexing, optimize API queries, introduce caching where appropriate, use FastAPI's asynchronous features. Monitor performance with tools.

### Story 5.2: Comprehensive Data Security (Encryption & Authorization)

As a user,
I want my personal information and study notes to be fully secure and private,
So that I trust the application with my data.

**Acceptance Criteria:**

**Given** any data transmission,
**When** data is sent between client and server,
**Then** it is encrypted using TLS (NFR-2).
**Given** sensitive user data stored in the database,
**When** accessing it,
**Then** it is encrypted at rest.
**And** strict authorization rules prevent unauthorized access to any user's data (NFR-2).

**Prerequisites:** Story 1.3 (authentication), all CRUD operations for user data.

**Covers:** NFR-2

**Technical Notes:** Enforce HTTPS, configure database encryption (Supabase provides this), implement row-level security (RLS) policies in Supabase, ensure all API endpoints have robust authorization checks.

### Story 5.3: Scalable Backend Architecture

As a growing user base,
I want the application to remain performant and available,
So that new users can join and existing users can continue to study effectively.

**Acceptance Criteria:**

**Given** an increase in user load and data volume,
**When** the application is used by a larger number of concurrent users,
**Then** the backend scales efficiently to maintain performance (NFR-3).
**And** no significant performance degradation is observed up to X concurrent users (define X based on initial target).

**Prerequisites:** All backend features (Epics 1, 2, 3)

**Covers:** NFR-3

**Technical Notes:** Design FastAPI application for statelessness. Consider deployment on platforms with auto-scaling capabilities (e.g., cloud functions, container orchestration). Optimize database schema and queries.

### Story 5.4: Full Responsiveness Across Devices

As a user,
I want to use the AI Study Buddy on any device,
So that I can study conveniently whether I'm on my desktop, tablet, or mobile phone.

**Acceptance Criteria:**

**Given** the application is accessed on various screen sizes (desktop, tablet, mobile),
**When** interacting with any part of the UI,
**Then** all elements are appropriately sized and positioned, providing an optimal user experience without horizontal scrolling (NFR-4).
**And** all interactive elements are easily tappable/clickable.

**Prerequisites:** All frontend UI features

**Covers:** NFR-4

**Technical Notes:** Implement a mobile-first responsive design strategy using Tailwind CSS. Test across a range of device emulators and actual devices.

### Story 5.5: WCAG 2.1 Level AA Accessibility Compliance

As a user with diverse needs (e.g., using a screen reader or keyboard-only navigation),
I want to fully access and interact with the application,
So that I can study effectively like any other user.

**Acceptance Criteria:**

**Given** any interactive UI element,
**When** navigating with a keyboard,
**Then** all elements are reachable and operable.
**And** clear focus indicators are visible (NFR-5).
**Given** a screen reader is active,
**When** navigating through the application,
**Then** all content and interactive elements are correctly announced and understandable (NFR-5).
**And** the application adheres to WCAG 2.1 Level AA guidelines.

**Prerequisites:** All frontend UI features

**Covers:** NFR-5

**Technical Notes:** Use semantic HTML. Implement ARIA attributes where necessary. Ensure sufficient color contrast. Conduct regular accessibility audits with tools like Lighthouse and screen readers.

---

_For implementation: Use the `create-story` workflow to generate individual story implementation plans from this epic breakdown._
The `docs/epics.md` file has been created and populated with the epic and story breakdown for the AI Study Buddy project.

This document serves as the implementation breakdown derived from the PRD, ready for subsequent architecture and development phases.