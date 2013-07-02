#10 001st prime number
import math,time

start = time.time()

primesFound = 3
currentPrime = 7
i = 7
while(primesFound!=10001):
	found=True
	probavajDo=int(math.sqrt(i))+1
	for num in range(2,probavajDo):
		if(i%num==0):
			found=False
			break
		

	if(found):
		primesFound+=1
		currentPrime=i
		

	i+=2

print currentPrime
print "Time:", (time.time()-start)
