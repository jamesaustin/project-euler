primes = [2]
x = 3
while len(primes) != 10001:
    for p in primes:
        if x % p == 0:
            break
    else:
        primes.append(x)
    x += 2

print primes[-1]    