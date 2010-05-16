def f(n):
    (d, m) = divmod(n, 2)
    if m == 0:
        return f(d)
    (d, m) = divmod(n, 5)
    if m == 0:
        return f(d)

    m = 1
    while True:
        if ((10 ** m) - 1) % n == 0:
            return m
        m += 1

(c, m) = (0, 0)
for n in range(1, 1000):
    x = f(n)
    if x > c:
        c = x
        m = n

print m
