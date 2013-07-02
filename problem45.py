from operator import itemgetter

x = 40755

tph = [1,1,1]
nList = [1,1,1]

import time
start = time.time()

while True:
	p = min(enumerate(tph), key=itemgetter(1))[0]
	nList[p]=nList[p]+1
	n=nList[p]
	if(p==0):
		tph[p]=n*(n+1)/2
	elif(p==1):
		tph[p]=n*(3*n-1)/2
	elif(p==2):
		tph[p]=n*(2*n-1)
	if(tph[0]==tph[1] and tph[1]==tph[2]):
		if(tph[0]>x):
			print tph[0]
			break


print time.time()-start