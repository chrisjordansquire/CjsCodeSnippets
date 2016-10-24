import numpy as np
import scipy as sp
import scipy.linalg as la
from poisson import create_data, poisson_dataset

def fit_heavy_ball(X, y, max_itr, mb_size, true_beta):

    data = poisson_dataset(X, y, mb_size)
    beta = np.zeros([data.p,1])
    converged = False
    itr = 0
    
    beta_prev = beta
    momentum = 0.9 
    while itr<max_itr and not converged:
        itr += 1

        grad = data.s_grad(beta)
        step_size = 1/(np.sqrt(2*itr)+100)

        beta_new = beta + step_size*grad + momentum*(beta - beta_prev)
        if itr % 100 == 0:
            print "new itr"
            print "---------------------"
            print np.sum(np.abs(beta-true_beta))
            print np.sum(np.abs(beta-beta_new))
        
        beta_prev = beta
        beta = beta_new
        #converged = np.all(np.abs(beta-beta_new) < 0.0001)

    #return [i, beta]

def main():
    
    X,y,beta = create_data(10000, 10, 0, 0.1)
    fit_heavy_ball(X,y, 10000, 60, beta)
    

if __name__ == "__main__":
    main()
