count = 0
(a, b) = (1, 1)
for x in xrange(1000):
    (a, b) = (2 * b + a, a + b)
    if len(str(a)) > len(str(b)):
        count += 1
print count
