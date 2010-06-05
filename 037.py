from primes import is_prime

def truncatable_prime(p):
    d = 10
    (tl, tr) = (p, p)
    while tl > 10:
        tl = p / d
        tr = p % d
        if not is_prime(tl) or not is_prime(tr):
            return False
        d *= 10
    return True

x = 11
m = 0
n = 0
while n < 11:
    if is_prime(x):
        if truncatable_prime(x):
            m += x
            n += 1
    x += 2
print m

# or

import itertools

m = 23 + 53
n = 2
l = 2
while n < 11:
    # Suitable combinations
    for c in itertools.product('1379', repeat=l):

        # Convert n to an int
        t = 1
        x = 0
        for i in c:
            x += (ord(i) - 48) * t
            t *= 10

        # Test x
        if is_prime(x):
            if truncatable_prime(x):
                m += x
                n += 1
    l += 1
print m