f = open('cipher1.txt')
cipher = [int(x) for x in f.read().split(',')]

(a, z) = (ord('a'), ord('z'))
def codes():
    for x in xrange(26):
        for y in xrange(26):
            for z in xrange(26):
                yield [a + x, a + y, a + z]

(s, m) = (0, 0)
for code in codes():
    uncoded = [ code[x % 3] ^ cipher[x] for x in xrange(len(cipher)) ]
    n = sum([x for x in uncoded if x >= a and x <= z])
    if n > m:
        (s, m) = (sum(uncoded), n)

print s
