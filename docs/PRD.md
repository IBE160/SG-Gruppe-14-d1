# IBE160 - Product Requirements Document

**Author:** BIP
**Date:** 20. november 2025
**Version:** 1.0

---

## Executive Summary

AI Study Buddy is a minimalist, AI-powered web application designed to help students improve their study efficiency by generating multiple-choice quizzes from their own notes. By automating the time-consuming process of creating study materials, the application provides a structured and distraction-free environment for effective learning.

### What Makes This Special

By automating the time-consuming process of creating study materials, the application provides a structured and distraction-free environment for effective learning.

---

## Project Classification

**Technical Type:** Web Application (SPA)
**Domain:** Education Technology
**Complexity:** Medium

This project is a Medium-complexity Web Application (SPA) in the Education Technology domain.

### Domain Context

The application operates within the Education Technology (EdTech) space, specifically targeting self-directed learning and study efficiency. The core pedagogical principle is **active recall**, facilitated by auto-generated quizzes. The context is defined by a minimalist, distraction-free environment, contrasting with feature-heavy educational tools. The primary goal is to automate the tedious task of creating study materials, allowing students to focus on structured and consistent review.


---

## Success Criteria

Success for the AI Study Buddy means:
- **Core functionality is flawless:** Users can seamlessly create accounts, manage their notes, and generate relevant, high-quality quizzes without issues.
- **It just works:** Data persists reliably across sessions, and the application is fully responsive on both desktop and mobile.
- **It's accessible to everyone:** The application is fully usable with screen readers, meeting our accessibility goals from day one.
- **Users are engaged:** We see users not just trying the app, but creating multiple notes and generating quizzes, indicating they find real value in the core loop.

### Business Metrics

- **Weekly Active Users (WAU):** How many unique users engage with the app each week?
- **Core Feature Adoption:** What percentage of users generate at least one quiz within their first week?
- **User Retention:** What percentage of users return to the app a week after signing up?

---

## Product Scope

### MVP - Minimum Viable Product

-   **User Registration & Authentication:** Securely create and log into accounts.
-   **Lecture Note Management:** Full Create, Read, Update, Delete (CRUD) for notes.
-   **Quiz Management:** Create and delete quizzes generated from notes.
-   **Basic Quiz Listing:** A simple, single list view for all generated quizzes.
-   **Core Accessibility:** Foundational support for screen readers.

### Growth Features (Post-MVP)

-   **Expanded Content Generation:** Create flashcards, summaries, and keywords from notes.
-   **Advanced Organization:** Implement folder and tag-based organization for notes and quizzes.
-   **Search & Filtering:** Allow users to quickly find materials.
-   **Analytics:** Introduce a progress tracking dashboard to monitor study habits and performance.

### Vision (Future)

-   **AI Chat Study Companion:** An interactive chat interface for asking questions about study materials.
-   **Spaced Repetition System (SRS):** An intelligent algorithm to schedule reviews for optimal long-term retention.
-   **Gamification:** Introduce elements like score sharing and study streaks to boost motivation.

---

## Domain-Specific Requirements

- **Data Security:** All user data, including personal information and study notes, must be handled securely to ensure privacy and confidentiality. This will inform all architectural and implementation decisions.

---

## Web Application (SPA) Specific Requirements

The application will be a responsive Single-Page Application (SPA) built with a modern tech stack to ensure a fluid and seamless user experience.

### API Specification

The specific API endpoints, methods, and data schemas will be defined in detail during the architecture and implementation phases. The API will be designed to support the user flows outlined in the project proposal, including operations for managing users, notes, and quizzes.

### Authentication & Authorization

The application will feature a secure authentication system. Users will register and log in to access their personal study materials. The backend, built with FastAPI, will enforce strict, token-based access controls to ensure a user can only ever view and manage their own data.

### Platform Support

The frontend, built with Next.js, will be a responsive web application accessible on modern desktop and mobile web browsers. The UI will be optimized for a clean and intuitive experience on a wide range of screen sizes.

---

## User Experience Principles

- **Visual Vibe:** The design will be clean, modern, and professional, with a calm color palette. It will feel like a focused workspace, not a busy social media app.
- **Core Feel:** The user experience must be intuitive and seamless. Every action will be straightforward, minimizing cognitive load and allowing students to stay in their study flow.

### Key Interactions

- The central user journey—creating a note, generating a quiz, and reviewing the quiz—must be the most prominent and effortless workflow in the application.

---

## Functional Requirements

### User Account Management
- **FR-1:** Users must be able to create a new account using an email and password. (MVP)
- **FR-2:** Users must be able to log in to their account and log out. (MVP)
- **FR-3:** The system must persist user sessions, automatically logging them in on return visits. (MVP)

