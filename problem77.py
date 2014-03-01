def memWays(fun):
	store = {}
	def inner(n, nums):
		if nums:
			m = nums[0]
			val = store.get((n, m))
			if val:
				return val
			else:
				val = fun(n, nums)
				store[(n, m)] = val
				return val
		else:
			return fun(n, nums)
	return inner


@memWays
def ways(n, nums):
	#print n, nums
	if not nums:
		return 0

	m = nums[0]
	if(m == n):
		return 1 + ways(n, nums[1:])
	elif(m < n):
		return ways(n - nums[0], nums) + ways(n, nums[1:])
	else:
		while True:
			nums = nums[1:n]
			if not nums:
				return 0
			elif(nums[0] >= n):
				return ways(n, nums)

from utils import primes
p = primes(100)
from time import time
start = time()
for x in range(1, len(p)):
	if ways(x, p) > 5000:
		print x
		break
print time() - start