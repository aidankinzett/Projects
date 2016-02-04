import math
from sympy.mpmath import *

fibonacci = lambda n: (phi**n - (((-1)**n)/phi**n))/sqrt(5)