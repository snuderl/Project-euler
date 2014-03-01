fileName = "triangle.txt"

parsed = [map(int, x.split()) for x in open(fileName)]
parsed.reverse()

import time
start = time.time()
###Build a trinagle of shortest paths starting from the bottom
for counter,line in enumerate(parsed):
	for i, current in enumerate(line):
		if(i==len(line)-1):
			continue
		next=line[i+1]
		if(current > next):
			parsed[counter+1][i]+=current
		else:	
			parsed[counter+1][i]+=next

print parsed[-1][-1]

print time.time() - start