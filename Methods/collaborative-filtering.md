2 types:

1. neighborhood methods
2. [restricted boltzman machines](http://www.cs.toronto.edu/~rsalakhu/papers/rbmcf.pdf)
3. latent factor methods
    - assume that both users and movies (in the netflix example) live in a some low-dimensional space
    - this space is called the `latent space`
    - recommend a movie to the user based on its proximity to the user in the `latent space`
    - based on matrix factorizatoin
    - 3 typical methods of matrix factorization
        1. unconstrained matrix factorization
        2. Singular Value Decompositoin
            - A = U(orthagonal) x Sigma(diagonal) x V.T(orthagonal)
            - A can be any matrix
            - if A is symmetric positive definite U and V can be the same and equal to eigenvectors of A
        3. Non negative matrix factorization

