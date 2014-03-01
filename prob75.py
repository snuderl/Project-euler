from collections import Counter
from itertools import count

def gcd(m, n):
    """Return the greatest common divisor of m and n."""
    while n != 0:
        m, n = n, m % n
    return m

def coprime(m, n):
    """Return True iff m and n are coprime."""
    return gcd(m, n) == 1

def all_primitive_triples():
    """Generate all primitive Pythagorean triples, together with a lower
    bound on the perimeter for which all triples have been generated
    so far.

    """
    for m in count(1):
        for n in range(1, m):
            if (m + n) % 2 and coprime(m, n):
                a = m * m - n * n
                b = 2 * m * n
                yield a, b, m * m + n * n, 2 * m * (m + 1)

def problem75(limit):
    """Return the number of values of L <= limit such that there is
    exactly one integer-sided right-angled triangle with perimeter
    L.

    """
    triangles = Counter()
    for a, b, c, q in all_primitive_triples():
        if q > limit:
            break
        p = a + b + c
        for i in range(p, limit + 1, p):
            triangles[i] += 1
    return sum(n == 1 for n in triangles.values())

print problem75(1500000)