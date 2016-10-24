import numpy as np

def qr(A):
    assert len(A.shape) == 2
    assert A.shape[0] == A.shape[1]

    n = A.shape[0]

    Q = np.eye(n, dtype='float64')
    R = np.array(A, dtype='float64')

    for p in xrange(n):
        v = np.copy(R[p:,p])
        v = v.reshape(n-p,1)
        v[0] += np.linalg.norm(v) * np.sign(v[0])
        v /= np.linalg.norm(v)

        Q[:, p:] -= 2*np.dot(np.dot(Q[:, p:], v), v.T)
        R[p:, p:] -= 2 * np.dot(v, np.dot(v.T, R[p:, p:]))

    return Q, R



def main():

    np.set_printoptions(precision=4)
    sep = "------------------------"

    A = np.random.randn(5,5)
    A *= 10

    Q, R = qr(A)

    print A
    print sep
    print np.dot(Q, R)
    print sep
    print np.abs(A - np.dot(Q,R))
    print sep 
    print Q
    print sep
    print R
    print sep
    print np.dot(Q.T, Q)
    print sep


if __name__ == "__main__":
    main()
