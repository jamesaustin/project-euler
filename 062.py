cubes = { }
answers = [ ]

x = 1
digits = 0
while True:
    x3 = x * x * x
    s3 = tuple(sorted(str(x3)))

    if digits > 0 and len(s3) > digits:
        break

    a3 = cubes.setdefault(s3, [ ])
    a3.append(x3)
    if len(a3) == 5:
        digits = len(s3)
        answers.append(a3)

    x += 1

print min(map(min, answers))
