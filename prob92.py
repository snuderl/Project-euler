###Square digit chain###
from utils import memoize

@memoize
def chain(x):
	if(x) == "1":
		return "1"
	if(x) == "89":
		return "89"

	else: return chain(str(sum([int(digit)**2 for digit in x])))

s = sum([1 for x in range(2, 10**4) if chain("".join(sorted(str(x)))) == "89"])
print s