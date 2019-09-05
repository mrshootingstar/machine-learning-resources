import numpy as np
from numpy import array

def pca(X):
    # Data matrix X, assumes 0-centered
    n, m = X.shape
    # assert the mean of each **column** is close to 0
    assert np.allclose(X.mean(axis=0), np.zeros(m))
    # Compute covariance matrix
    C = np.dot(X.T, X) / (n-1)
    # Eigen decomposition
    eigen_vals, eigen_vecs = np.linalg.eig(C)
    # Project X onto PC space
    X_pca = np.dot(X, eigen_vecs)
    return X_pca


def svd(X):
    # Data matrix X, X doesn't need to be 0-centered
    n, m = X.shape
    # Compute full SVD
    U, Sigma, Vh = np.linalg.svd(X, 
        full_matrices=False, # It's not necessary to compute the full matrix of U or V
        compute_uv=True)
    # Transform X with SVD components
    X_svd = np.dot(U, np.diag(Sigma))
    return X_svd



# Check the relationship between SVD and eigendecomposition
X = array([
    [1, 2, 3]
  , [4, 5, 6]
  , [7, 8, 9]
])
n=3

# Compute covariance matrix
C = np.dot(X.T, X) / (n-1)
# Eigen decomposition
eigen_vals, eigen_vecs = np.linalg.eig(C)
# SVD
U, Sigma, Vh = np.linalg.svd(X, 
    full_matrices=False, 
    compute_uv=True)
# Relationship between singular values and eigen values:
print(np.allclose(np.square(Sigma) / (n - 1), eigen_vals)) # True



print(pca(X-X.mean(axis=0)))