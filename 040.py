def d(n):
    num_digits = 1
    n = n - 1
    while True:
        numbers = 9 * num_digits * (10 ** (num_digits - 1))
        if n <= numbers:
            break
        n -= numbers
        num_digits += 1
    return int(str((n / num_digits) + (10 ** (num_digits - 1)))[n % num_digits])

print d(1) * d(10) * d(100) * d(1000) * d(10000) * d(100000) * d(1000000)
