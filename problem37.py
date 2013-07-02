c = 0
s = 0
import mathTools,time
start = time.time()
gen = mathTools.genPrimes()
primeList = [False]*10**6
primes = mathTools.primes(10**6)
for x in primes:
	primeList[x]=True

for prime in primes:
	if(prime <10): continue
	p= str(prime)
	isPrime = True
	for i in xrange(1, len(p)):
		if(not primeList[int(p[i:len(p)])]):
			isPrime=False
			break
		if(not primeList[int(p[0:i])]):
			isPrime=False
			break
		
	if isPrime:
		c+=1
		s+=prime
		print prime

print c
print s
print time.time()-start