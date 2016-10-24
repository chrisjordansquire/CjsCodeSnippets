import numpy as np
import scipy.linalg as linalg

# Rayleigh Quotient Iteration

def rqi_iter(A, callback=None, tol=1e-10, max_iter=20):
    assert len(A.shape) == 2
    assert A.shape[0] == A.shape[1]

    N = A.shape[0]
    x = np.zeros((N,1), dtype='float64')
    x[0] = 1

    mu = 1
    mu_prev = 0
    
    converged = False
    shifted = A.copy()
    iter = 0

    while not converged and iter < max_iter:
        shifted -= (mu - mu_prev) * np.eye(N)
        x = linalg.solve(shifted, x)
        x /= linalg.norm(x)

        mu_prev = mu
        Ax = np.dot(A,x)
        mu = float(np.dot(x.T, Ax))

        err = linalg.norm(mu*x -Ax) 
        if err < tol:
            converged=True

        iter += 1
        if callback:
            callback(mu, x)


def main():
    A = np.random.randn(5,5)*10
    
    def print_stuff(mu, x):
        print "-----------------"
        print "mu ", mu
        print "x ", x
        print

    rqi_iter(A, callback=print_stuff)
    eig = linalg.eig(A)
    print "*************"
    print eig[0]
    print "*************"
    print eig[1].T




if __name__ == "__main__":
    main()
        


        


