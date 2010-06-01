(X, Y) = (1, 1)
for x in xrange(10, 100):
    for y in xrange(x + 1, 100):
        (sx, sy) = (str(x), str(y))

        if sx[1] == '0' and sy[1] == '0':
            continue
            
        if sx[0] == sy[0] and sy[1] != '0':
            if float(x) / float(y) == float(sx[1]) / float(sy[1]):
                (X, Y) = (X * x, Y * y)

        if sx[0] == sy[1] and sy[0] != '0':
            if float(x) / float(y) == float(sx[1]) / float(sy[0]):
                (X, Y) = (X * x, Y * y)

        if sx[1] == sy[0] and sy[1] != '0':
            if float(x) / float(y) == float(sx[0]) / float(sy[1]):
                (X, Y) = (X * x, Y * y)

        if sx[1] == sy[1] and sy[0] != '0':
            if float(x) / float(y) == float(sx[0]) / float(sy[0]):
                (X, Y) = (X * x, Y * y)

def gcd(a, b):
    while b:
        (a, b) = (b, a % b)
    return a

print Y / gcd(X, Y)
