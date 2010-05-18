import math

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
    for x in range(3, int(math.sqrt(p)) + 1, 2):
        if p % x == 0:
            primes[p] = False
            return False
    primes[p] = True
    return True

def circular_prime(x):
    if prime(x):
        s = str(x)
        for n in range(len(s) - 1):
            s = s[1:] + s[0]
            if not prime(int(s)):
                return False
        else:
            return True

c = 1
for x in range(3, 1000000, 2):
    if circular_prime(x):
        c += 1
print c

# or

import itertools

c = 2 # 2, 5
for l in range(1, 7):
    for m in itertools.product('acgi', repeat=l):
        t = 1
        x = 0
        for i in m:
            x += (ord(i) - 96) * t
            t *= 10

        if circular_prime(x):
            c += 1
print c