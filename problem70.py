from utils import primes, memoize, phi, arePermutations
from collections import defaultdict

print arePermutations("87109", "79180")
s = {}



nn = 100000000000
mm = 100000000000
for n in range(2, 10**7 + 1):
	s = phi(n)
	if n / float(s) < nn and arePermutations(str(int(s)), str(int(n))):
		nn = n / s
		mm = n
		kk = s

print nn, mm, s

print phi(99)