from primes import is_prime_c

(A, B, C) = (0, 0, 0)
for a in xrange(-999, 999, 1):
    for b in xrange(-999, 999, 1):
        (c, p) = (0, True)
        while p is True:
            N = c * c + a * c + b
            if N <= 0:
                break
            p = is_prime_c(N)
            c += 1
        c -= 1
        if c > C:
            (A, B, C) = (a, b, c)

print A * B