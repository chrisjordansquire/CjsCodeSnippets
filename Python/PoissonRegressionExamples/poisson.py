import numpy as np
import scipy as sp
import scipy.special as special


def create_data(nobs, npar, xmin, xmax):
    X = np.random.rand(nobs, npar)
    X = (X*(xmax - xmin)) - xmin

    beta = np.random.rand(npar,1)

    eta = np.dot(X, beta)
    mu = np.exp(eta)
    y = np.random.poisson(mu)

    return X,y,beta


class poisson_dataset(object):

    def __init__(self, X, y, mb_size=None):
        assert(len(y.shape) == len(X.shape) == 2)
        assert(y.shape[0] == X.shape[0])
        assert(y.shape[1] == 1)

        self.N = X.shape[0]
        self.p = X.shape[1]
        self.mb_size = mb_size
        self.mb_count = 0

        self.y = np.array(y)
        self.X = np.array(X)
        shuffle_ind = np.arange(self.N)
        np.random.shuffle(shuffle_ind)

        self.y = self.y[shuffle_ind,:]
        self.X = self.X[shuffle_ind,:]

    def _check_beta(self, beta):
        assert(len(beta.shape) == 2)
        assert(beta.shape[0] == self.p)

    def reset_mb(self, mb_size):
        self.mb_count = 0
        self.mb_size = mb_size

    def lik(self, beta):
        self._check_beta(beta)
        eta = np.dot(self.X, beta)
        mu = np.exp(eta)
        liks = -mu + self.y*eta - special.gammaln(self.y+1)
        return np.average(liks)

    def grad(self, beta, idx=None):
        self._check_beta(beta)
        if idx is not None:
            X = self.X[idx,:]
            y = self.y[idx]
        else:
            X = self.X
            y = self.y
        eta = np.dot(X, beta)
        mu = np.exp(eta) #Must be replaced if non-log-link is used
        resid = y - mu
        grad = np.average(resid * X, axis=0).reshape(self.p,1)
        return grad

    def hess(self, beta, idx=None):
        self._check_beta(beta)
        if idx is not None:
            X = self.X[idx,:]
        else:
            X = self.X
        eta = np.dot(X, beta)
        weights = -np.exp(eta)/X.shape[0]
        hess = np.dot(X.T, weights*X)
        return hess

    def s_grad(self, beta):
        idx = self._next_mb_range()
        return self.grad(beta, idx)

    def s_hess(self, beta):
        idx = self.next_mb_range()
        return self.hess(beta, idx)

    def s_grad_hess(self, beta):
        idx = self.next_mb_range()
        grad = self.grad(beta,idx)
        hess = self.hess(beta, idx)
        return grad, hess

    def _next_mb_range(self):
        assert(self.mb_size is not None)
        if self.mb_count + self.mb_size >= self.N:
            idx=range(self.mb_count, self.N)
            self.mb_count=0
        else:
            idx=range(self.mb_count, self.mb_count+self.mb_size)
            self.mb_count += self.mb_size
        return idx



