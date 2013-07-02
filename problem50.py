def primes_sieve1(limit):
    limitn = limit+1
    primes = dict()
    for i in range(2, limitn): primes[i] = True

    for i in primes:
        factors = range(i,limitn, i)
        for f in factors[1:]:
            primes[f] = False
    return [i for i in primes if primes[i]==True]



import time



start = time.time()

primes = primes_sieve1(1000)
n=0
r,s = 0,0
g = 0
for i in primes:
	n+=i
	g+=1
	if n>1000:
		break

	if n in primes:
		r=n
		s=g
print r,g
print time.time()-start

	





