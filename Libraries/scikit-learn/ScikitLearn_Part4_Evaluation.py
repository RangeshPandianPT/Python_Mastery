"""
ScikitLearn_Part4_Evaluation.py
Techniques for model evaluation, cross-validation, and hyperparameter tuning.
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, classification_report
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    print("=== MODEL EVALUATION & TUNING ===")
    # Load Dataset
    data = load_iris()
    X = data.data
    y = data.target
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 1. Cross-Validation
    print("\n--- 1. Cross-Validation ---")
    svc = SVC(kernel='linear', C=1)
    # 5-fold cross validation on the training data
    scores = cross_val_score(svc, X_train, y_train, cv=5)
    print(f"Cross-validation scores: {scores}")
    print(f"Average CV accuracy: {scores.mean():.4f}")
    
    # 2. Hyperparameter Tuning using GridSearchCV
    print("\n--- 2. Grid Search CV (Hyperparameter Tuning) ---")
    param_grid = {
        'C': [0.1, 1, 10, 100],
        'kernel': ['linear', 'rbf'],
        'gamma': ['scale', 'auto', 0.1, 1]
    }
    
    grid = GridSearchCV(SVC(), param_grid, refit=True, cv=5, verbose=1)
    grid.fit(X_train, y_train)
    
    print(f"Best Parameters found: {grid.best_params_}")
    print(f"Best Estimator Score: {grid.best_score_:.4f}")
    
    # 3. Model Evaluation on Test Set
    print("\n--- 3. Evaluation Metrics ---")
    # Using the best model from GridSearch
    y_pred = grid.predict(X_test)
    
    print("Classification Report:")
    print(classification_report(y_test, y_pred, target_names=data.target_names))
    
    # Confusion Matrix Visualization
    print("Showing Confusion Matrix plot...")
    cm = confusion_matrix(y_test, y_pred)
    sns.heatmap(cm, annot=True, cmap='Blues', xticklabels=data.target_names, yticklabels=data.target_names)
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.title('Confusion Matrix')
    plt.show()

if __name__ == "__main__":
    main()
