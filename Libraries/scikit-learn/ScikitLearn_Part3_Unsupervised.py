"""
ScikitLearn_Part3_Unsupervised.py
Implementing Unsupervised Learning models (Clustering and Dimensionality Reduction).
"""

import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs, load_digits
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

def clustering_example():
    print("=== CLUSTERING (K-Means) ===")
    # Generate synthetic clustering data
    X, y_true = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)
    
    # K-Means Clustering
    kmeans = KMeans(n_clusters=4, random_state=0, n_init='auto')
    y_kmeans = kmeans.fit_predict(X)
    
    print(f"Cluster Centers:\n{kmeans.cluster_centers_}")
    print("Plotting results... (Close the plot window to continue)")
    
    # Plotting
    plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')
    centers = kmeans.cluster_centers_
    plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, alpha=0.5)
    plt.title("K-Means Clustering")
    plt.show()

def dimensionality_reduction_example():
    print("\n=== DIMENSIONALITY REDUCTION (PCA) ===")
    # Load a high-dimensional dataset (Digits: 64 features)
    digits = load_digits()
    X = digits.data
    y = digits.target
    
    print(f"Original shape: {X.shape}") # (1797, 64)
    
    # It's important to scale before PCA
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Reduce from 64 dimensions to 2 dimensions for visualization
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_scaled)
    
    print(f"Reduced shape: {X_pca.shape}") # (1797, 2)
    print(f"Explained variance ratio by 2 components: {sum(pca.explained_variance_ratio_):.2f}")
    
    print("Plotting results... (Close the plot window to continue)")
    plt.figure(figsize=(8, 6))
    plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, edgecolor='none', alpha=0.5, cmap=plt.cm.get_cmap('nipy_spectral', 10))
    plt.xlabel('Component 1')
    plt.ylabel('Component 2')
    plt.colorbar(label='Digit Label', ticks=range(10))
    plt.title("PCA of Digits Dataset")
    plt.show()

if __name__ == "__main__":
    clustering_example()
    dimensionality_reduction_example()
