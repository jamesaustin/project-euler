(m, c) = (120, 3)
for p in xrange(120, 1001):
    a = 0
    for x in xrange(1, min(p, 500)):
        (y, my) = divmod(p * (p - 2 * x), 2 * (p - x))
        if my == 0 and y > 0 and p - x - y > 0:
            a +=1
    if a > c:
        (m, c) = (p, a)
print m
