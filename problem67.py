fileName = "triangle.txt"
file = open(fileName)
a = []
for line in file:
	line=line[:len(line)-1]
	a.append(line)


parsed =[]
for counter,line in enumerate(a):
	parsed.append(line.split(" "))

parsed.reverse()
parsed = [map(int, x) for x in parsed]


import time
start = time.time()
for counter,line in enumerate(parsed):
	for i,current in enumerate(line):
		if(i==len(line)-1):
			continue
		next=line[i+1]
		if(current > next):
			parsed[counter+1][i]+=current
		else:	
			parsed[counter+1][i]+=next

print parsed[-1][-1]

print time.time()-start