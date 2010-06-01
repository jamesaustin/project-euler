def pentagonal(n):
    return n * (3 * n - 1) / 2

pentagonals = { }
for x in xrange(1, 1000000):
    pentagonals[pentagonal(x)] = x

for x in xrange(1, 3000):
    for y in xrange(x + 1, 3000):
        px = pentagonal(x)
        py = pentagonal(y)
        if (px + py) in pentagonals and (py - px) in pentagonals:
            print py - px
