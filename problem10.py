#sum of primes bellow 2000 000
import math,time

start = time.time()

i = 3
sum=2
while(i<2000000):
	found=True
	probavajDo=int(math.sqrt(i))+1
	for num in xrange(2,probavajDo):
		if(i%num==0):
			found=False
			break
		

	if(found):
		sum+=i

	i+=2

		


print sum
print "Time:" , time.time()-start