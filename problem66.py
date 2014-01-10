

mVal = 2
mIn = 2

def solve(D):
	## x*x - D * y = 1
	for x in range(mVal, 100000000):
		x2 = x*x - 1
		if x2 % D == 0:
			y = (x2 / D) ** 0.5
			if y == int(y):
				return x
	print "Didnt found:("

for x in range(1, 1001):
    sq = x ** 0.5
    if int(sq) == sq:
        continue

    res = solve(x)
    if res and res > mVal:
    	mVal = res
    	mIn = x

print mVal, mIn
