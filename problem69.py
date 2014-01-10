from utils import primes, memoize
primes = primes(10000000)
primeSet = set(primes)

@memoize
def factors(x):    
    if x in primeSet:
        return {x}
    t = x
    for i in primes:
        if t % i == 0:
            t = t / i
            break
    return {t, i} | factors(t)

###Calculates the number of relatively prime numbers up to x
@memoize
def phi(x):
    if x in primeSet:
        return x - 1.
    for p in primes:
        c = 0
        s = x
        if x % p == 0:
            while s % p == 0:
                c += 1
                s = s / p
            if c == 1:
                return phi(p) * phi(x / p)
            else:
                return phi(s * p) * (p ** (c - 1) * (p - 1))

nn = 0
mm = 0

# for x in range(2, 10**6 + 1):
#     s = x / float(phi(x))
#     if s > nn:
#         nn = s
#         mm = x

print nn, mm

###Final solution is the product of first n primes.... such that it is smaler than target value
t = 1
for x in primes:
    t = t * x
    if t > 10**6 + 1:
        t = t / x
        break
print t, t/2