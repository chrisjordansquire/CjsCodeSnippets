import numpy as np
import scipy as sp
import scipy.linalg as la
from poisson import create_data, poisson_dataset
from my_args import parseArgs

def fit_bfgs(X, y, max_itr, true_beta, init_beta=None, ls=None):
    converged = False

    data = poisson_dataset(X, y) 
    beta = np.zeros([data.p,1])

    if init_beta:
        beta = init_beta
    itr = 0
    H = data.hess(beta)
    grad_new = data.grad(beta)

    while itr<max_itr and not converged:
        itr += 1

        grad = grad_new 

        dir = np.dot(H, grad) 

        if ls:
            f = data.lik(beta)
            f_prime = -np.dot(grad.T, dir)
            step = ls(data, beta, -dir, f, f_prime)
        else:
            step = 0.1

        beta_new = beta - step*dir

        grad_new = data.grad(beta_new) 

        s = beta_new - beta
        y = grad_new - grad
        rho = 1/np.sum(s*y) 
        conj = np.eye(data.p) - rho * np.dot(s,y.T) 
        H = np.dot(conj, np.dot(H, conj)) + rho*np.dot(s,s.T) 


        print "new itr"
        print "-----------------"
        print data.lik(beta_new)
        print np.sum(np.abs(beta - true_beta))
        print np.sum(np.abs(grad))
        print step

        #z = eta + (y-mu) / mu
        #tmp = np.dot(Xt, DX)
        #beta_new = la.solve(tmp, np.dot(np.transpose(DX),z))

        print np.sum(np.abs(beta-beta_new))
        #converged = np.all(np.abs(beta-beta_new) < 0.0000001)

        beta = beta_new

    return beta,itr

def armijo_search(data,beta, d, f, f_prime,  alpha0=1.0,
        c=1e-2, decrease=2.0, max_iter=40):
    
    alpha=alpha0
    iter=1
    while iter < max_iter:
        if data.lik(beta + alpha*d) > f + alpha*c*f_prime:
            return alpha
        alpha = alpha/decrease
        iter += 1

    return alpha

def interpol_search(data,beta, d, f, f_prime,  alpha0=1.0,
        c=1e-2, decrease=2.0, max_iter=40):
    """
    WARNING: the problem being solved is maximization. So you CANNOT
    directly use the formulas in Nocedal/Wright.
    """
    
    pass

def main():
    args = parseArgs()

    X,y,beta = create_data(10000, 100, 0, 0.1) 

    if args.opt=="pure":
        ls=None
    elif args.opt == "armijo":
        ls=armijo_search 
    elif args.opt == "interpolation":
        ls=interpol_search

    fit_bfgs(X,y,20, beta, ls=ls)


if __name__ == "__main__":
    main()
