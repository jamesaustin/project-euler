def factorial(n):
    return reduce(lambda a, b: a * b, xrange(1, n + 1), 1)

# Central biomial coefficients
def combinations(n):
    p = factorial(2 * n)
    q = factorial(n)
    return p / (q * q)

print combinations(20)
