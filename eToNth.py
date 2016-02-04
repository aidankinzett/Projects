from sympy import *
from sympy.mpmath import *

def e_to_n(n):
	if n <= 100:
		return N(E, n)
	else:
		return N(E, 100)

print e_to_n(99)