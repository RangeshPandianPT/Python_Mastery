"""
ScikitLearn_Part5_Pipelines.py
Building Machine Learning Pipelines to prevent data leakage and streamline workflows.
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def main():
    print("=== SCKIT-LEARN PIPELINES ===")
    
    # 1. Create mixed-type dummy data
    data = {
        'Age': [25, 30, np.nan, 45, 22, 50, 35, np.nan],
        'Income': [50000, 60000, 55000, 80000, 45000, 90000, 70000, 65000],
        'City': ['NY', 'London', 'NY', 'Paris', 'London', 'Paris', 'NY', 'London'],
        'Target': [0, 1, 0, 1, 0, 1, 1, 0]
    }
    df = pd.DataFrame(data)
    
    X = df.drop('Target', axis=1)
    y = df['Target']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

    # 2. Define column types
    numeric_features = ['Age', 'Income']
    categorical_features = ['City']

    # 3. Create Preprocessing steps (Transformers)
    # Numeric Pipeline: Impute missing -> Scale
    numeric_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='mean')),
        ('scaler', StandardScaler())
    ])

    # Categorical Pipeline: Impute missing -> OneHotEncode
    categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
        ('onehot', OneHotEncoder(handle_unknown='ignore'))
    ])

    # 4. Combine into a ColumnTransformer
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric_features),
            ('cat', categorical_transformer, categorical_features)
        ])

    # 5. Create the Final Pipeline (Preprocessor + Estimator)
    model_pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('classifier', RandomForestClassifier(random_state=42))
    ])

    # 6. Fit and Predict using the pipeline
    print("Training Model Pipeline...")
    model_pipeline.fit(X_train, y_train) # Pipeline handles fit/transform on training data automatically
    
    print("Making Predictions...")
    y_pred = model_pipeline.predict(X_test) # Pipeline handles transform on test data automatically
    
    print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
    print("\nPipeline components:")
    print(model_pipeline)

if __name__ == "__main__":
    main()
