import time


count = 0

def wordSum(n):
	n = str.lower(n)
	a = ord("a")-1
	return reduce(lambda c,d: ord(d)+c-a, n, 0)


triangle = ["False"]*10**4
for i in xrange(1,10000):
	a = (i*(i+1))/2
	if(a>10**4): break
	triangle[a]=True

f = open("words.txt")
for x in f.xreadlines():
	print len(x)
	c = x[1:len(x)-1].split('","')
	for y in c:
		n = wordSum(y)
		if(triangle[n]==True):
			count+=1

print count

