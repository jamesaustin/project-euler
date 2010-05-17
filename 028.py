m = 1
for n in range(1, (1001  / 2) + 1):
    m += 4 * (4 * (n ** 2) + n + 3 - 2 * ((n + 2) % (n+1)))
print m
