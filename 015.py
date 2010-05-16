import math

# Central biomial coefficients
def combinations(n):
    p = math.factorial(2 * n)
    q = math.factorial(n)
    return p / (q * q)

print combinations(20)
