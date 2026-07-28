# ============================================================
# FASTAPI PART 3: DATABASE INTEGRATION (SQLAlchemy)
# ============================================================
# This file demonstrates how to connect a FastAPI application 
# to a SQL database (SQLite in this case) using SQLAlchemy.
#
# Requirements:
# pip install fastapi uvicorn sqlalchemy
#
# To run this file:
# uvicorn FastAPI_Part3_Database:app --reload
# ============================================================

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel

# ============================================================
# 1. DATABASE SETUP (SQLAlchemy)
# ============================================================

# SQLite database URL (creates a file named 'app.db' in the same folder)
SQLALCHEMY_DATABASE_URL = "sqlite:///./app.db"

# Create the SQLAlchemy engine
# connect_args={"check_same_thread": False} is needed only for SQLite
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Create a SessionLocal class. Each instance will be a database session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for our database models
Base = declarative_base()

# ============================================================
# 2. DATABASE MODELS
# ============================================================

class DBUser(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)

# Create the tables in the database
Base.metadata.create_all(bind=engine)


# ============================================================
# 3. PYDANTIC SCHEMAS (For request/response validation)
# ============================================================

class UserCreate(BaseModel):
    email: str

class UserResponse(BaseModel):
    id: int
    email: str
    is_active: bool

    class Config:
        orm_mode = True # Tells Pydantic to read data even if it's not a dict (like an ORM model)


# ============================================================
# 4. FASTAPI APP & DEPENDENCIES
# ============================================================

app = FastAPI(title="FastAPI with Database")

# Dependency to get the DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ============================================================
# 5. API ENDPOINTS
# ============================================================

@app.post("/users/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    """Create a new user in the database."""
    # Check if user already exists
    db_user = db.query(DBUser).filter(DBUser.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Create the new user instance
    new_user = DBUser(email=user.email)
    
    # Add to DB session, commit, and refresh (to get the generated ID)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user

@app.get("/users/", response_model=list[UserResponse])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Retrieve a list of users from the database."""
    users = db.query(DBUser).offset(skip).limit(limit).all()
    return users

@app.get("/users/{user_id}", response_model=UserResponse)
def read_user(user_id: int, db: Session = Depends(get_db)):
    """Retrieve a specific user by ID."""
    user = db.query(DBUser).filter(DBUser.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
