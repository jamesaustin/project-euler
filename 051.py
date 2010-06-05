from primes import is_prime_list

import itertools

l = 1000000
is_prime = is_prime_list(l)

def f():
    for (n1, n2 ,n3) in itertools.product('123456789', repeat=3):
        s = set()
        for digits in itertools.permutations( (n1, n2, n3, '*', '*', '*') ):
            s.add(digits)
        for digits in s:
            c = 0
            first = 0
            for y in xrange(0, 10):
                p = int(''.join(digits).replace('*', str(y)))
                if is_prime[p]:
                    c += 1
                    if first == 0:
                        first = p
            if c == 8:
                return first

print f()
