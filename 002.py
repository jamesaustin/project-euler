x = 1
y = 2

total = 0
while y <= 4000000:
    if y % 2 == 0:
        total += y
    next = y + x
    x = y
    y = next
print total
