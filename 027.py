import math

primes = { }
def prime(p):
    if p == 1 or p == 2:
        return True
    if p in primes:
        return primes[p]
    for x in range(3, int(math.sqrt(p)) + 1, 2):
        if p % x == 0:
            primes[p] = False
            return False
    primes[p] = True
    return True

(A, B, C) = (0, 0, 0)
for a in range(-999, 999, 1):
    for b in range(-999, 999, 1):
        (c, p) = (0, True)
        while p is True:
            N = c * c + a * c + b
            if N <= 0:
                break
            p = prime(N)
            c += 1
        c -= 1
        if c > C:
            (A, B, C) = (a, b, c)

print A * B