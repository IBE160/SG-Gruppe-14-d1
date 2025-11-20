# AI Study Buddy - Epic Breakdown

**Author:** BIP
**Date:** 20. november 2025
**Project Level:** Medium
**Target Scale:** Web Application (SPA)

---

## Overview

This document provides the complete epic and story breakdown for the AI Study Buddy application, decomposing the requirements from the [PRD](./PRD.md) into implementable stories.

The project is broken down into the following epics, designed to deliver incremental value and build upon a solid foundation:

- **Epic 1: Foundational Setup & Core Infrastructure:** Establishes the complete project skeleton, including repository setup, a CI/CD pipeline, database schema, and the basic frontend and backend application structures. This epic is foundational for all subsequent development.
- **Epic 2: User Authentication & Session Management:** Implements a secure system for users to create accounts, log in, and maintain persistent sessions, ensuring that all user data is protected.
- **Epic 3: Course and Note Management:** Delivers the core content creation functionality, allowing users to create, view, update, and delete their courses and lecture notes.
- **Epic 4: AI-Powered Quiz Generation:** Focuses on the core "magic" of the application by implementing the AI-driven service to generate multiple-choice quizzes from user notes.
- **Epic 5: Quiz Interaction & Presentation:** Provides the user-facing functionality for viewing, using, and managing the generated quizzes in a clean and structured format.
- **Epic 6: Accessibility Compliance:** Ensures the application is fully accessible by implementing WCAG 2.1 AA standards, including full keyboard navigation and screen reader compatibility.

---

## Epic 1: Foundational Setup & Core Infrastructure (MVP)

To establish the complete project skeleton, including repository setup, a CI/CD pipeline, database schema, and the basic frontend and backend application structures, creating a stable foundation for all future development.

-   **Story 1.1:** As a user, I want the application to be built on a solid foundation, so that my experience is reliable and new features are added consistently. (MVP)
    *   **FR/NFRs:** NFR-1, NFR-6
    *   **Acceptance Criteria:**
        *   Project repository is initialized and configured.
        *   Basic CI/CD pipeline is set up for automated builds and tests.
        *   Core application structure for frontend and backend is in place.

-   **Story 1.2:** As a user, I want to trust that my study notes are saved securely, so that I can use the app without worrying about data loss. (MVP)
    *   **FR/NFRs:** NFR-3, NFR-4, NFR-5
    *   **Acceptance Criteria:**
        *   Database schema is defined for secure storage of user data and notes.
        *   User data (including notes) is encrypted at rest and in transit.
        *   Basic authorization mechanisms are implemented to prevent unauthorized access.

-   **Story 1.3:** As a user, I want the application to feel responsive and functional from the very first visit, so that I know it's a quality product. (MVP)
    *   **FR/NFRs:** NFR-1, NFR-7
    *   **Acceptance Criteria:**
        *   Initial page load time is optimized for responsiveness.
        *   Basic application functions (e.g., navigation, button clicks) respond fluidly.

---

## Epic 2: User Authentication & Session Management (MVP)

This epic covers all functionality related to user accounts, from creation to session management.

### User Stories

-   **Story 2.1:** As a new user, I want to sign up with my email and password so that I can create a secure, personal account. (MVP)
    *   **FR/NFRs:** FR-1
    *   **Acceptance Criteria:**
        *   A registration form allows users to enter email and password.
        *   Passwords are securely hashed and salted before storage (NFR-5).
        *   New user accounts are successfully created and stored in the database.
        *   Appropriate error messages are displayed for invalid input (e.g., email format, password strength).

-   **Story 2.2:** As a registered user, I want to log in with my credentials so that I can access my study materials. (MVP)
    *   **FR/NFRs:** FR-2
    *   **Acceptance Criteria:**
        *   A login form allows users to enter email and password.
        *   Successful login redirects the user to their dashboard.
        *   Invalid credentials display an appropriate error message.

-   **Story 2.3:** As an authenticated user, I want to remain logged in between sessions so that I don't have to enter my credentials every time I visit. (MVP)
    *   **FR/NFRs:** FR-3
    *   **Acceptance Criteria:**
        *   User sessions persist across browser sessions (e.g., using secure tokens).
        *   The user is automatically logged in upon returning to the application within the session duration.

