import os
import sys
from fastapi import HTTPException
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

sys.path.append(os.path.dirname(__file__))
import database
from main import (
    create_book,
    delete_book,
    get_model_metadata,
    health_check,
    predict_survival,
    read_book,
    read_books,
    update_book,
)
import schemas

# Setup an isolated test database
TEST_DB_FILE = os.path.join(os.path.dirname(__file__), "test_books.db")
SQLALCHEMY_DATABASE_URL = f"sqlite:///{TEST_DB_FILE}"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)

database.Base.metadata.create_all(bind=engine)


@pytest.fixture
def db_session():
    """Yield a database session and roll back changes after test."""
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


def test_health_check(db_session):
    result = health_check(db=db_session)
    assert result["database"] == "healthy"
    assert result["status"] in ["healthy", "degraded"]
    assert "model_loaded" in result
    assert result["version"] == "1.1.0"


def test_create_and_read_book(db_session):
    book_in = schemas.BookCreate(
        title="Automate the Boring Stuff",
        author="Al Sweigart",
        price=29.99,
    )
    created = create_book(book=book_in, db=db_session)
    assert created.title == "Automate the Boring Stuff"
    assert created.author == "Al Sweigart"
    assert created.price == 29.99
    assert created.id is not None

    fetched = read_book(book_id=created.id, db=db_session)
    assert fetched.id == created.id
    assert fetched.title == "Automate the Boring Stuff"


def test_read_books_list_and_filter(db_session):
    book_a = schemas.BookCreate(
        title="Fluent Python",
        author="Luciano Ramalho",
        price=45.00,
    )
    book_b = schemas.BookCreate(
        title="Python Crash Course",
        author="Eric Matthes",
        price=35.00,
    )
    create_book(book=book_a, db=db_session)
    create_book(book=book_b, db=db_session)

    all_books = read_books(skip=0, limit=100, db=db_session)
    assert len(all_books) >= 2

    filtered = read_books(title="Fluent", db=db_session)
    assert len(filtered) >= 1
    assert any("Fluent" in b.title for b in filtered)


def test_update_book(db_session):
    book = create_book(
        book=schemas.BookCreate(
            title="Old Edition", author="Writer", price=15.00
        ),
        db=db_session,
    )

    update_payload = schemas.BookUpdate(price=19.99, title="New Edition")
    updated = update_book(
        book_id=book.id, book_update=update_payload, db=db_session
    )
    assert updated.id == book.id
    assert updated.price == 19.99
    assert updated.title == "New Edition"
    assert updated.author == "Writer"


def test_delete_book(db_session):
    book = create_book(
        book=schemas.BookCreate(
            title="Book to Delete", author="Temporary", price=9.99
        ),
        db=db_session,
    )

    del_response = delete_book(book_id=book.id, db=db_session)
    assert del_response["id"] == book.id
    assert "successfully" in del_response["message"]

    with pytest.raises(HTTPException) as exc:
        read_book(book_id=book.id, db=db_session)
    assert exc.value.status_code == 404


def test_nonexistent_book_errors(db_session):
    with pytest.raises(HTTPException) as exc1:
        read_book(book_id=999999, db=db_session)
    assert exc1.value.status_code == 404

    with pytest.raises(HTTPException) as exc2:
        update_book(
            book_id=999999,
            book_update=schemas.BookUpdate(title="X"),
            db=db_session,
        )
    assert exc2.value.status_code == 404

    with pytest.raises(HTTPException) as exc3:
        delete_book(book_id=999999, db=db_session)
    assert exc3.value.status_code == 404


def test_model_metadata():
    metadata = get_model_metadata()
    assert metadata["status"] == "ready"
    assert "model_type" in metadata
    assert "features" in metadata


def test_predict_survival():
    passenger = schemas.Passenger(
        pclass=1,
        sex="female",
        age=29.0,
        sibsp=0,
        parch=0,
        fare=211.33,
        embarked="S",
    )
    result = predict_survival(passenger)
    assert "survived" in result
    assert isinstance(result["survived"], bool)
    assert "survival_probability" in result
    assert 0.0 <= result["survival_probability"] <= 1.0
    assert result["confidence_label"] in ["High", "Moderate"]


# Clean up test database file if possible
def teardown_module(module):
    if os.path.exists(TEST_DB_FILE):
        try:
            os.remove(TEST_DB_FILE)
        except PermissionError:
            pass
