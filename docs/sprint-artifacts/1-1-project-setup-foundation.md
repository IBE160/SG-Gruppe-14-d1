# Story 1.1: Project Setup & Foundation

Status: ready-for-dev

## Story

As a **developer**,
I want **a standardized project structure and build system**,
so that **I can begin development efficiently**.

## Acceptance Criteria

1.  **Given** the project repository is cloned
    **When** I run the project setup script
    **Then** the required dependencies for the Next.js frontend and FastAPI backend are installed.
2.  **Given** the project repository is cloned
    **When** I run the project setup script
    **Then** the basic folder structure for frontend (`/app`) and backend (`/api`) is created.
3.  **Given** the project repository is cloned
    **When** I run the project setup script
    **Then** a basic CI/CD pipeline is configured to run tests on push.

## Tasks / Subtasks

- [ ] Initialize Next.js project in `/app` (AC: 1, 2)
  - [ ] `npx create-next-app@latest app`
  - [ ] Configure `package.json`
- [ ] Set up FastAPI project in `/api` (AC: 1, 2)
  - [ ] Create `api/` directory
  - [ ] Initialize `pyproject.toml`
  - [ ] Install FastAPI, Uvicorn, Pydantic
- [ ] Configure basic CI/CD pipeline (AC: 3)
  - [ ] Create `.github/workflows/main.yml`
  - [ ] Add basic test commands for frontend and backend
- [ ] Document project setup steps in `README.md`

## Dev Notes

### Relevant architecture patterns and constraints
- **Monorepo Structure:** `/app` for Next.js (frontend), `/api` for FastAPI (backend). [Source: `docs/architecture.md#2-scaffolding-&-project-initialization`]
- **Core Libraries:** Next.js, React, FastAPI, Uvicorn, Pydantic. [Source: `docs/epics.md#story-1.1-project-setup-foundation`]

### Source tree components to touch
- Project root: `.gitignore`, `README.md`
- Frontend: `/app/`, `package.json`
- Backend: `/api/`, `pyproject.toml`
- CI/CD: `.github/workflows/`

### Testing standards summary
- Initial CI/CD will include placeholder tests. [Source: `docs/epics.md#story-1.1-project-setup-foundation`]
- Further test strategy defined in Tech Spec for Epic 1, including Unit, Integration, and E2E tests with GitHub Actions. [Source: `docs/sprint-artifacts/tech-spec-epic-1.md#test-strategy-summary`]

### Project Structure Notes

- **Frontend (`/app`):** `npx create-next-app@latest` will scaffold the basic Next.js structure.
- **Backend (`/api`):** Manual setup will ensure a clean FastAPI project, separate from the Next.js structure.

### References

- `docs/epics.md#story-1.1-project-setup-foundation`
- `docs/architecture.md#2-scaffolding-&-project-initialization`
- `docs/sprint-artifacts/tech-spec-epic-1.md`

## Dev Agent Record

### Context Reference

- docs/sprint-artifacts/1-1-project-setup-foundation.context.xml

### Agent Model Used

Gemini

### Debug Log References

### Completion Notes List

### File List

## Change Log
- **2025-11-28**: Story drafted.
