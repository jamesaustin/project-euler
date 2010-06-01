m = 0
# 1 not valid answer
N = (9 ** 5) * 5 + 1
for n in xrange(2, N):
    digits = [int(x) for x in str(n)]
    if n == sum([x ** 5 for x in digits]):
        m += n
print m