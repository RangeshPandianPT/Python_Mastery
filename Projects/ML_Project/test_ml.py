import json
import os
import joblib
import numpy as np
import pandas as pd
import pytest


@pytest.fixture
def model_path():
    path = os.path.join(os.path.dirname(__file__), "titanic_rf_model.joblib")
    assert os.path.exists(path), f"Model file not found at {path}"
    return path


@pytest.fixture
def metrics_path():
    path = os.path.join(os.path.dirname(__file__), "model_metrics.json")
    assert os.path.exists(path), f"Metrics file not found at {path}"
    return path


@pytest.fixture
def sample_passengers():
    return pd.DataFrame(
        [
            {
                "pclass": 3,
                "sex": "male",
                "age": 22.0,
                "sibsp": 1,
                "parch": 0,
                "fare": 7.25,
                "embarked": "S",
            },
            {
                "pclass": 1,
                "sex": "female",
                "age": 35.0,
                "sibsp": 1,
                "parch": 0,
                "fare": 71.28,
                "embarked": "C",
            },
        ]
    )


def test_model_loading_and_pipeline_structure(model_path):
    model = joblib.load(model_path)
    assert hasattr(model, "predict"), "Model missing predict method"
    assert hasattr(model, "predict_proba"), "Model missing predict_proba method"
    assert "preprocessor" in model.named_steps
    assert "classifier" in model.named_steps


def test_model_prediction_output(model_path, sample_passengers):
    model = joblib.load(model_path)
    preds = model.predict(sample_passengers)
    assert len(preds) == 2
    for pred in preds:
        assert pred in [0, 1]

    probs = model.predict_proba(sample_passengers)
    assert probs.shape == (2, 2)
    # Probabilities must sum to ~1.0
    for prob in probs:
        assert 0.0 <= prob[0] <= 1.0
        assert 0.0 <= prob[1] <= 1.0
        assert np.isclose(np.sum(prob), 1.0)


def test_model_handles_missing_values_and_unseen_categories(model_path):
    model = joblib.load(model_path)
    # Row with NaN age, fare, and unknown embarkation port
    noisy_passenger = pd.DataFrame(
        [
            {
                "pclass": 2,
                "sex": "female",
                "age": np.nan,
                "sibsp": 0,
                "parch": 0,
                "fare": np.nan,
                "embarked": "UNKNOWN_PORT",
            }
        ]
    )
    pred = model.predict(noisy_passenger)
    assert len(pred) == 1
    assert pred[0] in [0, 1]


def test_model_metrics_content(metrics_path):
    with open(metrics_path, "r", encoding="utf-8") as f:
        metrics = json.load(f)

    assert "model_type" in metrics
    assert "training_timestamp" in metrics
    assert "features" in metrics
    assert "metrics" in metrics
    assert "random_forest" in metrics["metrics"]
    assert "accuracy" in metrics["metrics"]["random_forest"]
    assert "roc_auc" in metrics["metrics"]["random_forest"]

