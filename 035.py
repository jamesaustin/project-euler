from primes import is_prime_c

def circular_prime(x):
    if is_prime_c(x):
        s = str(x)
        for n in xrange(len(s) - 1):
            s = s[1:] + s[0]
            if not is_prime_c(int(s)):
                return False
        else:
            return True

c = 1
for x in xrange(3, 199999, 2):
    if circular_prime(x):
        if x > 99999:
            c += len(str(x))
        else:
            c += 1
print c

# or

import itertools

c = 2 # 2, 5
for l in xrange(1, 7):
    for m in itertools.product('acgi', repeat=l):
        t = 1
        x = 0
        for i in m:
            x += (ord(i) - 96) * t
            t *= 10

        if circular_prime(x):
            c += 1
print c