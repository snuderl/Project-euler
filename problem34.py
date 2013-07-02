import math,time
start = time.time()
values = [math.factorial(x) for x in range(0,10)]
t = 0
for i in xrange(3,1000000):
	x = str(i)
	value = sum([values[int(a)] for a in x])
	if(i==value):
		t+=value
		print i

print t
print time.time()-start

