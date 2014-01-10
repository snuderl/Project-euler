import utils
from itertools import combinations, takewhile, product, chain

primesSet = list(map(str, utils.primes(100000000)))
primes = list(takewhile(lambda x: int(x) < 10000, list(primesSet)))
primesSet = set(primesSet)


print len(primes), len(primesSet)


def checkAllPrimes(x):
    if not len(set(x)) == len(x):
        return False
    for y, z in combinations(x, 2):
        if not (y + z in primes and z + y in primes):
            return False
    return True


def checkAllPrimes2(x1, x2):
    for y in x1:
        if not (y + x2 in primes and x2 + y in primes):
            return False
    return True


# pairs = None

# print "Got primes"
# pairs = list(filter(checkAllPrimes,
#                     combinations(filter(lambda x: int(x) < 500000, list(primes)), 2)))
# candidates = set(chain.from_iterable(pairs))
# print len(candidates)
# triples = [list(pair) + [x] for x in candidates for pair in pairs if x not in pair and checkAllPrimes2(list(pair), x)]
# candidates = set(chain.from_iterable(triples))
# print len(candidates)
# fours = [list(pair) + [x] for x in candidates for pair in triples if x not in pair and checkAllPrimes2(list(pair), x)]
# candidates = set(chain.from_iterable(fours))
# print len(candidates)
# fives = [list(pair) + [x] for x in candidates for pair in fours if x not in pair and checkAllPrimes2(list(pair), x)]
# candidates = set(chain.from_iterable(fives))
# print fives

s = len(primes)
table = []
for i in range(s):
    table.append([False]*s)

for i1 in range(s-1):
    for i2 in range(i1 + 1, s):
        x1, x2 = primes[i1], primes[i2]

        if ( (x1 + x2) in primesSet and (x2 + x1) in primesSet):
            table[i1][i2] = True
            table[i2][i1] = True

print "Starting"
for i in range(s - 4):
    for i2 in range(i + 1, s - 3):
        if(not table[i][i2]):
            continue
        for i3 in range(i2 + 1, s - 2):
            if(not (table[i][i3] and table[i2][i3])):
                continue
            for i4 in range(i3 + 1, s - 1):
                if(not (table[i][i4] and table[i2][i4] and table[i3][i4])):
                    continue
                for i5 in range(i4 + 1, s):
                    if(not (table[i][i5] and
                        table[i2][i5] and
                        table[i3][i5] and
                        table[i4][i5])):
                        continue
                    indices = [i, i2, i3, i4, i5]
                    print[primes[x] for x in indices]
                    print sum(map(int, [primes[x] for x in indices]))

# triples = [list(pair) + [x] for x in candidates for pair in pairs if x not in pair and checkAllPrimes2(list(pair), [x])]
# print len(triples)
# fives = [list(pair) + list(triple) for pair in pairs for triple in triples if checkAllPrimes2(pair, triple)]
# print fives

# quadruples = list(
#     filter(
#         checkAllPrimes,
#         map(lambda (x, y): x + y, combinations(pairs, 2))))

# print len(quadruples)

# for x in primes:
#     for p in quadruples:
#         l = list(p)
#         l.append(x)
#         if checkAllPrimes(l):
#             print l
