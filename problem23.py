from math import sqrt
import time



def factorGenerator(n):
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



def getfactors(n):
    factors = set()
    for x in range(1, int((n**0.5)+1)):
        if n%x == 0:
            factors.add(x)
            q = int(n/x)
            if q != n:
                factors.add(q)

    return factors



def divisorGen(n):
    factors = list(factorGenerator(n))
    nfactors = len(factors)
    f = [0] * nfactors
    while True:
        yield reduce(lambda x, y: x*y, [factors[x][0]**f[x] for x in range(nfactors)], 1)
        i = 0
        while True:
            f[i] += 1
            if f[i] <= factors[i][1]:
                break
            f[i] = 0
            i += 1
            if i >= nfactors:
                return


def start(abc):
    start = time.time()
    abundant = []
    for i in xrange(12,abc):
        a = sum(getfactors(abc))-i
        if(a>i and a < abc): abundant.append(i)
    abundant.sort()
    print "Abundants:", len(abundant)
    print "Time1", time.time()-start


    l=[True]*(abc+1)
    def nums(a):
        for x in xrange(0,len(a)):
            b = a[x]
            for y in xrange(x,len(a)):
                c=b+a[y]
                if c>=abc+1:
                    break
                else:
                    l[c]=False
    nums(abundant)

    print "nums:", len(l)
    result = 0
    for i, t in enumerate(l):
       if t:
            result+=i

    print result
    print time.time()-start
    return l



start(21000)