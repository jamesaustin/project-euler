import itertools

def prime(p):
    for x in xrange(3, int(p ** 0.5) + 1, 2):
        if p % x == 0:
            return False
    return True

m = 0
for n in itertools.permutations('1234567'):
    if n[-1] in ['1', '3', '7']:
        p = int(''.join(n))
        if prime(p):
            m = max(m, p)
print m
