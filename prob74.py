

def fac(x):
	if x == 1:
		return 1
	if x == 0:
		return 1
	return x * fac(x - 1)

s = list(fac(x) for x in range(0, 10))

def intToDigits(x):
	return [int(y) for y in str(x).replace("0", "1")]

def calcPermutation(x):
	return "".join(sorted(str(x).replace("0", "1")))


count = 0
visited = [False] * 10**8
vals = [False] * 10**8
permutations = {}
for x in range(10**6, 1, -1):
	iteration = 0

	val = int(calcPermutation(x))
	visList = [val]

	while True:



		valZ = vals[val]
		if not valZ:
			digits = intToDigits(val)
			valZ = sum([s[y] for y in digits])
			vals[val] = valZ
		val = valZ
		iteration+=1


		if not visited[val]==False or val in visList:

			if visited[val]:
				iteration += visited[val]
			if val in visList:
				rev = list(visList[::-1])
				k = len(visList) - visList[::1].index(val)
				for i, z in enumerate(rev, 1):
					if i <= k:
						visited[z] = k
					else:
						visited[z] = i
			if iteration==60:
				count+= 1
			#print "1", iteration
			if x in [1454, 78, 69, 541]:
				print "->".join(map(str, visList + [val])), iteration
			break
		elif iteration == 61 and val == x:
			count+=1
			#print 2,iteration
			break

		visList.append(val)	


print count