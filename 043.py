import itertools

m = 0
for n in itertools.permutations('0123456789'):
    if n[0] != '0':
        p = ''.join(n)
        if int(p[1:4]) % 2 == 0 and \
           int(p[2:5]) % 3 == 0 and \
           int(p[3:6]) % 5 == 0 and \
           int(p[4:7]) % 7 == 0 and \
           int(p[5:8]) % 11 == 0 and \
           int(p[6:9]) % 13 == 0 and \
           int(p[7:10]) % 17 == 0:
           m += int(p)
print m
