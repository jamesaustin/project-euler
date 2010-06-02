def factorial(n):
    return reduce(lambda a, b: a * b, xrange(1, n + 1), 1)

factorials = [factorial(x) for x in xrange(0,10)]
m = 0
for x in xrange(3, factorials[9] * 7):
    if x == reduce( lambda a, b: factorials[int(b)] + a, str(x), 0 ):
        m += x
print m