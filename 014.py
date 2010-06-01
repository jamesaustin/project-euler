def next(x):
    (d, m) = divmod(x, 2)
    if m == 0:
        return d
    else:
        return (3 * x) + 1

(X, C) = (0, 0)
for x in xrange(999999, 1, -1):
    (y, c) = (x, 1)
    while y != 1:
        y = next(y)
        c += 1
    if c > C:
        (X, C) = (x, c)

print X

# or

history = { 1:1 }

def next2(x):
    if x not in history:
        (d, m) = divmod(x, 2)
        if m == 0:
            history[x] = 1 + next2(d)
        else:
            history[x] = 1 + next2(3 * x + 1)
    return history[x]

(X, C) = (0, 0)
for x in xrange(999999, 1, -1):
    c = next2(x)
    if c > C:
        (X, C) = (x, c)

print X
