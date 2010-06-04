m = 0
for a in xrange(100):
    for b in xrange(100):
        m = max(sum([ int(d) for d in str(a ** b) ]), m)
print m
