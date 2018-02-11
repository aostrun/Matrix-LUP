# Matrix LUP Decomposition
---
Python implementation of matrices that implements features such as LU/LUP decomposition and 
forward and backward substitutions which are used for solving linear equation Ax = B
and solving matrix inverse trough LU decomposition.

## LU and LUP

LU decomposition refers to the factorization of square matrix A into two factors, 
a unit in lower triangular matrix L and an upper triangular matrix U, A = LU.
More on the theory behind LU decomposition can be found [here](https://en.wikipedia.org/wiki/LU_decomposition).

This implementation allows for LU and LUP decompositions. Difference between the is that LU is the pure form of 
decomposition and LUP uses partial pivoting (permutations in rows) which solves problem of selecting pivot with value 0.


## Linear equations

We can represent linear equation with matrix form Ax = B where we want to solve the equation for x given A and B.
Firstly we need to decompose matrix A to A = LU with LU decomposition. After that our linear equations turns to 
LUx = B. We can insert substitution y = Ux and get equation Ly = B. Now we can easily solve this equation with 
forward substitution and find the y. After finding y we solve Ux = y with backward substitution and in the end we 
find the missing x. If we use LUP insted of LU we need to do matrix multiplication with 
P (permutation matrix of LUP) and B, resulting with equation Ly = PB and Ux = y.


