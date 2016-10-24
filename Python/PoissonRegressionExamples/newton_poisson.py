import numpy as np
import scipy as sp
import scipy.linalg as la
from poisson import create_data, poisson_dataset

def fit_newton(X, y, max_itr, true_beta, init_beta=None):
    converged = False

    data = poisson_dataset(X, y) 
    beta = np.zeros([data.p,1])

    if init_beta:
        beta = init_beta
    itr = 0

    while itr<max_itr and not converged:
        itr += 1

        grad = data.grad(beta)
        hess = data.hess(beta) 

        dir = la.solve(hess, grad)
        beta_new = beta - dir

        print "new itr"
        print "-----------------"
        print data.lik(beta_new)
        print np.sum(np.abs(beta - true_beta))
        print np.sum(np.abs(grad))

        #z = eta + (y-mu) / mu
        #tmp = np.dot(Xt, DX)
        #beta_new = la.solve(tmp, np.dot(np.transpose(DX),z))

        print np.sum(np.abs(beta-beta_new))
        #converged = np.all(np.abs(beta-beta_new) < 0.0000001)

        beta = beta_new

    return beta,itr

def main():
    X,y,beta = create_data(10000, 100, 0, 0.1) 
    fit_newton(X,y,20, beta)


if __name__ == "__main__":
    main()
