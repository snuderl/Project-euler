
with open("keylog.txt") as f:
	numbers = [x.strip() for x in f.readlines()]


def recurse(strings, m):
	if len(strings) == 1:
		#print strings[0]
		l = len(strings[0])
		if l > m:
			return m * 10000
		else:
			return l

	mVal = 1000
	for s in strings:
		st = list([x for x in strings if x != s])
		for y in st:
			i = 0
			#print s,y
			for i in range(min(len(s), len(y)), 0, -1):
				#print s[-i:], y[:i], str(s[-i:]) == str(y[:i])
				if s[-i:] == y[:i]:
					break
			#print s,y
			string = s + y[i:]

			v = recurse([string] + [x for x in st if x != y], m)
			if v < mVal:
				mVal = v
	return mVal

def rec2(strings):
	if len(strings) == 1:
		#print strings[0]
		return len(strings[0])

	longestSkip, start, xs = 0, "", set()
	for s in strings:
		st = list([x for x in strings if x != s])
		for y in st:
			i = 0
			#print s,y
			for i in range(min(len(s), len(y)), 0, -1):
				if i < longestSkip:
					break
				#print s[-i:], y[:i], str(s[-i:]) == str(y[:i])
				if s[-i:] == y[:i]:
					break
			#print s,y
			if i > longestSkip:
				longestSkip = i				
				s1, y = sorted([s, y])
				start = s1
				xs = {y}
			elif i == longestSkip:
				s1, y = sorted([s, y])
				if s1 == start and not y in xs:
					xs.add((y))
	if longestSkip == 0:
		return len("".join(strings))
	else:
		mv = 0
		#print xs
		for z in xs:
			st = list([x for x in strings if x != start and x != z])
			v = rec2([start + z[longestSkip:]] + st)
			if v > mv:
				mv = v
		return mv

i = 20
print recurse(set(numbers[:i]), 30)
#print rec2(list(set(numbers[:i])))
