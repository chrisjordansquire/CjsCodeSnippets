import numpy as np
import scipy as sp
import scipy.linalg as la
from poisson import create_data, poisson_dataset

def fit_polyak_rupert(X, y, max_itr, mb_size, true_beta):

    data = poisson_dataset(X, y, mb_size)
    beta = np.zeros([data.p,1])
    converged = False
    itr = 0

    n_avg = 1.0
    beta_avg = np.zeros([data.p,1])
    while itr<max_itr and not converged:
        itr += 1

        grad = data.s_grad(beta)
        step_size = 1/(np.sqrt(2*itr)+10000)

        beta_new = beta + step_size*grad
        if itr > max_itr-10000:
            beta_avg = beta_avg - (beta_avg-beta_new) / n_avg
            n_avg += 1
        if itr % 1000 == 0:
            print "new itr"
            print "---------------------"
            print np.sum(np.abs(beta_avg-true_beta)) 
            print np.sum(np.abs(beta-true_beta))
            print np.sum(np.abs(beta-beta_new))

        beta = beta_new
        #converged = np.all(np.abs(beta-beta_new) < 0.0001)

    #return [i, beta]

def main():
    
    X,y,beta = create_data(1000, 10, 0, 0.1)
    fit_polyak_rupert(X,y, 500000, 60, beta)
    

if __name__ == "__main__":
    main()
