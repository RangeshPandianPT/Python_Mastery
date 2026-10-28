from pydantic import BaseModel, ConfigDict


class BookBase(BaseModel):
    title: str
    author: str
    price: float


class BookCreate(BookBase):
    pass


class BookUpdate(BaseModel):
    title: str | None = None
    author: str | None = None
    price: float | None = None


class Book(BookBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class BookDeleteResponse(BaseModel):
    message: str
    id: int


class HealthResponse(BaseModel):
    status: str
    database: str
    model_loaded: bool
    version: str = "1.0.0"


class ModelMetadataResponse(BaseModel):
    model_type: str
    features: dict[str, list[str]]
    metrics: dict[str, dict[str, float]]
    status: str


class Passenger(BaseModel):
    pclass: int
    sex: str
    age: float | None = None
    sibsp: int
    parch: int
    fare: float
    embarked: str


class PredictionResult(BaseModel):
    survived: bool
    survival_probability: float
    confidence_label: str
