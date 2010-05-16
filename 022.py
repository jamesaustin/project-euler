f = open('names.txt')
names = [x.strip('"') for x in f.read().split(',')]
names.sort()

count = 0
for i, n in enumerate(names):
    count += (i + 1) * reduce(lambda a, b: a + ord(b) - 64, n, 0)

print count

# or

print reduce(lambda a, (i, b): a + (i + 1) * reduce(lambda c, d: c + ord(d) - 64, b, 0), enumerate(names), 0)