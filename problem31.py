
coins = [1,2,5,10,20,50,100,200]
def time(fun):
	def inner(*args, **kwargs):
		import time
		start = time.time()
		res = fun(*args, **kwargs)
		print "Time to run: " + str(time.time() - start)
		return res
	return inner

from collections import defaultdict
def memoize(fun):
	store = defaultdict(dict)
	def inner(*args, **kwargs):
		key1, key2 = args[0], args[1]
		if key1 in store[key2]:
			return store[key2][key1]
		else:
			res = fun(*args)
			store[key2][key1] = res
			return res
	return inner


def count_change(total, coins):

	if(total == 0):
		return 1

	if(len(coins)==0):
		return 0

	head = coins[0]
	if(head > total):
		return 0

	return count_change(total, coins[1:]) + count_change(total-coins[0], coins)

@memoize
def count_change_1(total, coins_num):
	if coins_num <= 0: return 1
	res = 0
	while total >= 0:
		res = res + count_change_1(total, coins_num - 1)
		total -= coins[coins_num]
	return res

def count_change_3(total):
	ways = [0]*(total+1)
	ways[0] = 1
	for coin in coins:
		for j in range(coin, total+1):
			ways[j] = ways[j] + ways[j - coin]
	return ways[total]


print time(count_change)(200, coins)
print time(count_change_1)(200, len(coins)-1)
print time(count_change_3)(200)