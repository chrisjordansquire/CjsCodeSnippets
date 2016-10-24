from ctypes import *
import numpy as N
import os

allocated_arrays = []
def allocate(dim, shape):
    print 'allocate called'
    x = N.zeros(shape[:dim], 'f4')
    allocated_arrays.append(x)
    ptr = x.ctypes.data_as(c_void_p).value
    print hex(ptr)
    print 'allocate returning'
    return ptr

lib = CDLL(os.path.join(os.getcwd(), 'libcallback.so'))
lib.foo.restype = None
ALLOCATOR = CFUNCTYPE(c_long, c_int, POINTER(c_int))
lib.foo.argtypes = [ALLOCATOR]

print 'calling foo'
lib.foo(ALLOCATOR(allocate))
print 'foo returned'

print allocated_arrays[0]
