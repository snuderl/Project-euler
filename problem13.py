
def createTriangleNumbers():
	sum = 0
	for n in xrange(1,1000000,1):
		sum+=n
		yield sum

def getNumDivisors(num):
	count = 0
	import math
	for n in xrange(1,num+1):
		if num%n == 0:
			count+=1
	return count

import time
start = time.time()

for n in createTriangleNumbers():
	if(n%1024*1024!=0): continue
	divisors=getNumDivisors(n)
	print n,":",divisors
	if(divisors>500): 
		print n
		break

print "Time:", time.time()-start
