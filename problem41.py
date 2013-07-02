import mathTools, time
start = time.time()

def loop(remaining):
	if(len(remaining)==1):
		yield str(remaining[0])
	else:
		for x in remaining:
			for y in loop([y for y in remaining if y!=x]):
				yield str(x)+y



for x in loop(range(7,0,-1)):
	if(mathTools.isPandigital(x) and mathTools.isPrime(int(x))):
		print x
		break

print time.time()-start