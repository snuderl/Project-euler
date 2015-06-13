import utils
import math

def generate_composite_numbers(n):
	yield 4
	for i in range(5, n + 1, 2):
		for x in range(2, i):
			if i % x == 0:
				yield i
				break
		# Even numbers are always composite
		yield i + 1

MAX = 10000
composites = list([x for x in generate_composite_numbers(MAX) if x % 2 == 1])
primes = [1] + utils.primes(MAX)
for c in composites:
	exists = False
	for p in primes:
		if p >= c: break
		sq = (c - p) // 2
		pp = sq ** 0.5
		if pp == int(pp):
			exists = True
	if not exists:
		print c
		break

