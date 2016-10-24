import numpy as np


def lu(A):
    assert len(A.shape) == 2
    assert A.shape[0] == A.shape[1]

    n = A.shape[0]

    L = np.zeros((n,n), dtype = 'float64')
    U = np.zeros((n,n), dtype = 'float64')

    np.fill_diagonal(U, 1)

    L[:,0] = A[:,0] 
    U[0,:] = A[0,:] / L[0,0]
    for p in range(1, n):
        L[p:,p] = A[p:,p] - np.dot(L[p:, 0:p], U[0:p, p])
        U[p,(p+1):] = (A[p,(p+1):]-np.dot(L[p, 0:p], U[0:p, (p+1):]))/ L[p,p]

    return L, U


def main():

    np.set_printoptions(precision=4)

    A = np.random.randn(5,5)
    A *= 10

    L, U = lu(A)
    print A
    print "------------------"
    print np.dot(L, U)
    print "------------------"
    print L
    print "------------------"
    print U
    print "------------------"
    print np.abs(A - np.dot(L, U))

if __name__ == "__main__":
    main()
