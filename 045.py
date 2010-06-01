def triangle(n):
    return n * (n + 1) / 2

def pentagonal(n):
    return n * (3 * n - 1) / 2

def hexagonal(n):
    return n * (2 * n - 1)

def is_pentagonal(n):
    (_, r) = divmod( (0.5 + (0.25 + 6 * n) ** 0.5) / 3, 1)
    return (r == 0)

def is_hexagonal(n):
    (_, r) = divmod( (0.25 + (0.5 * n + 0.0625) ** 0.5), 1)
    return (r == 0)

m = 286
while True:
    t = triangle(m)
    if is_pentagonal(t) and is_hexagonal(t):
        break
    m += 1
print triangle(m)
