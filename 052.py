x = 0
while True:
    x += 1
    s1 = list(str(x))
    s2 = list(str(x * 2))
    s1.sort()
    s2.sort()
    if s1 == s2:
        s3 = list(str(x * 3))
        s3.sort()
        if s1 == s3:
            s4 = list(str(x * 4))
            s4.sort()
            if s1 == s4:
                s5 = list(str(x * 5))
                s5.sort()
                if s1 == s5:
                    s6 = list(str(x * 6))
                    s6.sort()
                    if s1 == s6:
                        break
print x

# or

def f(x):
    s = list(str(x))
    s.sort()
    return s

x = 0
while True:
    x += 1
    if f(x) == f(x * 2) == f(x * 3) == f(x * 4) == f(x * 5) == f(x * 6):
        break
print x