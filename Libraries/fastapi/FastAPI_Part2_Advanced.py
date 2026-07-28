# ============================================================
# FASTAPI PART 2: ADVANCED TOPICS (Routing, Dependencies, Files)
# ============================================================
# This file covers advanced FastAPI concepts, including:
# 1. APIRouter for organizing larger applications
# 2. Dependencies (Dependency Injection)
# 3. File Uploads and Form Data
# 4. Background Tasks
#
# To run this file:
# uvicorn FastAPI_Part2_Advanced:app --reload
# ============================================================

from fastapi import FastAPI, APIRouter, Depends, HTTPException, File, UploadFile, Form, BackgroundTasks
from pydantic import BaseModel
import time

app = FastAPI(title="FastAPI Advanced", description="Advanced routing and dependencies")

# ============================================================
# 1. API ROUTER
# ============================================================
# APIRouter is used to group related routes together, often in 
# separate files in real projects, to keep the codebase clean.

users_router = APIRouter(prefix="/users", tags=["Users"])

@users_router.get("/")
def get_users():
    return [{"username": "alice"}, {"username": "bob"}]

@users_router.get("/{username}")
def get_user(username: str):
    return {"username": username, "status": "active"}

# Include the router in the main app
app.include_router(users_router)


# ============================================================
# 2. DEPENDENCY INJECTION
# ============================================================
# Dependencies allow you to extract common logic (like checking
# authentication, getting a DB connection, or parsing common params).

def common_parameters(q: str = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}

@app.get("/items/")
def read_items(commons: dict = Depends(common_parameters)):
    """This endpoint automatically receives the result of `common_parameters`"""
    return {"message": "Dependencies work!", "params": commons}

# A simple authentication dependency
def verify_token(x_token: str = "supersecret"):
    if x_token != "supersecret":
        raise HTTPException(status_code=400, detail="X-Token header invalid")
    return True

@app.get("/secure-data/", dependencies=[Depends(verify_token)])
def read_secure_data():
    return {"data": "This is highly classified information."}


# ============================================================
# 3. FILE UPLOADS & FORM DATA
# ============================================================
# Requires installing `python-multipart`: pip install python-multipart

@app.post("/login/")
def login(username: str = Form(...), password: str = Form(...)):
    """Receives data as form fields instead of JSON."""
    return {"username": username, "status": "logged in"}

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    """Handles file uploads."""
    # You can read the file contents asynchronously
    contents = await file.read()
    return {
        "filename": file.filename, 
        "content_type": file.content_type, 
        "size_bytes": len(contents)
    }


# ============================================================
# 4. BACKGROUND TASKS
# ============================================================
# Background tasks run after returning a response to the client.
# Useful for sending emails, processing data, etc.

def write_notification(email: str, message=""):
    time.sleep(3) # Simulate a slow task (e.g. sending an email)
    with open("log.txt", mode="a") as email_file:
        content = f"notification for {email}: {message}\n"
        email_file.write(content)

@app.post("/send-notification/{email}")
def send_notification(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_notification, email, message="Your account is ready!")
    return {"message": "Notification sent in the background"}

