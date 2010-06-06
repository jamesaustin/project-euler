print (28433 * pow(2, 7830457, 10 ** 10) + 1) % 10 ** 10

# or

m = 1
t = 10 ** 10
c = 2 ** 8
p = 2 ** c
for x in xrange(0, 7830457 - c, c):
    m = (m * p) % t

m *= 2 ** (7830457 % c)
m *= 28433
m += 1

print m % t

# or

print (28433 * reduce(lambda a, b: (a * p) % t, xrange(0, 7830457 - c, c), 1) * (2 ** (7830457 % c)) + 1) % t
