def ways(m, n):
	return m * (m + 1) * n * (n + 1) / 4


error = 1000000
m,n=0,0
for x in range(1, 1000):
	for y in range(1, 1000):
		w = ways(x, y)
		er = abs(2000000 - w)
		if er > error and w > 2000000:
			break
		if er < error:
			error = er
			m = x
			n = y

print error, m, n, ways(m, n), m* n