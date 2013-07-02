def getFactors(n):
    c = 0
    i = 2
    factors = []
    while n>1:
        while n%i==0:
            n=n/i
            c+=1
        if not c==0:
            yield (i,c)
        c=0
        i+=1



def getDivisors(n):
    factors = set()
    for x in range(1, int((n**0.5)+1)):
        if n%x == 0:
            factors.add(x)
            q = int(n/x)
            if q != n:
                factors.add(q)

    return factors

def genPrimes():
    """ Slow. Generate an infinite sequence of prime numbers.
    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    D = {}  

    # The running integer that's checked for primeness
    q = 2  

    while True:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            # 
            yield q        
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next 
            # multiples of its witnesses to prepare for larger
            # numbers
            # 
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]

        q += 1

def isPrime(n):
    '''check if integer n is a prime'''
    # range starts with 2 and only needs to go up the squareroot of n
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True

def higestCommonDivisor(no1,no2):
    while no1!=no2:
        if no1>no2:
            no1-=no2
        elif no2>no1:
            no2-=no1
    return no1

def primes(n): 
    if n==2: return [2]
    elif n<2: return []
    s=range(3,n+1,2)
    mroot = n ** 0.5
    half=(n+1)/2-1
    i=0
    m=3
    while m <= mroot:
        if s[i]:
            j=(m*m-3)/2
            s[j]=0
            while j<half:
                s[j]=0
                j+=m
        i=i+1
        m=2*i+3
    return [2]+[x for x in s if x]


def baseConvert(num, b):
    """convert positive decimal integer n to equivalent in another base (2-36)"""

    return ((num == 0) and  "0" ) or ( baseConvert(num // b, b).lstrip("0") + "0123456789abcdefghijklmnopqrstuvwxyz"[num % b])

def isPandigital(x):
    g = set(str(x))
    if not len(str(x)) == len(g):
        return False
    if("0" in g): return False
    for a in map(str,range(1,len(g))):
        if(not a in g):
            return False
    return True