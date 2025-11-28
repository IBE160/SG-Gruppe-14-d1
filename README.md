# SG-Gruppe-14-d1
Repository for SG-Gruppe-14-d1 - IBE160 Programmering med KI.

## Project Setup

This project consists of a Next.js frontend (`app/`) and a FastAPI backend (`api/`), structured as a monorepo.

### Prerequisites

*   Node.js (LTS version recommended)
*   Python 3.11+
*   npm (usually comes with Node.js)
*   pip (usually comes with Python)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/IBE160/SG-Gruppe-14-d1.git
    cd SG-Gruppe-14-d1
    ```

2.  **Frontend Setup:**
    Navigate to the `app` directory and install dependencies:
    ```bash
    cd app
    npm install
    cd ..
    ```

3.  **Backend Setup:**
    Navigate to the `api` directory and install dependencies:
    ```bash
    cd api
    pip install -r requirements.txt
    cd ..
    ```
    *Note: A virtual environment is recommended for Python projects to manage dependencies.*

### Running the Application (Development)

*   **Frontend:**
    ```bash
    cd app
    npm run dev
    ```
    The frontend will be accessible at `http://localhost:3000` (or similar).

*   **Backend:**
    ```bash
    cd api
    uvicorn main:app --reload
    ```
    The backend API will be accessible at `http://localhost:8000` (or similar).
    *(Note: You will need a `main.py` file with a FastAPI app instance for this to work.)*

### CI/CD

A basic CI/CD pipeline is configured using GitHub Actions. It will lint and build the frontend, and install backend dependencies on `push` and `pull_request` events to the `main` branch. See `.github/workflows/main.yml` for details.