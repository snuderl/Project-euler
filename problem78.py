from utils import memoize

def memWays(fun):
	store = {}
	def inner(n, m):
		if m > 0:
			val = store.get((n, m))
			if val:
				return val
			else:
				val = fun(n, m)
				store[(n, m)] = val
				return val
		else:
			return fun(n, m)
	return inner

@memWays
def ways(n, m):
	s = 0
	while True:
		if m <= 0:
			return s

		queue = []
		if(m == n):
			s += 1
			m -= 1
		elif(m < n):
			return s + ways(n - m, m) + ways(n, m-1)
		else:
			return s + ways(n, n)
	

bound = 1000000
@memoize
def p(n):
	if n < 0:
		return 0
	if n == 0:
		return 1
	else:
		s = 0
		a = 2
		b = 1
		k = 4
		sgn = 1
		while (n >= a):
			s += sgn * (p(n - a) + p(n - b))
			a += k + 1
			b += k
			sgn *= -1
			k += 3

		if n >= b:
			s += sgn * p(n - b)
		return s % bound


for x in range(1, 1000000):
	if p(x) % bound == 0:
		print x
		break

