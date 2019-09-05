#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

# Reconstruct SVD
from numpy import array
from numpy import diag
from numpy import dot
from numpy import zeros
from scipy.linalg import svd
# define a matrix

A = array([
    [1, 2, 3]
  , [4, 5, 6]
  , [7, 8, 9]
])

print(A)
# Singular-value decomposition
U, s, VT = svd(A)
# create n x n Sigma matrix
Sigma = diag(s)
print(f"Sigma {Sigma}")
# reconstruct matrix
B = U.dot(Sigma.dot(VT))
print(B)

