import random

def is_prime(p):
    if p == 1:
        return False
    if p == 2:
        return True
    if p % 2 == 0:
        return False
    for x in xrange(3, int(p ** 0.5) + 1, 2):
        if p % x == 0:
            return False
    return True

primes = { }
def is_prime_c(p):
    if p == 1:
        return False
    if p == 2:
        return True
    if p % 2 == 0:
        return False
    if p in primes:
        return primes[p]
    for x in xrange(3, int(p ** 0.5) + 1, 2):
        if p % x == 0:
            primes[p] = False
            return False
    primes[p] = True
    return True

def is_prime_list(l):
    p = [False, False] + [True] * (l - 2)

    for x in xrange(4, l, 2):
        p[x] = False

    for x in xrange(3, l / 2, 2):
        if p[x] == True:
            for y in xrange(x * 2, l, x):
                p[y] = False

    return p

def prime_set(l):
    p = [2, 3, 5, 7]
    for x in xrange(3, l, 2):
        root = int(x ** 0.5) + 1
        for y in p:
            if y > root:
                p.append(x)
                break
            if x % y == 0:
                break
        else:
            p.append(x)
    return set(p)

def prime_list(l):
    p = is_prime_list(l)
    return [x for x in xrange(2, l) if p[x]]


# Fast for large primes
def _to_binary(n):
    r = [ ]
    while (n > 0):
        r.append(n % 2)
        n = n / 2
    return r

def _test(a, n):
    b = _to_binary(n - 1)
    d = 1
    for i in xrange(len(b) - 1, -1, -1):
        x = d
        d = (d * d) % n
        if d == 1 and x != 1 and x != n - 1:
            return True # Complex
        if b[i] == 1:
            d = (d * a) % n
    if d != 1:
        return True # Complex
    return False # Prime

def is_prime_fast(n, s=10):
    for _ in xrange(1, s + 1):
        a = random.randint(1, n - 1)
        if (_test(a, n)):
            return False # n is complex
    return True # n is prime
