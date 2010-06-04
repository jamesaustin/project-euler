import itertools

l = 1000000
is_prime = [False, False] + [True] * (l - 2)

for x in xrange(4, l, 2):
    is_prime[x] = False

for x in xrange(3, l / 2, 2):
    if is_prime[x] == True:
        for y in xrange(x * 2, l, x):
            is_prime[y] = False

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
