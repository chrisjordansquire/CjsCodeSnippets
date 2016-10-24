import numpy as np
import ctypes as c

_foo = np.ctypeslib.load_library('foo', '.')
_foo.bar.restype = c.c_int
_foo.bar.argtypes = [c.POINTER(c.c_double), c.c_int]

def bar(x):
    return _foo.bar(x.ctypes.data_as(c.POINTER(c.c_double)), len(x))

x = np.random.randn(10)
n = bar(x)
