import utils
from collections import Counter
from itertools import tee, izip

def window(iterable, size):
    iters = tee(iterable, size)

    for i in xrange(1, size):
	    for each in iters[i:]:
	        next(each, None)
    return izip(*iters)

MAX = 1000000
primes = utils.primes(MAX)
def factor_consequtive(x):
	factors = utils.factor(x, primes)
	counts = Counter(factors)
	for k in counts:
		yield k ** counts[k]

def generate_consequtive():
	i = 1
	while True:
		yield set(factor_consequtive(i))
		i += 1


for a, b, c, d in window(generate_consequtive(), 4):
	if len(a.union(b).union(c).union(d)) == 16:
		print a
		break
