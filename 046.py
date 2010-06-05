from primes import is_prime

m = 3
while True:
    if is_prime(m) is False:
        for x in xrange(1, m):
            n = m - 2 * x * x
            if n > 0 and is_prime(n):
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