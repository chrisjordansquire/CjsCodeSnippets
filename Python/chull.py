import numpy as np
import scipy.spatial as sps
from mayavi import mlab
import argparse
import scipy.stats as stats

# Example using Mayavi

def helix(t):
    return np.array([np.sin(5*t), np.cos(5*t), t])

def testHelix():
    t = np.linspace(0, 10, 1000)
    return helix(t).T

def chPic3d(arr):
    assert(len(arr.shape) == 2)
    assert(arr.shape[1] == 3)

    cHull = sps.ConvexHull(arr)
    mlab.triangular_mesh(arr[:,0], arr[:, 1], arr[:, 2], 
                         cHull.simplices)

def plot3d(arr):
    assert(len(arr.shape) == 2)
    assert(arr.shape[1] == 3)

    mlab.plot3d(arr[:,0], arr[:,1], arr[:,2], line_width=0.8)

def expit(x):
    return 1/(1+np.exp(-x))

def makeArr():
    beta = np.linspace(0, 5, 1000)
    f = lambda x : np.array((x, x*x, 20 * expit((x-1)/0.1) * expit(4.5-x)/0.05))
    return f(beta).T

def makeArrPois():
    beta = np.linspace(0.01, 8, 1000)
    f = lambda y,beta : stats.poisson.pmf(y,beta)
    arr = np.zeros((1000, 3))
    arr[:,2] = beta
    arr[:,0] = f(2, beta)
    arr[:,1] = f(6, beta)

    return arr

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--test', action='store_true', default=False)
    parser.add_argument('-p', '--plot', action='store_true', default=False)
    args = parser.parse_args()

    if args.test:
        arr = testHelix()
    else:
        arr = makeArrPois()
       
    if args.plot:
        plot3d(arr)
    else:
        chPic3d(arr)
    mlab.show()

if __name__ == "__main__":
    main()
