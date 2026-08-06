from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import database
import schemas
import pandas as pd
import joblib
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from Python.Logging_Config import setup_logger

logger = setup_logger("API_Database_Project")

# Create the database tables
database.Base.metadata.create_all(bind=database.engine)
logger.info("Database tables initialized.")

app = FastAPI(title="Bookstore API", description="A simple CRUD API with Database integration")

# Load the trained machine learning model
MODEL_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'ML_Project', 'titanic_rf_model.joblib'))
ml_model = None
try:
    ml_model = joblib.load(MODEL_PATH)
    logger.info("ML model loaded successfully.")
except FileNotFoundError:
    logger.warning(f"ML model not found at {MODEL_PATH}. Prediction endpoint will not work until model is trained.")


# Dependency to get the database session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/books/", response_model=schemas.Book, status_code=201)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    logger.info(f"Creating book: {book.title}")
    db_book = database.Book(**book.model_dump())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

@app.get("/books/", response_model=list[schemas.Book])
def read_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    books = db.query(database.Book).offset(skip).limit(limit).all()
    return books

@app.get("/books/{book_id}", response_model=schemas.Book)
def read_book(book_id: int, db: Session = Depends(get_db)):
    logger.info(f"Fetching book id: {book_id}")
    book = db.query(database.Book).filter(database.Book.id == book_id).first()
    if book is None:
        logger.warning(f"Book id {book_id} not found")
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@app.post("/predict")
def predict_survival(passenger: schemas.Passenger):
    if ml_model is None:
        raise HTTPException(status_code=503, detail="ML model is not available")
    
    # Convert payload to DataFrame for the model
    passenger_df = pd.DataFrame([passenger.model_dump()])
    
    # Predict
    prediction = ml_model.predict(passenger_df)
    survived = bool(prediction[0] == 1)
    
    return {"survived": survived}
