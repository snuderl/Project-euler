import math,time

start= time.time()

sqrt = [False]*800**2
for x in range(1,500):
	for y in range(1,500):
		a = x*x+y*y
		if(a**0.5<800):
			sqrt[a]=True

bigest = 0
count = {0:0}
most = 0
for a in xrange(1,1000/3):
	for b in xrange(a+1,1000/2):
		c = a*a+b*b
		if(sqrt[c]):
			p = a+b + c**0.5
			if(p<1000):
				count[p]=count.get(p,0)+1
				if(count[p]>count[most]):
					most = p
if count>bigest:
	bigest=count
	r=p

print most, count[most]
print time.time()-start