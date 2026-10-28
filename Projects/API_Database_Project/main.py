import json
import logging
import os
import sys
from fastapi import Depends, FastAPI, HTTPException, status
import joblib
import pandas as pd
from sqlalchemy import text
from sqlalchemy.orm import Session

import database
import schemas

try:
    sys.path.append(
        os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    )
    from Python.Logging_Config import setup_logger

    logger = setup_logger("API_Database_Project")
except (ImportError, ModuleNotFoundError):
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    logger = logging.getLogger("API_Database_Project")

# Create the database tables
database.Base.metadata.create_all(bind=database.engine)
logger.info("Database tables initialized.")

app = FastAPI(
    title="Bookstore & ML API",
    description="Full CRUD Bookstore API integrated with Titanic ML Predictions",
    version="1.1.0",
)


# Path resolver for ML model
def find_model_path():
    candidate_paths = [
        os.environ.get("MODEL_PATH"),
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__), "..", "ML_Project", "titanic_rf_model.joblib"
            )
        ),
        os.path.abspath(
            os.path.join(os.path.dirname(__file__), "titanic_rf_model.joblib")
        ),
        "/app/models/titanic_rf_model.joblib",
    ]
    for path in candidate_paths:
        if path and os.path.exists(path):
            return path
    return candidate_paths[1]


# Path resolver for ML metrics metadata
def find_metrics_path():
    candidate_paths = [
        os.environ.get("METRICS_PATH"),
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__), "..", "ML_Project", "model_metrics.json"
            )
        ),
        os.path.abspath(
            os.path.join(os.path.dirname(__file__), "model_metrics.json")
        ),
        "/app/models/model_metrics.json",
    ]
    for path in candidate_paths:
        if path and os.path.exists(path):
            return path
    return candidate_paths[1]


MODEL_PATH = find_model_path()
METRICS_PATH = find_metrics_path()
ml_model = None

try:
    ml_model = joblib.load(MODEL_PATH)
    logger.info(f"ML model loaded successfully from {MODEL_PATH}.")
except (FileNotFoundError, Exception) as e:
    logger.warning(
        f"ML model not found or could not be loaded at {MODEL_PATH}: {e}. "
        "Prediction endpoint will not work until model is trained."
    )


# Dependency to get the database session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/health", response_model=schemas.HealthResponse)
def health_check(db: Session = Depends(get_db)):
    """Health check endpoint to verify API, database connectivity, and ML model status."""
    db_status = "healthy"
    try:
        db.execute(text("SELECT 1"))
    except Exception as exc:
        logger.error(f"Database health check failed: {exc}")
        db_status = "unhealthy"

    overall_status = (
        "healthy" if db_status == "healthy" and ml_model is not None else "degraded"
    )
    return {
        "status": overall_status,
        "database": db_status,
        "model_loaded": ml_model is not None,
        "version": "1.1.0",
    }


@app.post(
    "/books/",
    response_model=schemas.Book,
    status_code=status.HTTP_201_CREATED,
)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    logger.info(f"Creating book: {book.title}")
    db_book = database.Book(**book.model_dump())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


@app.get("/books/", response_model=list[schemas.Book])
def read_books(
    skip: int = 0,
    limit: int = 100,
    title: str | None = None,
    author: str | None = None,
    db: Session = Depends(get_db),
):
    query = db.query(database.Book)
    if title:
        query = query.filter(database.Book.title.ilike(f"%{title}%"))
    if author:
        query = query.filter(database.Book.author.ilike(f"%{author}%"))
    return query.offset(skip).limit(limit).all()


@app.get("/books/{book_id}", response_model=schemas.Book)
def read_book(book_id: int, db: Session = Depends(get_db)):
    logger.info(f"Fetching book id: {book_id}")
    book = db.query(database.Book).filter(database.Book.id == book_id).first()
    if book is None:
        logger.warning(f"Book id {book_id} not found")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book not found"
        )
    return book


@app.put("/books/{book_id}", response_model=schemas.Book)
def update_book(
    book_id: int,
    book_update: schemas.BookUpdate,
    db: Session = Depends(get_db),
):
    logger.info(f"Updating book id: {book_id}")
    db_book = db.query(database.Book).filter(database.Book.id == book_id).first()
    if db_book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book not found"
        )

    update_data = book_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_book, key, value)

    db.commit()
    db.refresh(db_book)
    return db_book


@app.delete("/books/{book_id}", response_model=schemas.BookDeleteResponse)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    logger.info(f"Deleting book id: {book_id}")
    db_book = db.query(database.Book).filter(database.Book.id == book_id).first()
    if db_book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Book not found"
        )

    db.delete(db_book)
    db.commit()
    return {"message": "Book deleted successfully", "id": book_id}


@app.get("/model/metadata", response_model=schemas.ModelMetadataResponse)
def get_model_metadata():
    """Retrieve metadata and evaluation metrics for the deployed ML model."""
    if ml_model is None:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="ML model is not available",
        )

    if os.path.exists(METRICS_PATH):
        try:
            with open(METRICS_PATH, "r", encoding="utf-8") as f:
                metrics_data = json.load(f)
            return {
                "model_type": metrics_data.get("model_type", "RandomForestClassifier"),
                "features": metrics_data.get("features", {}),
                "metrics": metrics_data.get("metrics", {}),
                "status": "ready",
            }
        except Exception as exc:
            logger.warning(f"Error reading metrics file {METRICS_PATH}: {exc}")

    # Fallback if json file not found
    return {
        "model_type": type(ml_model.named_steps["classifier"]).__name__,
        "features": {
            "numerical": ["age", "fare", "sibsp", "parch"],
            "categorical": ["pclass", "sex", "embarked"],
        },
        "metrics": {},
        "status": "ready",
    }


@app.post("/predict", response_model=schemas.PredictionResult)
def predict_survival(passenger: schemas.Passenger):
    """Predict Titanic survival probability and classification."""
    if ml_model is None:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="ML model is not available",
        )

    passenger_df = pd.DataFrame([passenger.model_dump()])

    # Predict probability and class
    prediction = ml_model.predict(passenger_df)[0]
    survived = bool(prediction == 1)

    survival_prob = 1.0 if survived else 0.0
    if hasattr(ml_model, "predict_proba"):
        probabilities = ml_model.predict_proba(passenger_df)[0]
        survival_prob = float(probabilities[1])

    confidence_label = (
        "High"
        if survival_prob >= 0.75 or survival_prob <= 0.25
        else "Moderate"
    )

    return {
        "survived": survived,
        "survival_probability": round(survival_prob, 4),
        "confidence_label": confidence_label,
    }
