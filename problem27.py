import mathTools

import time

start = time.time()
primeGen = mathTools.gen_primes()
primes = [False]*(104729+1)
primesLower = []
for i in xrange(0,10000):
	prime = primeGen.next()
	primes[prime]=True
	if(prime<1000):
		primesLower.append(prime)





longest = 0
pair = (0,0)
for a in xrange(-999,1000,2):
	for b in primesLower:
		for i in xrange(0, 10000):
			s =i*i+a*i+b
			if(s>len(primes)): break
			else:
				if(primes[s]):
					if(i>longest):
						longest = i+1
						pair = (a,b)
				else: break
				
					

print longest
print pair
print time.time()-start

