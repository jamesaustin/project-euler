import math

combinations = [0, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
numbers = [0,1,2,3,4,5,6,7,8,9]
counts = [0]

t = 1000000 - 1
while t != 0:
    if t - combinations[-1] >= 0:
        t -= combinations[-1]
        counts[-1] += 1
    else:
        counts.append(0)
        combinations.pop()
counts.append(0)

print '%i%i%i%i%i%i%i%i%i%i' % (numbers.pop(counts[0]), 
                                numbers.pop(counts[1]),
                                numbers.pop(counts[2]),
                                numbers.pop(counts[3]),
                                numbers.pop(counts[4]),
                                numbers.pop(counts[5]),
                                numbers.pop(counts[6]),
                                numbers.pop(counts[7]),
                                numbers.pop(counts[8]),
                                numbers.pop(counts[9]))


