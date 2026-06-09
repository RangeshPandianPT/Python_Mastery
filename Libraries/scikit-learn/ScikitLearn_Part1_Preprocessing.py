"""
ScikitLearn_Part1_Preprocessing.py
A guide to data preprocessing and feature engineering using Scikit-Learn.
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder, OneHotEncoder
from sklearn.impute import SimpleImputer

def main():
    # 1. Create a dummy dataset
    data = {
        'Age': [25, np.nan, 30, 45, 22, 50],
        'Salary': [50000, 60000, 55000, np.nan, 45000, 80000],
        'City': ['New York', 'London', 'New York', 'Paris', 'London', 'Paris'],
        'Purchased': ['No', 'Yes', 'No', 'Yes', 'No', 'Yes']
    }
    df = pd.DataFrame(data)
    print("--- Original Dataset ---")
    print(df)
    
    # 2. Handling Missing Data (Imputation)
    print("\n--- Imputing Missing Values ---")
    # Impute missing numerical values with the mean
    imputer = SimpleImputer(strategy='mean')
    df[['Age', 'Salary']] = imputer.fit_transform(df[['Age', 'Salary']])
    print(df)
    
    # 3. Encoding Categorical Data
    print("\n--- Encoding Categorical Data ---")
    # Label Encoding for the Target Variable ('Purchased')
    le = LabelEncoder()
    df['Purchased'] = le.fit_transform(df['Purchased'])
    
    # One-Hot Encoding for Nominal Categorical Data ('City')
    df = pd.get_dummies(df, columns=['City'], drop_first=True)
    print(df)
    
    # 4. Feature Scaling
    print("\n--- Feature Scaling ---")
    # Standardizing features by removing the mean and scaling to unit variance
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(df[['Age', 'Salary']])
    
    df_scaled = df.copy()
    df_scaled[['Age', 'Salary']] = scaled_features
    print("Standardized DataFrame:")
    print(df_scaled)
    
    # 5. Train/Test Split
    print("\n--- Train / Test Split ---")
    X = df_scaled.drop('Purchased', axis=1) # Features
    y = df_scaled['Purchased']              # Target
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    print(f"X_train shape: {X_train.shape}")
    print(f"X_test shape: {X_test.shape}")
    print("Ready for machine learning models!")

if __name__ == "__main__":
    main()
