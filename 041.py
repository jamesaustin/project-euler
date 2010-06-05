import itertools

from primes import is_prime

m = 0
for n in itertools.permutations('1234567'):
    if n[-1] in ['1', '3', '7']:
        p = int(''.join(n))
        if is_prime(p):
            m = max(m, p)
print m
