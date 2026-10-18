from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

from main import app, get_db
import database

# Setup a test database
SQLALCHEMY_DATABASE_URL = "sqlite:///./test_books.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

database.Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


def test_create_book():
    response = client.post(
        "/books/",
        json={"title": "Test Book", "author": "John Doe", "price": 19.99}
    )
    assert response.status_code == 201, response.text
    data = response.json()
    assert data["title"] == "Test Book"
    assert "id" in data


def test_read_books():
    response = client.get("/books/")
    assert response.status_code == 200
    assert type(response.json()) == list


def test_predict_survival():
    payload = {
        "pclass": 1,
        "sex": "female",
        "age": 29.0,
        "sibsp": 0,
        "parch": 0,
        "fare": 211.33,
        "embarked": "S"
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200, response.text
    data = response.json()
    assert "survived" in data
    assert isinstance(data["survived"], bool)


# Cleanup after tests
def teardown_module(module):
    if os.path.exists("./test_books.db"):
        try:
            os.remove("./test_books.db")
        except PermissionError:
            pass  # Windows might hold the file lock sometimes

