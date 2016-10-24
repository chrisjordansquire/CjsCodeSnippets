import numpy as np
from poisson import create_data, poisson_dataset

def fit_nesterov(X, y, max_itr, mb_size, true_beta):

    theta = 1
    L = 1e-4

    data = poisson_dataset(X, y, mb_size)
    beta = np.zeros([data.p,1])
    converged = False
    itr = 0
    ls_count = 0

    beta_prev = beta
    while itr<max_itr and not converged:
        itr += 1

        theta_prev = theta
        theta = np.sqrt(theta_prev**4 + 4*theta_prev**2) - theta_prev**2
        theta = theta / 2

        y_new = beta + theta*(theta_prev**(-1) - 1) * (beta- beta_prev)
        grad_y = data.s_grad(y_new)
        grad_y_norm = np.sum(grad_y**2)

        beta_prev = beta
        beta = y_new + grad_y / L

        if itr % 10 == 0 or itr < 20:
            suff_decr = data.lik(beta) >= data.lik(y_new) + grad_y_norm / (L*2)
            if not suff_decr:
                ls_count += 1
                ls_itr = 0

                while (not suff_decr) and ls_itr < 10:
                    print 'LS', itr, ls_itr
                    L *= 2
                    ls_itr += 1
                    beta = y_new + grad_y / L
                    suff_decr = data.lik(beta) >= data.lik(y_new) + grad_y_norm / (L*2)

        if itr % 100 == 0:
            print "new itr"
            print "---------------------"
            print np.sum(np.abs(beta-true_beta))
            print np.sum(np.abs(beta_prev-beta))
            print ls_count
            print L
            ls_count = 0

    #return [i, beta]

def main():

    X,y,beta = create_data(10000, 10, 0, 0.1)
    fit_nesterov(X,y, 1000, 60, beta)


if __name__ == "__main__":
    main()
