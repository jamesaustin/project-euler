def d(n):
    count = 1
    for x in range(2, int(n ** 0.5) + 1):
        (d, r) = divmod(n, x)
        if r == 0:
            count += x
            if d != x:
                count += d

    return count

count = 0
for x in range(2, 10000):
    y = d(x)
    if d(y) == x:
        if y != x:
            print x, y
            count += y + x

print count / 2