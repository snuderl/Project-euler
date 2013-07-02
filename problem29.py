import mathTools

n = 0
used = [False]*101
a=mathTools.gen_primes()
for x in xrange(2,101):
	if(used[x]): continue
	n+=99
	used[x]=True
	while(True):
		x=x*x
		if(x>100): break
		n+=44
		used[x]=True

print n
