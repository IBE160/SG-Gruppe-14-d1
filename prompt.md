## Case Title 
AI Study Buddy

## Background

Students often struggle to efficiently process large volumes of study material, such as lecture notes, textbooks, and digital files. Manually creating quizzes (and similar study materials) is time-consuming, and only a small number of students consistently take the time to do it. As a result, many lack structure and discipline in how they review and engage with their materials. There is a clear need for a tool that helps students become more organized and consistent in their study routines.

## Purpose

This application provides students with AI-generated quizzes from the students input (text). It focuses on improving efficiency and supporting more structured learning by offering a focused, minimalistic environment. Unlike many educational tools overloaded with unnecessary features, this product will include only a carefully crafted set of core functions designed to directly support the learning process by generating material into quizzes. The goal is to make studying more effective, organized, and distraction-free.

## Target Users

The primary users of this application are students who want to organize their study materials and improve the efficiency of their learning process.

## Core Functionality

### Must Have (MVP)

- User registration and authentication: Allow users to create accounts, log in, and securely manage their study materials.
- Lecture notes management (CRUD): Create, read, update and delete lecture notes. 
- Quiz management (CRD): Create, read and delete quizzes generated from lecture notes.
- Basic quiz listing: Users can view all quizzes in a single list view. 
- Allows students to type or paste content into a single note field for each lecture.
- Assistive technology support: Ensure accessibility through screen reader compatibility and clear UI design that is consistent.

### Nice to Have (Optional Extensions)

- Flashcards, summaries and key word extractions: generate flashcards, summaries and keywords from the provided input. 
- Folder organization: Group flashcards and quizzes into folders for improved structure and navigation.
- Search and filtering: Allow users to search by title, content, or tags for faster access to materials.
- AI Chat Study Companion: A chatbot interface that allows students to ask questions about their uploaded notes (e.g., _"Explain this topic again"_, _"Give me three quiz questions about this section"_). Optionally, users can connect their own OpenAI or Anthropic API key for higher-quality results.
- Tag-based organization: Add tags to flashcards and quizzes to provide an additional way of categorizing and filtering study materials.
- Progress tracking: Monitor which topics a user has studied and how they performed on quizzes over time.
- Statistics dashboard: Display an overview of user activity, such as the total number of flashcards, quizzes, folders, and tags in their account.
- Spaced Repetition System (SRS): Implement an algorithm that schedules flashcard reviews at optimal intervals to improve long-term retention, similar to the approach used in Anki.
- Keyboard shortcuts: Allow users to navigate the interface and perform common actions (e.g., flipping flashcards, starting quizzes, saving notes) directly from the keyboard to improve accessibility and study flow.
- Score system and sharing: Implement a scoring mechanism for quizzes, allowing users to compare and share their results with friends to stay motivated.
- Streak tracking: Display a streak indicator showing how many consecutive days a user has studied or completed quiz/flashcard sessions, promoting consistent study habits.
- File upload and summarization: Users can upload notes in supported formats (TXT, PDF, or DOCX — up to 10 MB per file, text-based PDFs only) and generate concise, structured summaries using an AI model. Longer documents are automatically chunked into smaller sections to stay within token limits, ensuring quick and consistent summarization. Scanned image-only PDFs are excluded in the MVP to simplify scope.


## Data Requirements

- Users: name, email, password (securely hashed), account creation date, and optionally API key for connecting external AI services.
- Lecture notes: user ID, text content, creation date, and last updated date.
- Quizzes: input, questions, possible answers, correct answers, creation date.

## User Stories 

- The student start the application by creating account and logging in. When the student logs in, they land on the dashboard, where they can view all their existing courses and create new ones. After selecting a course, the student is taken to the course page, where they can see all lecture notes associated with that course, modify or delete the course, create new lecture notes by providing a title and date, and immediately see which notes already have an associated quiz. From this page, the student can also generate a course-level quiz that combines all lecture notes, which opens in a new page once generated.
When the student selects a specific lecture note, they are taken to the lecture note page, where they can view the note content, edit and save any changes, or delete the note entirely. They can also see whether a quiz has already been generated for that note and when it was last created. If no quiz exists, they can generate one; if one already exists, they may choose to replace it with a newly generated version. Once generated, the student can open the quiz in a separate page.
On the quiz page, the student can read the quiz in markdown format, delete it if needed, copy the quiz content for study purposes, and navigate back to the corresponding note or course page.


