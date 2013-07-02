import math

sumDivisors=[0]*10**6
i=0
def divisors(x):
	div=[1]
	s=0
	for i in xrange(2, int(math.sqrt(x))):
		if(x%i==0):
			div.append(i)
			div.append(x/i);
			div = list(set(sumDivisors[x/i]+div))
			break


	sumDivisors[x]=div
	return sum(div)

searched = [False]*10**6
longest = 0
for x in xrange(1,10**6):
	divisors(x)

print "1"
for i,x in enumerate(sumDivisors[1:]):
	sumDivisors[i+1]=sum(x)


checked = [False]*10**6
longest = 0
for i,x in enumerate(sumDivisors[1:]):
	if(checked[i+1]==False and checked[x] == False):
		checked[i+1]=True
		checked[x]=True
		count = 2
		l = [i+1,x]
		while(x<10**6 and checked[x]==False):
			x = divisors[x]
			checked[x]=True
			if(x in l):
				count = len(l)-l.index(x)
				if count>longest: count +=1
				break

print longest

