# ============================================================
# END-TO-END MACHINE LEARNING PROJECT: TITANIC SURVIVAL
# ============================================================
# This script builds on EDA by creating a predictive model.
# Steps:
# 1. Load Data
# 2. Preprocessing & Feature Engineering
# 3. Model Building & Training
# 4. Evaluation
# 5. Model & Metrics Saving
# ============================================================

import datetime
import json
import os
import joblib
import pandas as pd
import seaborn as sns
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


def load_titanic_dataset():
    """Load Titanic dataset online via seaborn or fall back to local CSV."""
    try:
        data = sns.load_dataset("titanic")
        print("Loaded dataset online via seaborn.")
        return data
    except Exception as exc:
        print(f"Online download failed ({exc}). Attempting to load local fallback...")
        candidate_paths = [
            os.path.abspath(
                os.path.join(
                    os.path.dirname(__file__), "..", "shared_data", "titanic.csv"
                )
            ),
            os.path.abspath(
                os.path.join(os.path.dirname(__file__), "titanic.csv")
            ),
            "/data/titanic.csv",
        ]
        for path in candidate_paths:
            if os.path.exists(path):
                print(f"Loaded dataset from fallback path: {path}")
                return pd.read_csv(path)
        raise RuntimeError("Could not load Titanic dataset online or locally.")


print("=" * 50)
print("1. LOADING DATA")
print("=" * 50)

df = load_titanic_dataset()
print(f"Dataset Shape: {df.shape}")

# We will predict 'survived'. Let's drop some redundant or difficult columns for simplicity
# 'alive' is exactly the same as 'survived', 'class' is same as 'pclass', 'who' is redundant
columns_to_drop = ["alive", "class", "who", "adult_male", "deck", "embark_town"]
available_to_drop = [col for col in columns_to_drop if col in df.columns]
df = df.drop(columns=available_to_drop)

# Drop rows where the target 'survived' is missing (if any)
df = df.dropna(subset=["survived"])

X = df.drop("survived", axis=1)
y = df["survived"]

print("\n" + "=" * 50)
print("2. PREPROCESSING & PIPELINE SETUP")
print("=" * 50)

# Identify numerical and categorical columns
numeric_features = ["age", "fare", "sibsp", "parch"]
categorical_features = ["pclass", "sex", "embarked"]

# Preprocessing for numerical data: Impute missing with median, then scale
numeric_transformer = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()),
    ]
)

# Preprocessing for categorical data: Impute missing with mode, then OneHotEncode
categorical_transformer = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("onehot", OneHotEncoder(handle_unknown="ignore")),
    ]
)

# Combine preprocessing steps using ColumnTransformer
preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numeric_features),
        ("cat", categorical_transformer, categorical_features),
    ]
)

print("Preprocessing pipeline created.")

print("\n" + "=" * 50)
print("3. MODEL TRAINING")
print("=" * 50)

# Split the data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
print(f"Training data shape: {X_train.shape}")
print(f"Testing data shape: {X_test.shape}")

# Create full pipelines including the classifier
rf_pipeline = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        (
            "classifier",
            RandomForestClassifier(n_estimators=100, random_state=42),
        ),
    ]
)

lr_pipeline = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        (
            "classifier",
            LogisticRegression(random_state=42, max_iter=1000),
        ),
    ]
)

# Train models
print("Training Random Forest...")
rf_pipeline.fit(X_train, y_train)

print("Training Logistic Regression...")
lr_pipeline.fit(X_train, y_train)

print("\n" + "=" * 50)
print("4. EVALUATION")
print("=" * 50)

# Evaluate Random Forest
rf_predictions = rf_pipeline.predict(X_test)
rf_prob = rf_pipeline.predict_proba(X_test)[:, 1]
rf_accuracy = float(accuracy_score(y_test, rf_predictions))
rf_precision = float(precision_score(y_test, rf_predictions, zero_division=0))
rf_recall = float(recall_score(y_test, rf_predictions, zero_division=0))
rf_f1 = float(f1_score(y_test, rf_predictions, zero_division=0))
rf_roc_auc = float(roc_auc_score(y_test, rf_prob))

print(f"Random Forest Accuracy: {rf_accuracy:.4f}")
print(f"Random Forest ROC-AUC:  {rf_roc_auc:.4f}")
print("Random Forest Classification Report:")
print(classification_report(y_test, rf_predictions))

# Evaluate Logistic Regression
lr_predictions = lr_pipeline.predict(X_test)
lr_prob = lr_pipeline.predict_proba(X_test)[:, 1]
lr_accuracy = float(accuracy_score(y_test, lr_predictions))
lr_precision = float(precision_score(y_test, lr_predictions, zero_division=0))
lr_recall = float(recall_score(y_test, lr_predictions, zero_division=0))
lr_f1 = float(f1_score(y_test, lr_predictions, zero_division=0))
lr_roc_auc = float(roc_auc_score(y_test, lr_prob))

print(f"\nLogistic Regression Accuracy: {lr_accuracy:.4f}")
print(f"Logistic Regression ROC-AUC:  {lr_roc_auc:.4f}")
print("Logistic Regression Classification Report:")
print(classification_report(y_test, lr_predictions))

print("\n" + "=" * 50)
print("5. SAVING MODEL & METRICS")
print("=" * 50)

# Save Random Forest model pipeline
model_dir = os.path.dirname(os.path.abspath(__file__))
model_filename = os.path.join(model_dir, "titanic_rf_model.joblib")
joblib.dump(rf_pipeline, model_filename)
print(f"Model successfully saved as '{model_filename}'")

# Save detailed model metadata and metrics
metrics_payload = {
    "model_type": "RandomForestClassifier",
    "training_timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "dataset_shape": list(df.shape),
    "features": {
        "numerical": numeric_features,
        "categorical": categorical_features,
    },
    "metrics": {
        "random_forest": {
            "accuracy": round(rf_accuracy, 4),
            "precision": round(rf_precision, 4),
            "recall": round(rf_recall, 4),
            "f1_score": round(rf_f1, 4),
            "roc_auc": round(rf_roc_auc, 4),
        },
        "logistic_regression": {
            "accuracy": round(lr_accuracy, 4),
            "precision": round(lr_precision, 4),
            "recall": round(lr_recall, 4),
            "f1_score": round(lr_f1, 4),
            "roc_auc": round(lr_roc_auc, 4),
        },
    },
    "hyperparameters": {
        "n_estimators": 100,
        "random_state": 42,
    },
}

metrics_path = os.path.join(model_dir, "model_metrics.json")
with open(metrics_path, "w", encoding="utf-8") as f:
    json.dump(metrics_payload, f, indent=2)
print(f"Model metrics successfully exported to '{metrics_path}'")

# Demonstration of loading the model
loaded_model = joblib.load(model_filename)
sample_passenger = pd.DataFrame(
    [
        {
            "pclass": 3,
            "sex": "male",
            "age": 22.0,
            "sibsp": 1,
            "parch": 0,
            "fare": 7.25,
            "embarked": "S",
        }
    ]
)
sample_prediction = loaded_model.predict(sample_passenger)
sample_probability = loaded_model.predict_proba(sample_passenger)[0][1]
outcome = "Survived" if sample_prediction[0] == 1 else "Did not survive"
print(
    f"\nPrediction for a sample passenger (3rd class, male, 22yo): "
    f"{outcome} (Survival Probability: {sample_probability:.2%})"
)
