import time

start = time.time()

def numberGenerator():
	i=0
	p = 10
	while True:
		if i*6 < p:
			i=i+1
			yield i
		else:
			i=p
			p*=10
			yield i



for i in numberGenerator():
	s = str(i)
	l = len(s)
	s = set(s)
	c=1
	for y in xrange(6,1,-1):
		number = i*y
		l1 = len(str(number))
		s1 =  set(str(number))
		if l==l1 and s ==s1:
			c+=1
			continue
		break
	if c>=5:
		print i,c
		break

print time.time()-start
