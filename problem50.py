import utils
import itertools
import time

start = time.time()
BOUND = 1000000
current = (0,1)

primes = list(utils.primes(BOUND))
prime_arr = [False] * BOUND

for p in primes:
	prime_arr[p] = True

print ("Primes generated")
max_length = 0
for i in range(0, len(primes)):
	s = 0
	curr_length = 0
	for p in primes[i:]:
		s += p
		if s >= BOUND:
			break
		curr_length += 1
		if prime_arr[s]:
			if curr_length > max_length:
				max_length = curr_length
				print "New max: %s" % max_length
				print sum(primes[i:i+curr_length])

print (time.time() - start)





