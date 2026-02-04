def if_(c, t, f):
	if c:
		t
	else:
		f

from math import sqrt

def real_sqrt(x):
	"""Return the real part of the square root of x."""
	return if_(x >= 0, sqrt(x), 0)
