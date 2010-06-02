def factorial(n):
    return reduce(lambda a, b: a * b, xrange(1, n + 1), 1)

print reduce(lambda x, y: x + int(y), str(factorial(100)), 0)