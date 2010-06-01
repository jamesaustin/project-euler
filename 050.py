l = 1000000

is_prime = [False, False] + [True] * (l - 2)

for x in range(4, l, 2):
    is_prime[x] = False

for x in range(3, l / 23, 2):
    if is_prime[x] == True:
        for y in range(x * 2, l, x):
            is_prime[y] = False

prime_list = [x for x in xrange(2, l) if is_prime[x]]

(n, m) = (0, 0)
for i in xrange(0, len(prime_list) - 1):
    
    prime_sum = 0
    for j in xrange(i, len(prime_list) - 1):
        prime_sum += prime_list[j]
        if prime_sum >= l:
            break
    
    for k in xrange(j, i, -1):
        prime_sum -= prime_list[k]
        if is_prime[prime_sum]:
            break
    
    d = k - i
    if d > n:
        (n, m) = (d, prime_sum)

print m
