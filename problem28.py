import time
start=time.time()
i=1
s=1
diagonal = 3
while(True):
	if(diagonal>1001): break

	a = diagonal-1
	s+=sum((map(lambda x: x*a+i,range(1,5))))
	i+= 4*(diagonal-1)
	diagonal+=2

print i
print s
print time.time()-start