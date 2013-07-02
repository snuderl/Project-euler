from decimal import Decimal

def cycle_length(n):
	remainders = []

	r=1
	while r!=0:

		if(r in remainders):
			break
		else:
			remainders.append(r)
			while(r < n):
				r*=10
			r = r%n
	
	first = -1
	for i,x in enumerate(remainders):
		if(x==r):
			return len(remainders)-i
	return 0
	

import math
a= [(cycle_length(x),x) for x in xrange(1,1000)]
c = 1
d = 0
for b in a:
	if b[0]>c:
		d=b[1]
		c=b[0]
print d
print c

	