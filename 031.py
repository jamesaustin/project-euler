m = 1 + 1
for c0 in xrange(0, 2):
    m0 = 200 - (100 * c0)
    for c1 in xrange(0, m0 / 50 + 1):
        m1 = m0 - (50 * c1)
        for c2 in xrange(0, m1 / 20 + 1):
            m2 = m1 - (20 * c2)
            for c3 in xrange(0, m2 / 10 + 1):
                m3 = m2 - (10 * c3)
                for c4 in xrange(0, m3 / 5 + 1):
                    m4 = m3 - (5 * c4)
                    m += m4 / 2 + 1
print m
