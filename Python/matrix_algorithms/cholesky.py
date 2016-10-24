import numpy as np


def cholesky(A):
    assert(len(A.shape) == 2) 
    rows = A.shape[0]
    columns = A.shape[1]
    assert(rows == columns)
    size = rows
    workSpace = A.copy()
    L = np.zeros((size, size))
    for j in range(size):
        L[j, j] = np.sqrt(workSpace[j, j])
        L[j+1:, j] = workSpace[j+1:, j] / L[j, j]
        workSpace[(j+1):, (j+1):] -= np.outer(L[j+1:, j], L[j+1:, j])
    return L
