count = 0
for x in xrange(10000):
    xs = str(x)
    for i in xrange(50):
        xs = str(int(xs) + int(xs[::-1]))
        if xs == xs[::-1]:
            break
    else:
        count += 1
print count