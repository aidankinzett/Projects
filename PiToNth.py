import math
from sympy.mpmath import mp

def pi_to_n(n):
	if n <= 100:
		mp.dps = n
	else:
		mp.dps = 100

	return mp.pi
		
print pi_to_n(134)