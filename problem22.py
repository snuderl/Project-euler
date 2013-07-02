def getNameValue(x):
	y = 0
	for i in x.lower():
		y+=ord(i)-96
	return y

import time
tic = -time.time()
lines = open("names.txt").read().replace('"',"").split(",")
lines.sort()
y= 0

for i, line in enumerate(lines):
	y+=(getNameValue(line)*(i+1))

print y
print tic+time.time()