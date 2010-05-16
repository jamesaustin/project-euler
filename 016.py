d = 2 ** 1000

s = 0
while d != 0:
    (d, m) = divmod(d, 10)
    s += m

print s