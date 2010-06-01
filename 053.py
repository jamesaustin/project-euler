import math

l = 100

factorials = [math.factorial(x) for x in xrange(0, l + 1)]

count = 0
for n in xrange(1, l + 1):
    for r in xrange(1, (n / 2) + 1):
        if factorials[n] / (factorials[r] * factorials[n - r]) > 1000000:
            if r * 2 == n:
                count += 1
            else:
                count += 2
print count
