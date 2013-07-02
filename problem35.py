import mathTools,time,itertools
start = time.time()

primes = mathTools.genPrimes()
numbers = [False]*(10**6)
prime = []
for x in mathTools.primes(10**6):
	prime.append(x)

	numbers[x]=True


c = 0
while(len(prime)>0):
	p = prime.pop()
	circular = True
	n = str(p)
	for a in xrange(1, len(n)):
		if(len(n)>1):
			n = n[1:len(n)]+n[0]
		if(numbers[int(n)]==False):
			circular=False
			break
	if(circular): 
		c+=1


print c
print time.time()-start

	
