m = 0
for x in range(1, 1000000, 2):
    s = str(x)
    if s == s[::-1]:
        b = bin(x)[2:]
        if b == b[::-1]:
            m += x
print m

# or

def binary_palindromic(n):
    t = 1
    x = 0
    for i in n:
        x += (ord(i) - 48) * t
        t *= 10

    b = bin(x)[2:]
    if b == b[::-1]:
        return x
    return 0

m = 0
for x in range(1, 999):
    n = str(x)
    m += binary_palindromic(n[:-1] + n[::-1])
    m += binary_palindromic(n + n[::-1])
print m

# or

import itertools

m = 0
for l in range(1, 4):
    for n in itertools.product('0123456789', repeat=l):
        if n[0] != '0':
            m += binary_palindromic(n[:-1] + n[::-1])
            m += binary_palindromic(n + n[::-1])
print m
