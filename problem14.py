import time

start = time.time()
cache=[0]*10000001

bigest = 1
count = 1
for n in xrange(1,1000000):
	tmpC = 1
	tmpB = n
	while(n!=1):
		if(n%2==0):
			n=n/2
		else:
			n=3*n+1
		tmpC+=1

		if n<1000000 and cache[n]>0:
			tmpC = tmpC + cache[n]
			n=1

	cache[tmpB]=tmpC

	if(tmpC>count):
		count=tmpC
		bigest=tmpB
		
print bigest
print "Time:",time.time()-start

