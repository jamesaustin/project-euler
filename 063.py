count = 0
for n in xrange(1, 50):
    # 10 ^ 2 = 100, so must be < 10
    for x in xrange(1, 10):
        if len(str(pow(x, n))) == n:
            count += 1

print count