import mathTools
import itertools

def isPermutation(x,y):
	return sorted(map(int, str(x)))==sorted(map(int, str(y)))



l = []
for x in mathTools.genPrimes():
	if x>10000:
		break
	if x>1000:
		l.append((x))

n= 3330
for x in l:
	n1 = x+n
	if n1 in l and isPermutation(n1,x):
		n2 = n1+n
		if n2 in l and isPermutation(n2,n1):
			print str(x)+ str(n1)+str(n2)

print isPermutation(123,231)







