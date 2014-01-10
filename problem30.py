count = 0
s = 0


def time(fun):
	def inner(*args, **kwargs):
		import time
		start = time.time()
		res = fun(*args, **kwargs)
		print "Time to run: " + str(time.time() - start)
		return res
	return inner

def pow(x):
	return x**5

def sumOfPowers(num):
	return sum(map(pow, map(int, [x for x in str(num)])))

@time
def calculate():
	return [x for x in range(2,999999) if x == sumOfPowers(x)]

nums = calculate()

print len(nums), sum(nums)
print nums