## Technical Constraints

- Gemini CLI: The entire application will be developed using the Gemini Command-Line Interface. Gemini CLI provides full AI-assisted support for code generation, refinement, testing, and execution, ensuring consistent integration across all project components.
- Must be responsive and function properly on both desktop and mobile devices.
- Platform: responsive web application (SPA)--not a PWA--built with Next.js (frontend) and FastAPI (backend).
- Must include user authentication to access personalized content and data.
- Must support accessibility features, including screen reader compatibility. VoiceOver on Apple platforms will be used for testing purposes.
- Must handle entered text securely and restrict access to each user's data.
- Should maintain reasonable performance even when processing large text input.
- The MVP intentionally excludes advanced features such as file upload, folder organization, search, and chatbot interaction to ensure a focused, achievable implementation within the 1.5-month timeframe.

## Frontend Specification

- Framework: Next.js 
- UI & Styling: Tailwind CSS
- Accessibility: WCAG 2.1 AA targets. Landmarks (`main`, `nav`), proper heading hierarchy, visible focus rings, keyboard navigation, and ARIA labels.

## Backend Specification

- Framework: Python UV.
- FastAPI.
- Database: Supabase.


## Deployment & Hosting

- Default: Local-only—for a small scope and identical behavior on both collaborators’ machines.


## AI Integration

We use Gemini 2.5 pro via the Gemini API as our primary model for quiz generation. This gives us a single hosted endpoint with consistent behavior across collaborators—no local GPU or setup beyond an API key.

- Tasks: Generate multiple-choice quizzes from entered text.
- Prompts & outputs: Task-specific prompts for quizzes. Return multiple-choice items as JSON with a question, an options array, and a correct answer index. Sampling temperature is configurable, and max_output_tokens caps response length.
- Reliability: If JSON parsing fails, we reprompt once and validate responses (Zod/Pydantic) before returning results.


## Success Criteria

- Users can create an account, log in, and securely manage their study materials.
- Users can input text and generate AI-powered quizzes successfully.
- AI-generated quizzes are relevant, accurate, and aligned with the input.
- Users can create, edit, and delete courses/lecture notes.
- Users can create and delete quizzes. 
- Data persists across sessions (users' materials and progress are saved).
- The application works with screen readers.
- The interface is responsive and functions properly on both desktop and mobile devices.

## Timeline and Milestones (6 Weeks)

The team uses BMAD to generate the Study Buddy application. 
If the team stays ahead of schedule we move to the next step, and some “Nice to Have” features may then be implemented before week 6.

### Week 1 – Proposal.md

Goals

- The proposal.md file is reviewed and considered finished. 

Deliverables

- Proposal.md is finished and can be used throughout the BMAD process. 

### Week 2 – Phase 1 analyze and phase 2 planning 

Goals

- The proposal.md file is put into Gemini CLI, the first step is for the analyst to read the proposal. 
- Project manager works on making a product reqirements documents PRD. 

Deliverables

- The analytic make a project brief.md based on the input from proposal.md.  
- The project manager make a PRD.md. 

### Week 3 – Phase 3 architecture 

Goals

- The agents architect and UX/UI designer are at work on their tasks.

Deliverables

- Solution-architecture.md
- ux-specification.md
- frontend-promt.md

### Week 4 – Phase 3 architecture 

Goals

- The agents architect and UX/UI designer are at work on their tasks.  

Deliverables

- Solution-architecture.md
- ux-specification.md
- frontend-promt.md

### Week 5 – Phase 4 implementation

Goals

- Epic based development.
- Just in time JIT principles. 

Deliverables

- Epic is developed.

### Week 6 – Phase 4 implementation

Goals

- Epic based development. 
- Just in time JIT principles. 

Deliverables

- Fully functional web app meeting all success criteria
- Accessibility verified for final submission

Milestone: All MVPs working and final testing complete.
