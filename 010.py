import math

primes = [2]
x = 3
m = 2
while x < 2000000:
    r = math.pow(x, 0.5)
    for p in primes:
        if p > r:
            primes.append(x)
            m += x
            break
        if x % p == 0:
            break
    else:
        primes.append(x)
        m += x
    x += 2
print m

# or

l = 2000000
primes = [True] * l

for x in xrange(4, l, 2):
    primes[x] = False

for x in xrange(3, l / 2, 2):
    for y in xrange(x * 2, l, x):
        primes[y] = False

m = 2
x = 3
while x < l:
    if primes[x]:
        m += x
    x += 2
print m

