import math

def d(n):
    count = 1
    for x in range(2, int(math.sqrt(n)) + 1):
        (d, r) = divmod(n, x)
        if r == 0:
            count += x
            if d != x:
                count += d

    return count

abundant_numbers = [ ]
for x in range(1, 28123):
    if d(x) > x:
        abundant_numbers.append(x)

sieve = [x for x in range(0, 28123)]
for v1 in abundant_numbers:
    for v2 in abundant_numbers:
        v = v1 + v2
        if v < 28123:
            sieve[v1 + v2] = 0

print sum(sieve)
