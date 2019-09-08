## LU or Lower Upper Decomposition
- A = L(lower triangle) x U(upper trinagle)
- only need proper permutation of rows (or columns)
    - P(permutation matrix) x A = L x U
## LDU
- A = Lower x Diagonal x Upper
## Cholesky
- Used to solve system of equations; in Kalman Filters
- A ( Hermitian positive-definite matrix) = L (lower triangular matrix with real and positive diagonal entries) x L* (conjugate transpose of L)
- Variation:
    - A = LDL* where D is a diagonal matrix
## QR decompositoin
- A (Any real square matrix) = Q (orthogonal) x R (Upper Trianagular )
- If A is `invertible` the decompostion is unique if elements of the trace of R are positive 
- Variations:
    - A = Q x L (Lower Triangular)
    - A = R x Q
    - A = L x Q
- Solution using `Gram–Schmidt process`
## Eigen Decomposition
- A (square n × n matrix with n linearly independent eigenvectors) = Q (square; col's are eigenvectors) x Lambda (diagonal with trace equal to eigenvectors) * Q^-1
- A = Q x Lambda x Q^{-1}
- Math:
    - Av = lambda x v (or in other words, matrix transformation is scaling)
    - then: 
## SVD 
- Input: (m x n) matrix 
- output: 3 matrixes: M = U x Sigma x V*
    - U: square (m x m) and unitary (hence orthogonal)
    - Sigma: diagonal (m × n) non-negative real numbers on the diagonal
    - V*: conjugate transpose of V (which is nxn and unitary)
## Non-negative Matrix Factorization