-   **Story 2.4:** As a logged-in user, I want to log out from a profile menu so that I can securely end my session. (MVP)
    *   **FR/NFRs:** FR-2
    *   **Acceptance Criteria:**
        *   A logout option is available in the user's profile or navigation menu.
        *   Clicking logout invalidates the current session and clears user authentication tokens.
        *   User is redirected to the login/landing page after logging out.

-   **Story 2.5:** As a user, I want to see clear error messages if my login or sign-up fails (e.g., "Invalid password") so that I can correct my input. (MVP)
    *   **FR/NFRs:** Implicitly supports FR-1, FR-2
    *   **Acceptance Criteria:**
        *   Specific error messages are displayed for common login/signup failures (e.g., "Email already registered," "Incorrect password," "Invalid email format").
        *   Error messages are user-friendly and actionable.

---

## Epic 3: Course and Note Management (MVP)

This epic covers the creation, organization, and manipulation of courses and lecture notes.

### User Stories

-   **Story 3.1:** As a student, I want to see a "Create New Course" button on my dashboard so that I can easily start organizing my materials. (MVP)
    *   **FR/NFRs:** FR-4, FR-6
    *   **Acceptance Criteria:**
        *   A clearly visible "Create New Course" button exists on the user dashboard.
        *   Clicking the button initiates the course creation workflow.

-   **Story 3.2:** As a student, I want to create a new course with a title and an optional description so that I can group my notes by subject. (MVP)
    *   **FR/NFRs:** FR-4
    *   **Acceptance Criteria:**
        *   A form allows input for course title (required) and description (optional).
        *   Successfully created courses appear in the user's course list.
        *   Course titles must be unique for a given user.

-   **Story 3.3:** As a student, I want to view a list of all my courses on the dashboard so that I have a clear overview and can navigate easily. (MVP)
    *   **FR/NFRs:** FR-6
    *   **Acceptance Criteria:**
        *   The dashboard displays a scrollable list of all courses created by the user.
        *   Each course entry shows its title and description (if available).
        *   Clicking on a course entry navigates to the course-specific page.

-   **Story 3.4:** As a student, I want to edit a course's title and description so that I can keep the information up to date. (MVP)
    *   **FR/NFRs:** FR-4
    *   **Acceptance Criteria:**
        *   An "Edit Course" option is available for each course.
        *   The edit form pre-populates with current course data.
        *   Changes to title and description can be saved and are reflected immediately.

-   **Story 3.5:** As a student, I want to delete a course (with a confirmation modal) so that I can remove subjects I am no longer studying. (MVP)
    *   **FR/NFRs:** FR-4
    *   **Acceptance Criteria:**
        *   A "Delete Course" option is available.
        *   Attempting to delete a course triggers a confirmation modal asking for user verification.
        *   Upon confirmation, the course and all associated notes and quizzes are permanently deleted.

-   **Story 3.6:** As a student, I want to add a lecture note with a title and content to a specific course so that I can capture my study material. (MVP)
    *   **FR/NFRs:** FR-5
    *   **Acceptance Criteria:**
        *   A "Create New Note" option is available within a course page.
        *   A form allows input for note title (required) and content (text area).
        *   Successfully created notes appear in the list for that course.

-   **Story 3.7:** As a student, I want to view and edit the content of an existing lecture note so that I can make corrections or additions. (MVP)
    *   **FR/NFRs:** FR-5
    *   **Acceptance Criteria:**
        *   Clicking on a note title or an "Edit" option opens the note for viewing/editing.
        *   The note editor displays current title and content.
        *   Changes to note title or content can be saved and are reflected immediately.

-   **Story 3.8:** As a student, I want to delete a lecture note (with confirmation) so that I can remove irrelevant information. (MVP)
    *   **FR/NFRs:** FR-5
    *   **Acceptance Criteria:**
        *   A "Delete Note" option is available for each note.
        *   A confirmation modal appears before permanent deletion.
        *   Upon confirmation, the note and any associated quizzes are permanently deleted.

---

## Epic 4: AI-Powered Quiz Generation (MVP)

This epic focuses on the core AI functionality of generating, displaying, and managing quizzes.

### User Stories

-   **Story 4.1:** As a student, I want to trigger a quiz generation from a single lecture note so that I can test my knowledge on that specific topic. (MVP)
    *   **FR/NFRs:** FR-8
    *   **Acceptance Criteria:**
        *   A "Generate Quiz" button is available on each individual lecture note page.
        *   Clicking the button initiates the quiz generation process for that note.

