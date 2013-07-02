import math

for i,x in enumerate(xrange(5,10)):
	print i,x

def divisors(x):
	div=[1]
	s=0
	for i in xrange(2, int(math.sqrt(x))):
		if(x%i==0):
			s=s+i+x/i;

	
	return s

divs=[]
checked=[]

import time
start= time.time()

for i in xrange(1,10000):
	if(i not in checked):
		x = divisors(i)
		if(x<10000 and not x==i):
			y=divisors(x)
			if(y==i):
				divs.append(i)
				divs.append(x)
				checked.append(x)
	
print sum(divs)
print time.time()-start
	
	