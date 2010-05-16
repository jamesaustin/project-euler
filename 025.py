(x, y) = (1, 1)
count = 2
while x < 10 ** (1000 - 1):
    (x, y) = (x + y, x)
    count += 1

print count