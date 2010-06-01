def distinct_factors(n):
    f = 2
    last = 0
    limit = (n ** 0.5)
    while f <= limit:
        (d, r) = divmod(n, f)
        if r == 0:
            n = d
            limit = (n ** 0.5)
            if last != f:
                yield f
                last = f
        else:
            f += 1
    if n > 1:
        yield n

(c, n) = (0, 1)
while c != 4:
    if len(list(distinct_factors(n))) >= 4:
        c += 1
    else:
        c = 0
    n += 1
print n - 4
