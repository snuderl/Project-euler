import mathTools, time 

start = time.time()
pent = [False]*10**6
for i in xrange(1,10000):
	a = (3*i-1)*i
	if(a>10**6): break
	pent[a] = a
r=[]
for a in pent:
	if(a==False): continue
	for b in pent:
		if b==False: continue
		if(a+b)>10**6: continue

		if(not pent[a+b] == False and not pent[abs(a-b)] == False):
			print a,b


