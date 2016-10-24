import numpy as np
import scipy as sp
import scipy.linalg as la
from poisson import create_data, poisson_dataset

np.seterr(divide='raise', over='raise', invalid='raise')

def fit_sgd(X, y, max_itr, mb_size, true_beta):

    data = poisson_dataset(X, y, mb_size)
    beta = np.zeros([data.p,1])
    converged = False
    itr = 0
    print data.lik(beta), " STARTING LIKELIHOOD"

    beta_prev = beta
    grad_prev = data.s_grad(beta)
    beta = beta + grad_prev

    k = 20
    last_k = np.array([-np.Inf]*k)
    n_too_small = 0
    used_ls = 0
    n_neg = 0
    while itr<max_itr and not converged:
        itr += 1

        grad = data.s_grad(beta)

        s = beta - beta_prev
        y = grad - grad_prev

        grad_prev = grad
        beta_prev = beta

        d = np.dot(y.T, s)
        if np.abs(d) < 1e-6:
            step_size = 0.0001
        else:
            step_size = -np.dot(s.T, s) / np.dot(y.T, s)
        if step_size < 0.0001:
            if step_size < 0:
                n_neg += 1
            step_size = 0.0001
            n_too_small += 1
        elif step_size > 100:
            print "too big"
            step_size = 100

        beta_tmp = beta + step_size*grad
        suff_decr = False
        max_k = min(last_k)
        grad_norm2 = np.dot(grad.T, grad)
        gamma = 0.001
        safeguard_itr = 0
        while not suff_decr:
            f_k = data.lik(beta_tmp)
            lower_bound = max_k + step_size * gamma * grad_norm2
            if f_k <= lower_bound:
                used_ls += 1
                safeguard_itr += 1
                if safeguard_itr > 10:
                    print itr
                    print lower_bound
                    print grad_norm2
                    print gamma
                    print step_size
                    print f_k
                    raise Exception("armijo safeguard fail")
                step_size = step_size / 2
                beta_tmp = beta + step_size*grad
            else:
                suff_decr = True
                last_k[itr % k] = f_k
        beta_new = beta_tmp

        if itr % 10 == 0:
            print "new itr"
            print "---------------------"
            print "too small: ", n_too_small
            print "negative stepsize", n_neg
            print "used ls", used_ls
            n_too_small = 0
            used_ls = 0
            n_neg = 0
            print data.lik(beta_new)
            print np.sum(np.abs(beta-true_beta))
            print np.sum(np.abs(grad))
            print np.sum(np.abs(beta-beta_new))

        beta = beta_new
        #converged = np.all(np.abs(beta-beta_new) < 0.0001)

    #return [i, beta]

def main():

    X,y,beta = create_data(10000, 100, 0, 0.1)
    fit_sgd(X,y, 100, 60, beta)


if __name__ == "__main__":
    main()
