triples = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25), (20, 21, 29), (12, 35, 37), (9, 40, 41), (28, 45, 53)]
triples.extend([(p2, p1, p3) for (p1, p2, p3) in triples])
triples.sort(lambda (a1, a2, a3), (b1, b2, b3): cmp(a3, b3))
triples.insert(0, (1, 0, 1))
num_triples = len(triples)

N = 120

L = int(N * (2 - 2 ** 0.5))
combinations = [ (0, 0, 0) ]
def combiner(c, location):
    for i in xrange(c, num_triples):
        (x, y, l) = location
        (cx, cy, cl) = triples[i]
        (x, y, l) = (x + cx, y + cy, l + cl)
        if l <= L:
            combinations.append( (x, y, l) )
            combiner(i, (x, y, l))
combiner(0, (0, 0, 0))

space = { }
for (ax, ay, al) in combinations:
    for (bx, by, bl) in combinations:
        c = (ax - bx, ay - by, al + bl)
        try:
            space[c] += 1
        except:
            space[c] = 1

m = 0
for (x, y, l1), a in space.iteritems():
    for l2 in xrange(0, (N - l1) + 1):
        c = (-y, x, l2)
        b = space.get(c, 0)
        m += a * b
    
m -= sum([2 * (N / 2 / l) for (_, _, l) in triples]) + 1

print m
