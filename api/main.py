from fastapi import FastAPI
from v1.endpoints import auth

app = FastAPI(title="AI Study Buddy API")

app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the AI Study Buddy API"}
