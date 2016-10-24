import ctypes as C
import numpy as np
import os

if __name__ == '__main__':
    print 'testing'
    a = np.array(np.random.random(45), dtype=np.float32)
    lib = C.CDLL(os.path.join(os.getcwd(), 'a.so'))
    f_load_index = lib.sum_float_numpy_array
    f_load_index.argtypes = [np.ctypeslib.ndpointer(dtype = np.float32), C.c_int]
    f_load_index.restype = C.c_float
    print 'python says sum is:', a.sum()
    print 'eigen instead says:', f_load_index(a, len(a))

    n = 10
    a = np.array(range(10), dtype=np.float64)
    b = a.copy()
    c = np.zeros(n, dtype=np.float64)

    e_vec_sum = lib.sum_double_numpy_array
    tmp = np.ctypeslib.ndpointer(dtype=np.float64)
    e_vec_sum.argtypes=[tmp, tmp, tmp, C.c_int]

    print 'python says sum is: ', a+b
    e_vec_sum(a, b, c, len(a))
    print 'eigen says:', c

