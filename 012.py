t = 0
x = 0
while True:
    t += x
    divisors = 2 # 1 and itself
    for y in xrange(2, int(t ** 0.5)):
        if t % y == 0:
            divisors += 2
    if divisors > 500:
        break
    x += 1

print t
    