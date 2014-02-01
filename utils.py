
from collections import defaultdict


def primes(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns  a list of primes < n """
    sieve = [True] * int(n / 2)
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[int(i / 2)]:
            sieve[int(i * i / 2)::i] = [False] * \
                int((n - i * i - 1) / (2 * i) + 1)
    return [2] + [2 * i + 1 for i in range(1, int(n / 2)) if sieve[i]]


def prime_sieve():
    primes = [2, 3]
    yield 2
    yield 3
    n = 3
    while True:
        n += 2
        if not any(map(lambda x: n % x == 0, primes)):
            primes.append(n)
            yield n

def primes_sieve2(n):
    table = [False] + [True, False] * (n / 2)
    if n % 2 == 1:
        table.append(True)
    primes = []
    for x in range(3, int(n ** 0.5 + 1), 2):
        if table[x]:
            table[x * x :: x] = [False] * int((n - x * x) / x + 1)
            primes.append(x)

    for y in range(int(n ** 0.5 + 1), n):
        if table[y]:      
            primes.append(y)

    return [2] + primes


#for x in range(2, 100):
    #print (primes_sieve2(x))
print sum(primes_sieve2(10**6))


def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p * 2, n + 1, p)))
    return primes


def primes_to_n(N):
    for x in prime_sieve():
        if x < N:
            yield x
        else:
            break


def isPalindrome(x):
    i = str(x)
    if(len(i) % 2 == 0):
        return i[0:len(i) / 2] == i[len(i) / 2:len(i)][::-1]
    else:
        return i[0:len(i) / 2] == i[len(i) / 2 + 1:len(i)][::-1]


def time(fun):
    def inner(*args, **kwargs):
        import time
        start = time.time()
        res = fun(*args, **kwargs)
        print("Time to run: " + str(time.time() - start))
        return res
    return inner


def memoize(fun):
    '''
    Currently works only for 2 parameters
    '''

    store = defaultdict(dict)

    def inner(*args, **kwargs):
        if args in store:
            return store[args]
        else:
            res = fun(*args)
            store[args] = res
            return res
    return inner

#primesList = primes(10000000)
#primesSet = set(primesList)

@memoize
def factors(x):    
    if x in primesSet:
        return {x}
    t = x
    for i in primesList:
        if t % i == 0:
            t = t / i
            break
    return {t, i} | factors(t)

###Calculates the number of relatively prime numbers up to x
@memoize
def phi(x):
    if x in primesSet:
        return x - 1.
    for p in primesList:
        c = 0
        s = x
        if x % p == 0:
            while s % p == 0:
                c += 1
                s = s / p
            if c == 1:
                return phi(p) * phi(x / p)
            elif s == 1:
                return (p ** (c - 1) * (p - 1))
            else:
                return phi(s) * (p ** (c - 1) * (p - 1))

#print phi(99)

def arePermutations(str1, str2):
  s1 = "".join(sorted(str1))
  s2 = "".join(sorted(str2))
  return s1 == s2
