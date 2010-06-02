limit = 5000000000000000
d = (2 * limit - 1) ** 0.5
N = int((d - 1) / 2) + 1 # Add 1 to simplify xrange tests and switch tests.

f = [2 * i * i + 2 * i + 1 for i in xrange(1, N)]

for i in xrange(1, N):
    p = f[i - 1]
    if p > 1:

        j = i + p
        while j < N:
            while (f[j - 1] % p == 0):
                f[j - 1] /= p
            j += p

        j = p - i - 1
        while j < N:
            while (f[j - 1] % p == 0):
                f[j - 1] /= p
            j += p

print len(filter(lambda i: f[i - 1] == 2 * i * i + 2 * i + 1, xrange(1, N)))
