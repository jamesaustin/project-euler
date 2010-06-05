from primes import is_prime_list

primes = [2]
x = 3
m = 2
while x < 2000000:
    r = x ** 0.5
    for p in primes:
        if p > r:
            primes.append(x)
            m += x
            break
        if x % p == 0:
            break
    else:
        primes.append(x)
        m += x
    x += 2
print m

# or

l = 2000000
primes = is_prime_list(l)

m = 2
x = 3
while x < l:
    if primes[x]:
        m += x
    x += 2
print m

