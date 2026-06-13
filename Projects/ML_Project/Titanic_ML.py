# ============================================================
# END-TO-END MACHINE LEARNING PROJECT: TITANIC SURVIVAL
# ============================================================
# This script builds on EDA by creating a predictive model.
# Steps:
# 1. Load Data
# 2. Preprocessing & Feature Engineering
# 3. Model Building & Training
# 4. Evaluation
# 5. Model Saving
# ============================================================

import pandas as pd
import numpy as np
import seaborn as sns
import joblib
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

print("=" * 50)
print("1. LOADING DATA")
print("=" * 50)

# Load the built-in Titanic dataset from seaborn
df = sns.load_dataset('titanic')
print(f"Dataset Shape: {df.shape}")

# We will predict 'survived'. Let's drop some redundant or difficult columns for simplicity
# 'alive' is exactly the same as 'survived', 'class' is same as 'pclass', 'who' is redundant
columns_to_drop = ['alive', 'class', 'who', 'adult_male', 'deck', 'embark_town']
df = df.drop(columns=columns_to_drop)

# Drop rows where the target 'survived' is missing (if any)
df = df.dropna(subset=['survived'])

X = df.drop('survived', axis=1)
y = df['survived']

print("\n" + "=" * 50)
print("2. PREPROCESSING & PIPELINE SETUP")
print("=" * 50)

# Identify numerical and categorical columns
numeric_features = ['age', 'fare', 'sibsp', 'parch']
categorical_features = ['pclass', 'sex', 'embarked']

# Preprocessing for numerical data: Impute missing with median, then scale
numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

# Preprocessing for categorical data: Impute missing with mode, then OneHotEncode
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

# Combine preprocessing steps using ColumnTransformer
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ])

print("Preprocessing pipeline created.")

print("\n" + "=" * 50)
print("3. MODEL TRAINING")
print("=" * 50)

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
print(f"Training data shape: {X_train.shape}")
print(f"Testing data shape: {X_test.shape}")

# Create full pipelines including the classifier
rf_pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                              ('classifier', RandomForestClassifier(n_estimators=100, random_state=42))])

lr_pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                              ('classifier', LogisticRegression(random_state=42, max_iter=1000))])

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
rf_accuracy = accuracy_score(y_test, rf_predictions)
print(f"Random Forest Accuracy: {rf_accuracy:.4f}")
print("Random Forest Classification Report:")
print(classification_report(y_test, rf_predictions))

# Evaluate Logistic Regression
lr_predictions = lr_pipeline.predict(X_test)
lr_accuracy = accuracy_score(y_test, lr_predictions)
print(f"\nLogistic Regression Accuracy: {lr_accuracy:.4f}")
print("Logistic Regression Classification Report:")
print(classification_report(y_test, lr_predictions))

print("\n" + "=" * 50)
print("5. SAVING THE MODEL")
print("=" * 50)

# Let's say Random Forest performed slightly better, so we save that pipeline
model_filename = 'titanic_rf_model.joblib'
joblib.dump(rf_pipeline, model_filename)
print(f"Model successfully saved as '{model_filename}'")

# Demonstration of loading the model
loaded_model = joblib.load(model_filename)
sample_passenger = pd.DataFrame([{
    'pclass': 3, 'sex': 'male', 'age': 22.0, 'sibsp': 1, 'parch': 0, 'fare': 7.25, 'embarked': 'S'
}])
sample_prediction = loaded_model.predict(sample_passenger)
print(f"\nPrediction for a sample passenger (3rd class, male, 22yo): {'Survived' if sample_prediction[0]==1 else 'Did not survive'}")
