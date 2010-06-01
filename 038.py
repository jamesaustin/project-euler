m = 918273645
for x in xrange(9000,10000):
    p = str(x) + str(x * 2)
    if '123456789'.strip(p) == '':
        m = max(int(p), m)
print m