### Course & Note Management
- **FR-4:** Users must be able to create, read, update, and delete courses. Each course must have a title and an optional description. (MVP)
- **FR-5:** Users must be able to create, read, update, and delete lecture notes within a course. Each note consists of a title and text content. (MVP)
- **FR-6:** The dashboard must display a list of all user-created courses. (MVP)
- **FR-7:** The course page must display a list of all lecture notes associated with that course. (MVP)

### Quiz Generation
- **FR-8:** Users must be able to generate a multiple-choice quiz from the content of a single lecture note. (MVP)
- **FR-9:** Users must be able to generate a single multiple-choice quiz from the combined content of all notes within a course. This function is only enabled if the course contains at least two lecture notes. (MVP)
- **FR-10:** The system must provide a loading indicator while the AI is generating a quiz. (MVP)
- **FR-11:** If a quiz already exists for a note or course, the system must ask the user for confirmation before generating a new one to replace it. (MVP)

### Quiz Interaction
- **FR-12:** Generated quizzes must be displayed in a clean, readable, and structured format (e.g., using markdown). (MVP)
- **FR-12a:** Users must be able to view a simple, single list of all their generated quizzes. (MVP)
- **FR-13:** Lecture-level quizzes must contain exactly 10 questions, and course-level quizzes must contain exactly 20 questions. (MVP)
- **FR-14:** Each quiz question must be presented with four answer options, only one of which is correct. (MVP)
- **FR-15:** A separate "Correct Answers" section must be displayed at the end of the quiz, clearly listing the correct option for each question. (MVP)
- **FR-16:** Users must have an option to copy the entire quiz content (questions and answers) to their clipboard. (MVP)
- **FR-17:** Users must be able to delete a previously generated quiz. (MVP)
- **FR-18:** Users must be able to interact with a dedicated quiz-taking interface. (Growth)
- **FR-19:** Users must be able to submit their answers for each question within the quiz-taking interface. (Growth)
- **FR-20:** The system must provide immediate feedback on whether the submitted answer for each question is correct or incorrect. (Growth)
- **FR-21:** The system must track and display the user's progress within a quiz (e.g., questions answered, score). (Growth)

---

## Non-Functional Requirements

### Performance
- **NFR-1:** The application must maintain responsive performance and a fluid user experience, even when processing large text inputs for quiz generation. (MVP)
- **NFR-2:** API response times for core user actions (e.g., creating notes, generating quizzes) must be optimized to minimize wait times. (MVP)

### Security
- **NFR-3:** All user data, particularly personal information and note content, must be handled securely and encrypted in transit (TLS) and at rest. (MVP)
- **NFR-4:** The system must enforce strict authorization, ensuring a user can only access and manage their own data. (MVP)
- **NFR-5:** User authentication credentials (passwords) must be securely hashed and salted. (MVP)

### Scalability
- **NFR-6:** The backend architecture must be designed to scale efficiently to handle a growing user base and increasing data volume without degradation in performance. (MVP)

### Accessibility & Usability
- **NFR-7:** The application must be fully responsive, providing an optimal and consistent user experience on both desktop and mobile web browsers. (MVP)
- **NFR-8:** The application must comply with Web Content Accessibility Guidelines (WCAG) 2.1 Level AA standards. (MVP)
- **NFR-9:** All application features must be navigable and operable using only a keyboard. (MVP)
- **NFR-10:** The application must be compatible with modern screen readers (e.g., VoiceOver, NVDA) to ensure it is usable by visually impaired users. (MVP)

---

## Implementation Planning

### Epic Breakdown Required

Requirements must be decomposed into epics and bite-sized stories (200k context limit).

**Next Step:** Run workflow epics-stories to create the implementation breakdown.

---

## References

- Product Brief: [product-brief.md](product-brief.md)
- Technical Research: [technical-research-gemini-libraries-1. november 2025.md](technical-research-gemini-libraries-1. november 2025.md)
- User Research: [user-research-report-1. november 2025.md](user-research-report-1. november 2025.md)

---

## ✅ PRD Complete

Your product requirements are documented and ready for implementation.

**Created:**

- **PRD.md** - Complete requirements adapted to Web Application (SPA) and Education Technology

### Next Steps

1.  **Epic Breakdown** (Required)
    Run: workflow create-epics-and-stories to decompose requirements into implementable stories

2.  **UX Design** (If UI exists)
    Run: workflow ux-design for detailed user experience design

3.  **Architecture** (Recommended)
    Run: workflow create-architecture for technical architecture decisions

---

_The magic of your product - automating the creation of study materials to provide a structured, distraction-free learning environment - is woven throughout the PRD and will guide all subsequent work._

_Created through collaborative discovery between BIP and AI facilitator._
