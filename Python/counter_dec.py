# Yep....this is how decorators work
class counter(object):

	def __init__(self, func):
		self.func = func
		self.counter = 0

	def __call__(self, *args, **kwargs):
		self.counter += 1
		return self.func(*args, **kwargs)

@counter
def fib(n):
	if n==1:
		return 1
	if n==2:
		return 2 
	return fib(n-1) + fib(n-2)

