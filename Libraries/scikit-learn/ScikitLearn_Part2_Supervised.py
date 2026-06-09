"""
ScikitLearn_Part2_Supervised.py
Implementing Supervised Learning models (Classification and Regression).
"""

from sklearn.datasets import load_breast_cancer, fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler

def classification_example():
    print("=== CLASSIFICATION (Breast Cancer Dataset) ===")
    data = load_breast_cancer()
    X = data.data
    y = data.target
    
    # Split & Scale
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Logistic Regression
    print("\n--- Logistic Regression ---")
    log_reg = LogisticRegression()
    log_reg.fit(X_train_scaled, y_train)
    y_pred_log = log_reg.predict(X_test_scaled)
    print(f"Accuracy: {accuracy_score(y_test, y_pred_log):.4f}")
    
    # Random Forest
    print("\n--- Random Forest Classifier ---")
    rf = RandomForestClassifier(n_estimators=100, random_state=42)
    rf.fit(X_train, y_train) # Tree models don't require scaling strictly
    y_pred_rf = rf.predict(X_test)
    print(f"Accuracy: {accuracy_score(y_test, y_pred_rf):.4f}")
    print("\nClassification Report (Random Forest):")
    print(classification_report(y_test, y_pred_rf, target_names=data.target_names))

def regression_example():
    print("\n=== REGRESSION (California Housing Dataset) ===")
    data = fetch_california_housing()
    X = data.data
    y = data.target
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Linear Regression
    print("\n--- Linear Regression ---")
    lin_reg = LinearRegression()
    lin_reg.fit(X_train, y_train)
    y_pred = lin_reg.predict(X_test)
    
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    print(f"Mean Squared Error: {mse:.4f}")
    print(f"R2 Score: {r2:.4f}")

if __name__ == "__main__":
    classification_example()
    regression_example()
