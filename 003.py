from primes import is_prime

x = 2
y = 600851475143
while x < y:
    if is_prime(x):
        while y % x == 0:
            y = y/x
    x += 1
print y

# or

x = 2
y = 600851475143
while (x != y):
    if y % x == 0:
        y = y / x
    else:
        x += 1
print x