-   **Story 4.2:** As a student, I want the ability to generate a single quiz from all lecture notes within a course so that I can have a comprehensive review of the subject. (MVP)
    *   **FR/NFRs:** FR-9
    *   **Acceptance Criteria:**
        *   A "Generate Course Quiz" button is available on the course page.
        *   Clicking the button initiates quiz generation using all notes within that course.

-   **Story 4.3:** As a student, I want the "Generate Course Quiz" button to be disabled if there are fewer than two notes, so that I understand why I can't generate a quiz yet. (MVP)
    *   **FR/NFRs:** Implies FR-9
    *   **Acceptance Criteria:**
        *   The "Generate Course Quiz" button is visibly disabled if the course contains less than two notes.
        *   A tooltip or message explains the reason for disability (e.g., "Requires at least two notes").

-   **Story 4.4:** As a student, I want to see a loading indicator while a quiz is being generated so that I have feedback that the system is working. (MVP)
    *   **FR/NFRs:** FR-10
    *   **Acceptance Criteria:**
        *   A visible loading indicator (spinner, progress bar) appears during quiz generation.
        *   The loading indicator disappears upon completion or error.

-   **Story 4.5:** As a student, I want to view a generated quiz in a clean, readable format with multiple-choice questions and a separate answer key at the bottom. (MVP)
    *   **FR/NFRs:** FR-12, FR-13, FR-14, FR-15
    *   **Acceptance Criteria:**
        *   Generated quizzes are displayed in a structured markdown format.
        *   Lecture quizzes contain exactly 10 questions and course quizzes exactly 20 questions.
        *   Each question has four answer options, only one correct.
        *   A "Correct Answers" section is clearly displayed at the end of the quiz.

-   **Story 4.6:** As a student, I want to be prompted to replace an existing quiz if I try to generate a new one for the same note, so I don't lose work accidentally. (MVP)
    *   **FR/NFRs:** FR-11
    *   **Acceptance Criteria:**
        *   If a quiz already exists for a note/course, a confirmation modal appears when generating a new one.
        *   The modal offers options to "Replace" or "Cancel."

-   **Story 4.7:** As a student, I want to copy the full content of a quiz to my clipboard so that I can easily use it in other applications or print it. (MVP)
    *   **FR/NFRs:** FR-16
    *   **Acceptance Criteria:**
        *   A "Copy Quiz" button or similar function is available on the quiz view page.
        *   Clicking the button copies the entire quiz text (questions and answers) to the clipboard.
        *   A success message (e.g., "Copied to clipboard!") is displayed.

-   **Story 4.8:** As a student, I want the option to delete a generated quiz so that I can keep my workspace clean. (MVP)
    *   **FR/NFRs:** FR-17
    *   **Acceptance Criteria:**
        *   A "Delete Quiz" option is available on the quiz view page or list view.
        *   A confirmation modal appears before permanent deletion.
        *   Upon confirmation, the quiz is permanently removed.

---

## Epic 5: Quiz Interaction & Presentation (MVP/Growth)

This epic provides the user-facing functionality for viewing, using, and managing the generated quizzes in a clean and structured format.

### User Stories

-   **Story 5.1:** As a student, I want to access a list of all my previously generated quizzes, so that I can easily find and retake them. (MVP)
    *   **FR/NFRs:** FR-12a
    *   **Acceptance Criteria:**
        *   A dedicated section or page lists all quizzes generated by the user.
        *   Each entry in the list clearly identifies the quiz (e.g., by source note/course and generation date).
        *   Clicking a quiz in the list navigates to its view/interaction page.

-   **Story 5.2:** As a student, I want to view a generated quiz in a dedicated quiz-taking interface, so that I can attempt the questions interactively. (Growth)
    *   **FR/NFRs:** FR-18
    *   **Acceptance Criteria:**
        *   Quizzes can be opened in an interactive interface, distinct from the static markdown view.
        *   The interface presents one question at a time or allows easy navigation between questions.

-   **Story 5.3:** As a student, I want to select an answer for each multiple-choice question within the quiz interface, so that I can test my knowledge. (Growth)
    *   **FR/NFRs:** FR-19
    *   **Acceptance Criteria:**
        *   Each question in the interactive interface allows selection of one of the four options.
        *   The selected answer is clearly indicated.

