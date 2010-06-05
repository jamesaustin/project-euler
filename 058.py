from primes import is_prime

(a, b, c, d) = (0, 1, 2, 1)
while True:
    if is_prime(b + c):
        a += 1
    if is_prime(b + 2 * c):
        a += 1
    if is_prime(b + 3 * c):
        a += 1
    if is_prime(b + 4 * c):
        a += 1

    b += 4 * c
    d += 4
    
    if float(a) / float(d) < 0.1:
        break

    c += 2
print c + 1