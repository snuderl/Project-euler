from utils import primes_to_n, prime_sieve
from itertools import takewhile
import time

start = time.time()
BOUND = 1000000
current = (0,1)

primes = list(takewhile(lambda x: x < 1000000, prime_sieve()))
print ("Primes generated")
for i in range(1, len(primes)):
	for y in range(0, i):
		if i-y > current[0]:
			slice = primes[y:i]
			s = sum(slice)
			if(s in primes):
				current = (i-y, s)
				print(current)
print (current)
print (time.time() - start)

	





