#Taken from example found online at hakantiftikci.wordpress.com
from ctypes import *
import math
import os
import os.path

cur_dir = os.getcwd()
library_path = os.path.join(cur_dir, 'quad.so') 


quadlib = CDLL(library_path) 

samplelibfun1 = quadlib.samplefun1
samplelibfun2 = quadlib.samplefun2

samplelibfun1.restype = c_double
samplelibfun1.argtypes = [c_double]

samplelibfun2.restype = c_double
samplelibfun2.argtypes = [c_double]

realFunction = CFUNCTYPE( c_double, c_double )

npow = c_int.in_dll(quadlib, "npow")
x = 2.0
for i in range(10):
    npow.value = i
    print "npow:%i => result(c-dll):%12.7f, result(Python):%12.7f" % (npow.value, samplelibfun2( x ), x+i*math.pow(x,i) )

quadlib.rectquad.argtypes = [realFunction, c_double, c_double, c_int]
quadlib.rectquad.restype = c_double


def Id(x):
    return x

def sqr(x):
    return x*x

print "_"*30
print "quadrature of c function samplelibfun1"
result = quadlib.rectquad( cast(samplelibfun1,realFunction ), c_double(0.), c_double(1.), c_int(64) )
print "result=",result


print "_"*30
print "quadrature of c function samplelibfun2 with parameter npow=3"
npow.value = 3
result = quadlib.rectquad( cast(samplelibfun2,realFunction ), c_double(0.), c_double(1.), c_int(64) )
print "result=",result


print "_"*30
print "quad of x->x"
for n in range(25,150,25):
    result = quadlib.rectquad( realFunction(Id), c_double(0.), c_double(1.), c_int(n) )
    print "result for subdivision %3i is %12.8f" % (n, result)

print "_"*30
print "quad of x->x*x"
for n in range(50,650,50):
    result = quadlib.rectquad( realFunction(sqr), c_double(0.), c_double(1.), c_int(n) )
    print "result for subdivision %3i is %12.8f" % (n, result)
