import itertools

from primes import is_prime_list

l = 10000
is_prime = is_prime_list(l)

solutions = set()
for c in itertools.combinations('1123345677899', 4):
    count = 0
    numbers = [ ]
    for d in itertools.permutations(''.join(c), 4):
        number = int(''.join(d))
        if is_prime[number]:
            numbers.append(number)
            count += 1
    if count >= 3:
        for x in numbers[:-2]:
            if x + 3330 in numbers and x + 6660 in numbers:
                solutions.add(x * 100000000 + (x + 3330) * 10000 + x + 6660)
solutions.remove(148748178147)
print list(solutions)[0]
