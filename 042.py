triangles = [ (n * (n + 1)) / 2 for n in xrange(1, 100) ]

f = open('words.txt')
words = [x.strip('"') for x in f.read().split(',')]

count = 0
for w in words:
    if reduce(lambda a, b: a + ord(b) - 64, w, 0) in triangles:
        count += 1

print count
    