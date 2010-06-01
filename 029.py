N = 100
numbers = { }
for a in xrange(2, N + 1):
    for b in xrange(2, N + 1):
        numbers[a ** b] = 1
print len(numbers)
