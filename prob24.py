import itertools

candidates = list(range(0,10))


print list(itertools.permutations(candidates))[1000000-1]
