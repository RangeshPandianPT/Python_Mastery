# Introduction to scikit-learn
# Scikit-learn is a powerful library for machine learning in Python.

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report

print("--- 1. Loading a Dataset ---")
# Load the classic Iris dataset
iris = load_iris()
X = iris.data # Features
y = iris.target # Labels
print(f"Dataset Shape: {X.shape}")

print("\n--- 2. Splitting Data into Training and Testing Sets ---")
# Split data: 80% for training, 20% for testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"Training set size: {X_train.shape[0]}")
print(f"Testing set size: {X_test.shape[0]}")

print("\n--- 3. Preprocessing (Scaling) ---")
# Standardize features by removing the mean and scaling to unit variance
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
print("Data scaling completed.")

print("\n--- 4. Training a Model ---")
# Initialize the K-Nearest Neighbors classifier
knn = KNeighborsClassifier(n_neighbors=3)
# Fit the model on training data
knn.fit(X_train_scaled, y_train)
print("Model trained successfully.")

print("\n--- 5. Making Predictions & Evaluation ---")
# Predict on testing data
y_pred = knn.predict(X_test_scaled)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")

print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))
