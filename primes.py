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

def prime_list(l):
    p = is_prime_list(l)
    return [x for x in xrange(2, l) if p[x]]