-   **Story 5.4:** As a student, I want to submit my answers and receive immediate feedback on whether my answers are correct or incorrect, so that I can learn from my mistakes. (Growth)
    *   **FR/NFRs:** FR-20
    *   **Acceptance Criteria:**
        *   Upon submitting an answer (per question or at end), immediate visual feedback is provided (e.g., green for correct, red for incorrect).
        *   The correct answer is clearly indicated for incorrect responses.

-   **Story 5.5:** As a student, I want to see a summary of my quiz results (e.g., score, number of correct/incorrect answers) after completing a quiz, so that I can track my progress. (Growth)
    *   **FR/NFRs:** FR-21
    *   **Acceptance Criteria:**
        *   After completing an interactive quiz, a summary screen displays the user's score.
        *   The summary includes the number of correct, incorrect, and unanswered questions.

-   **Story 5.6:** As a student, I want to have the option to review the correct answers for a quiz after completing it, so that I can reinforce my learning. (Growth)
    *   **FR/NFRs:** Implies FR-15
    *   **Acceptance Criteria:**
        *   A "Review Answers" option is available on the quiz results summary.
        *   The review mode clearly shows each question, the user's answer, and the correct answer.

-   **Story 5.7:** As a student, I want to mark a quiz as "completed" or "mastered" so that I can keep track of my study progress. (Growth)
    *   **FR/NFRs:** Implies FR-21
    *   **Acceptance Criteria:**
        *   Users can mark quizzes with a status (e.g., "Completed," "Mastered," "Needs Review").
        *   The status is visible in the quiz list or on the quiz detail page.

---

## Epic 6: Accessibility Compliance (MVP)

This epic ensures the application is usable, intuitive, and accessible to all users across different devices.

### User Stories

-   **Story 6.1:** As a user, I want the application to be fully responsive so that I can have a seamless experience on both my desktop and mobile devices. (MVP)
    *   **FR/NFRs:** NFR-7
    *   **Acceptance Criteria:**
        *   The UI adapts correctly to various screen sizes (desktop, tablet, mobile).
        *   All elements are visible and interactive on different devices without horizontal scrolling.

-   **Story 6.2:** As a user with visual impairments, I want to be able to navigate and use the entire application with a screen reader (e.g., VoiceOver) so that I can access all features. (MVP)
    *   **FR/NFRs:** NFR-10
    *   **Acceptance Criteria:**
        *   All UI elements have appropriate ARIA labels and roles.
        *   Content is logically structured for screen reader interpretation.
        *   Major workflows (e.g., creating notes, generating quizzes) are fully operable via screen reader.

-   **Story 6.3:** As a keyboard user, I want all interactive elements (buttons, links, inputs) to have a visible focus state so that I always know where I am on the page. (MVP)
    *   **FR/NFRs:** NFR-9
    *   **Acceptance Criteria:**
        *   All interactive elements display a clear visual focus indicator when tab-navigated.
        *   Keyboard focus moves logically through the page content.

-   **Story 6.4:** As a user, I want to interact with a clean, minimalist UI so that I can focus on my studies without distraction. (MVP)
    *   **FR/NFRs:** NFR-8 (partially, by contributing to usability)
    *   **Acceptance Criteria:**
        *   The design adheres to minimalist principles, reducing visual clutter.
        *   No intrusive ads or unnecessary animations are present.

-   **Story 6.5:** As a user, I want to see the dashboard automatically refresh after I create new content (like a course or note) so that my view is always up-to-date. (MVP)
    *   **FR/NFRs:** Implies a smooth user experience as per NFR-1, NFR-2
    *   **Acceptance Criteria:**
        *   Upon successful creation of a course or note, the relevant list (dashboard, course page) updates without requiring a manual page refresh.

-   **Story 6.6:** As a user, I want the UI to have a consistent and logical layout (e.g., navigation, headings) so that I can easily find my way around the application. (MVP)
    *   **FR/NFRs:** Implies NFR-8 (usability aspect)
    *   **Acceptance Criteria:**
        *   Navigation menus, headers, footers, and content areas maintain consistent positioning and styling across the application.
        *   Heading structures (H1, H2, etc.) are used semantically and consistently.

