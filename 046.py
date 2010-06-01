primes = { }
def prime(p):
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

m = 3
while True:
    if prime(m) is False:
        for x in xrange(1, m):
            n = m - 2 * x * x
            if n > 0 and prime(n):
                break
        else:
            break
    m += 2
print m

# or

# Great answer from Project Euler forums
n = 3
primes = set()
while True:
    if all(n % p for p in primes):
        primes.add(n)
    elif not any((n-2*i*i) in primes for i in xrange(1, n)):
        break
    n += 2
print n