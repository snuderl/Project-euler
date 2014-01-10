from itertools import permutations
from collections import Counter, defaultdict

s = 2000000000
cubesSet = {str(x*x*x) for x in range(1, int(s**0.34)) if x*x*x < s}

counter = defaultdict(int)
lookup = {}
for x in range(1,10000):
    st = str(x*x*x)
    hash = ''
    hash = "".join(sorted(st))
    counter[hash] += 1
    if hash not in lookup:
        lookup[hash] = st

for k,v in counter.iteritems():
    if v > 4:
        print lookup[k], v
# for x in range(1, s):
# 	cube = x * x * x
# 	if cube >= s:
# 		break
# 	cubes[cube] = True
# print "here"
# while cubesSet:
#     st = cubesSet.pop()
#     cubesSet.discard(st)
#     count = 1
#     for x in permutations(st):
#         x = "".join(x)
#         if not x == st and x in cubesSet:
#             count += 1
#             #cubsSet2.discard(x)
#             cubesSet.discard(x)
#             #print st, x
#     if count > 2:
#     	print count, st