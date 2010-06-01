for x in xrange(2, 1000):
    for y in xrange(x, 1000):
        z = 1000 - x - y
        if x * x + y * y == z * z:
            print x * y * z
            exit()