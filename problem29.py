
terms = {}

for x in range(2,101):
	for y in range(2,101):
		terms[x**y]=1

print len(terms.keys())